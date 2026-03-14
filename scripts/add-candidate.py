#!/usr/bin/env python3
"""
Script thêm ứng viên mới vào database
Usage: python3 add-candidate.py --role ai --name "Nguyen Van A" --source "voz-url"
"""

import argparse
import os
import re
import json
from datetime import datetime
from pathlib import Path

def slugify(text):
    """Convert text to slug"""
    text = re.sub(r'[^\w\s-]', '', text.lower())
    text = re.sub(r'[-\s]+', '-', text)
    return text

def get_next_id(role):
    """Generate next candidate ID based on role"""
    role_prefixes = {
        'ai': 'VAI',
        'backend-devops': 'VBD',
        'qa': 'VQA'
    }
    prefix = role_prefixes.get(role, 'VXX')
    
    # Count existing files
    role_path = Path(f'data/{role}')
    if not role_path.exists():
        return f"{prefix}-001"
    
    existing = list(role_path.glob('*.md'))
    existing = [f for f in existing if f.name != 'README.md']
    next_num = len(existing) + 1
    
    return f"{prefix}-{next_num:03d}"

def create_candidate_file(args):
    """Create a new candidate markdown file"""
    
    candidate_id = get_next_id(args.role)
    slug = slugify(args.name)
    filename = f"{candidate_id}-{slug}.md"
    
    role_path = Path(f'data/{args.role}')
    role_path.mkdir(parents=True, exist_ok=True)
    
    filepath = role_path / filename
    
    template = f"""---
id: {candidate_id}
name: {args.name}
role: {args.role}
source: {args.source}
post_date: {datetime.now().strftime('%Y-%m-%d')}
contacted_date:
status: new
skills:
  - 
experience: ""
location: ""
salary_expectation: ""
contact_info:
  telegram: 
  email: 
notes: ""
---

# {args.name}

## Thông tin từ post

<!-- Copy nội dung post gốc từ Voz -->

## Đánh giá

- Technical: ⭐⭐⭐⭐⭐
- Communication: ⭐⭐⭐⭐⭐
- Fit: ⭐⭐⭐⭐⭐

## Timeline liên hệ

- {datetime.now().strftime('%Y-%m-%d')}: Phát hiện post

"""
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(template)
    
    print(f"✅ Created: {filepath}")
    print(f"📝 ID: {candidate_id}")
    print(f"👤 Name: {args.name}")
    print(f"🔖 Role: {args.role}")
    
    return candidate_id

def update_role_readme(role):
    """Update the role README with new candidate"""
    # This would parse all files and regenerate the table
    # For now, just remind user to do it manually or run another script
    pass

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Add new candidate to tracker')
    parser.add_argument('--role', required=True, 
                       choices=['ai', 'backend-devops', 'qa'],
                       help='Candidate role category')
    parser.add_argument('--name', required=True,
                       help='Candidate full name')
    parser.add_argument('--source', required=True,
                       help='Voz thread URL')
    parser.add_argument('--skills', nargs='+',
                       help='List of skills (optional)')
    
    args = parser.parse_args()
    
    create_candidate_file(args)
    print("\n💡 Remember to:")
    print("1. Edit the file to add details from the Voz post")
    print("2. Update skills and contact info")
    print("3. Run: python3 scripts/update-stats.py")
