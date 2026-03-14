#!/usr/bin/env python3
"""
Thread Monitor - Theo dõi và phân tích threads trên Voz.vn
Usage: python3 monitor_thread.py --url "https://voz.vn/t/..." --deep-scan
"""

import asyncio
import json
import argparse
from datetime import datetime
from pathlib import Path
from playwright.async_api import async_playwright

async def scrape_thread_deep(url, thread_name, deep_scan=False):
    """Deep scrape a thread with optional reply analysis"""
    async with async_playwright() as p:
        browser = await p.chromium.launch(
            headless=False,
            slow_mo=100,
            args=['--disable-blink-features=AutomationControlled']
        )
        
        context = await browser.new_context(
            user_agent='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36',
            viewport={'width': 1280, 'height': 720}
        )
        
        page = await context.new_page()
        
        print(f"🔍 Scraping: {thread_name}")
        print(f"   URL: {url}")
        
        try:
            await page.goto(url, timeout=60000)
            await page.wait_for_timeout(5000)
            
            # Get thread info
            title_elem = await page.query_selector('h1.p-title-value')
            title = await title_elem.inner_text() if title_elem else "Unknown"
            
            # Get OP (first post)
            posts = await page.query_selector_all('article.message--post')
            
            op_data = None
            replies_data = []
            
            if posts:
                # First post is OP
                op = posts[0]
                op_data = await extract_post_data(op, is_op=True)
                
                # Extract replies if deep scan
                if deep_scan and len(posts) > 1:
                    print(f"   📊 Analyzing {len(posts)-1} replies...")
                    for i, post in enumerate(posts[1:21], 1):  # Limit to 20 replies
                        try:
                            reply_data = await extract_post_data(post, is_op=False)
                            if reply_data:
                                replies_data.append(reply_data)
                                print(f"      ✓ Reply {i}: {reply_data.get('author', 'Unknown')}")
                        except Exception as e:
                            print(f"      ✗ Reply {i} error: {e}")
                            continue
            
            # Get pagination info
            page_nav = await page.query_selector('.pageNav')
            has_multiple_pages = bool(page_nav)
            
            await browser.close()
            
            return {
                'thread_title': title.strip(),
                'url': url,
                'scraped_at': datetime.now().isoformat(),
                'op': op_data,
                'replies_count': len(replies_data),
                'replies': replies_data if deep_scan else [],
                'has_multiple_pages': has_multiple_pages,
                'needs_follow_up': has_multiple_pages or len(replies_data) >= 20
            }
            
        except Exception as e:
            print(f"❌ Error: {e}")
            await browser.close()
            return None

async def extract_post_data(post_elem, is_op=False):
    """Extract data from a post element"""
    try:
        # Author
        author_elem = await post_elem.query_selector('.message-userDetails a.username')
        author = await author_elem.inner_text() if author_elem else "Unknown"
        
        # Content
        content_elem = await post_elem.query_selector('.message-body .bbWrapper')
        content = await content_elem.inner_text() if content_elem else ""
        
        # Date
        date_elem = await post_elem.query_selector('time')
        post_date = await date_elem.get_attribute('title') if date_elem else ""
        
        # User info
        user_title_elem = await post_elem.query_selector('.userTitle')
        user_title = await user_title_elem.inner_text() if user_title_elem else ""
        
        # Stats
        reactions_elem = await post_elem.query_selector('.reactionsBar')
        reactions = await reactions_elem.inner_text() if reactions_elem else ""
        
        # Check for job-related keywords
        job_keywords = ['tuyển', 'hiring', 'job', 'tìm việc', 'freelance', 'remote', 
                       'available', 'looking for', 'opportunity', 'experience', 'năm kinh nghiệm',
                       'skills', 'kỹ năng', 'tech stack', 'cv', 'portfolio']
        
        content_lower = content.lower()
        has_job_signals = any(kw in content_lower for kw in job_keywords)
        
        # Skill extraction (basic)
        skills_found = []
        skill_keywords = ['python', 'javascript', 'java', 'golang', 'react', 'vue', 'angular',
                         'docker', 'kubernetes', 'aws', 'azure', 'gcp', 'terraform', 'ansible',
                         'nodejs', 'django', 'flask', 'spring', 'sql', 'nosql', 'mongodb',
                         'postgresql', 'mysql', 'redis', 'kafka', 'elasticsearch', 'nginx']
        
        for skill in skill_keywords:
            if skill in content_lower:
                skills_found.append(skill)
        
        return {
            'is_op': is_op,
            'author': author.strip(),
            'post_date': post_date,
            'content_preview': content[:500] + "..." if len(content) > 500 else content,
            'content_full': content if is_op else "",
            'user_title': user_title.strip(),
            'reactions': reactions.strip(),
            'has_job_signals': has_job_signals,
            'skills_mentioned': skills_found,
            'word_count': len(content.split()),
            'potential_candidate': has_job_signals and len(content) > 200
        }
        
    except Exception as e:
        print(f"Error extracting post: {e}")
        return None

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Monitor and scrape Voz threads')
    parser.add_argument('--url', required=True, help='Thread URL')
    parser.add_argument('--name', help='Thread name for reference')
    parser.add_argument('--deep-scan', action='store_true', help='Scan replies for candidates')
    parser.add_argument('--output', default='/tmp/thread_monitor_result.json', help='Output file')
    
    args = parser.parse_args()
    
    result = asyncio.run(scrape_thread_deep(
        args.url, 
        args.name or "Unknown Thread",
        args.deep_scan
    ))
    
    if result:
        with open(args.output, 'w', encoding='utf-8') as f:
            json.dump(result, f, ensure_ascii=False, indent=2)
        
        print(f"\n✅ Results saved to: {args.output}")
        print(f"\n📊 Summary:")
        print(f"   Thread: {result['thread_title']}")
        print(f"   OP Author: {result['op']['author'] if result['op'] else 'N/A'}")
        print(f"   Replies analyzed: {result['replies_count']}")
        
        if result['replies']:
            potential = [r for r in result['replies'] if r.get('potential_candidate')]
            print(f"   Potential candidates in replies: {len(potential)}")
            
            if potential:
                print(f"\n🎯 Potential Candidates Found:")
                for p in potential[:5]:
                    print(f"   - {p['author']}: {p['user_title'] or 'No title'}")
                    print(f"     Skills: {', '.join(p['skills_mentioned']) or 'None detected'}")
                    print(f"     Signals: {'✓' if p['has_job_signals'] else '✗'}")
        
        if result['needs_follow_up']:
            print(f"\n⚠️  Thread has multiple pages or many replies - needs follow-up scraping")
