#!/usr/bin/env python3
"""
Script tìm kiếm ứng viên trong database
Usage: 
  python3 search-candidates.py --skill python
  python3 search-candidates.py --role ai
  python3 search-candidates.py --status new
  python3 search-candidates.py --all
"""

import argparse
import re
import yaml
from pathlib import Path
from datetime import datetime

def parse_frontmatter(content):
    """Parse YAML frontmatter from markdown file"""
    if content.startswith('---'):
        parts = content.split('---', 2)
        if len(parts) >= 3:
            try:
                return yaml.safe_load(parts[1]), parts[2]
            except:
                return None, content
    return None, content

def search_candidates(role=None, skill=None, status=None, name=None):
    """Search candidates based on criteria"""
    results = []
    
    # Determine which directories to search
    if role:
        search_paths = [Path(f'data/{role}')]
    else:
        search_paths = [Path('data/ai'), Path('data/backend-devops'), Path('data/qa')]
    
    for search_path in search_paths:
        if not search_path.exists():
            continue
            
        for md_file in search_path.glob('*.md'):
            if md_file.name == 'README.md':
                continue
                
            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            metadata, body = parse_frontmatter(content)
            if not metadata:
                continue
            
            # Apply filters
            match = True
            
            if skill:
                skills = metadata.get('skills', [])
                if not any(skill.lower() in s.lower() for s in skills):
                    match = False
            
            if status and metadata.get('status') != status:
                match = False
            
            if name and name.lower() not in metadata.get('name', '').lower():
                match = False
            
            if match:
                results.append({
                    'file': str(md_file),
                    'metadata': metadata
                })
    
    return results

def format_output(results):
    """Format search results for display"""
    if not results:
        print("❌ No candidates found matching criteria")
        return
    
    print(f"\n🔍 Found {len(results)} candidate(s):\n")
    print("-" * 80)
    
    for r in results:
        m = r['metadata']
        print(f"🆔 ID: {m.get('id', 'N/A')}")
        print(f"👤 Name: {m.get('name', 'N/A')}")
        print(f"🔖 Role: {m.get('role', 'N/A')}")
        print(f"📊 Status: {m.get('status', 'N/A')}")
        print(f"🛠️  Skills: {', '.join(m.get('skills', [])) or 'N/A'}")
        print(f"📍 Location: {m.get('location', 'N/A')}")
        print(f"💰 Salary: {m.get('salary_expectation', 'N/A')}")
        print(f"🔗 Source: {m.get('source', 'N/A')}")
        print(f"📁 File: {r['file']}")
        print("-" * 80)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Search candidates in database')
    parser.add_argument('--role', choices=['ai', 'backend-devops', 'qa'],
                       help='Filter by role')
    parser.add_argument('--skill', help='Filter by skill (case insensitive)')
    parser.add_argument('--status', 
                       choices=['new', 'contacted', 'responded', 'interested', 
                               'interviewing', 'hired', 'rejected', 'no-response'],
                       help='Filter by status')
    parser.add_argument('--name', help='Search by name (partial match)')
    parser.add_argument('--all', action='store_true',
                       help='Show all candidates')
    
    args = parser.parse_args()
    
    if args.all:
        results = search_candidates()
    else:
        results = search_candidates(
            role=args.role,
            skill=args.skill,
            status=args.status,
            name=args.name
        )
    
    format_output(results)
