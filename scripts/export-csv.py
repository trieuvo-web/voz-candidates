#!/usr/bin/env python3
"""
Export candidates to CSV
Usage: python3 export-csv.py --output candidates.csv
"""

import csv
import yaml
import argparse
from pathlib import Path

def parse_frontmatter(content):
    """Parse YAML frontmatter from markdown file"""
    if content.startswith('---'):
        parts = content.split('---', 2)
        if len(parts) >= 3:
            try:
                return yaml.safe_load(parts[1])
            except:
                return None
    return None

def export_to_csv(output_file):
    """Export all candidates to CSV"""
    candidates = []
    
    search_paths = [Path('data/ai'), Path('data/backend-devops'), Path('data/qa')]
    
    for search_path in search_paths:
        if not search_path.exists():
            continue
            
        for md_file in search_path.glob('*.md'):
            if md_file.name == 'README.md':
                continue
                
            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            metadata = parse_frontmatter(content)
            if metadata:
                candidates.append({
                    'ID': metadata.get('id', ''),
                    'Name': metadata.get('name', ''),
                    'Role': metadata.get('role', ''),
                    'Status': metadata.get('status', ''),
                    'Skills': ', '.join(metadata.get('skills', [])),
                    'Experience': metadata.get('experience', ''),
                    'Location': metadata.get('location', ''),
                    'Salary': metadata.get('salary_expectation', ''),
                    'Source': metadata.get('source', ''),
                    'Post Date': metadata.get('post_date', ''),
                    'Contacted Date': metadata.get('contacted_date', ''),
                    'Notes': metadata.get('notes', '')
                })
    
    if not candidates:
        print("❌ No candidates found to export")
        return
    
    # Write CSV
    with open(output_file, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=candidates[0].keys())
        writer.writeheader()
        writer.writerows(candidates)
    
    print(f"✅ Exported {len(candidates)} candidates to {output_file}")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Export candidates to CSV')
    parser.add_argument('--output', default='candidates.csv',
                       help='Output CSV file path')
    
    args = parser.parse_args()
    export_to_csv(args.output)
