#!/usr/bin/env python3
"""
Fix empty PROJECT_GUIDE.md files by recovering and merging content from git history
"""

import subprocess
import re
from pathlib import Path

def get_git_content(filepath, commit="HEAD~1"):
    """Get file content from git history"""
    try:
        result = subprocess.run(
            ['git', 'show', f'{commit}:{filepath}'],
            capture_output=True,
            text=True,
            check=True
        )
        return result.stdout
    except subprocess.CalledProcessError:
        return None

def create_proper_guide(project_dir):
    """Create proper merged PROJECT_GUIDE.md"""
    project_dir = Path(project_dir)
    project_name = project_dir.name.replace('_', ' ').title()
    
    # Get content from git
    beginner_guide = get_git_content(str(project_dir / 'BEGINNER_GUIDE.md'))
    impl_guide = get_git_content(str(project_dir / 'Implementation_Guide.md'))
    
    if not beginner_guide and not impl_guide:
        print(f"  ⚠️  No guides found in git for {project_dir}")
        return False
    
    # Extract real-world application from beginner guide
    real_world = ""
    if beginner_guide:
        match = re.search(r'## 🎯 Real-World Application.*?(?=##|\Z)', beginner_guide, re.DOTALL)
        if match:
            real_world = match.group(0).strip()
    
    # Extract quick start from implementation guide
    quick_start = ""
    if impl_guide:
        # Get the step-by-step implementation section
        match = re.search(r'## Step-by-Step Implementation.*?(?=##|\Z)', impl_guide, re.DOTALL)
        if match:
            quick_start = match.group(0).strip()
    
    # Extract tutorial from beginner guide
    tutorial = ""
    if beginner_guide:
        match = re.search(r'## 📚 Step-by-Step Guide.*?(?=## 🎓|\Z)', beginner_guide, re.DOTALL)
        if match:
            tutorial = match.group(0).strip()
    
    # Extract troubleshooting
    troubleshooting = ""
    if beginner_guide:
        match = re.search(r'## 🔧 Troubleshooting.*?(?=##|\Z)', beginner_guide, re.DOTALL)
        if match:
            troubleshooting = match.group(0).strip()
    elif impl_guide:
        match = re.search(r'## Troubleshooting.*?(?=##|\Z)', impl_guide, re.DOTALL)
        if match:
            troubleshooting = match.group(0).strip()
    
    # Build merged guide
    merged = []
    merged.append(f"# Complete Project Guide: {project_name}")
    merged.append("## دليل المشروع الكامل")
    merged.append("")
    merged.append("---")
    merged.append("")
    
    # Real-world application
    if real_world:
        merged.append(real_world)
        merged.append("")
        merged.append("---")
        merged.append("")
    
    # Quick Start
    merged.append("## 🚀 Quick Start (For Experienced Students)")
    merged.append("## البدء السريع (للطلاب ذوي الخبرة)")
    merged.append("")
    merged.append("> 💡 **New to this project?** Skip to [Complete Tutorial](#-complete-tutorial-for-beginners) section below.")
    merged.append("")
    if quick_start:
        # Remove the header and add content
        quick_content = re.sub(r'^## Step-by-Step Implementation.*?\n', '', quick_start, flags=re.MULTILINE)
        merged.append(quick_content.strip())
    else:
        merged.append("See Complete Tutorial section below for detailed instructions.")
    merged.append("")
    merged.append("---")
    merged.append("")
    
    # Complete Tutorial
    merged.append("## 📚 Complete Tutorial (For Beginners)")
    merged.append("## دليل كامل للمبتدئين")
    merged.append("")
    merged.append("> 💡 **Already familiar with this?** See [Quick Start](#-quick-start-for-experienced-students) section above.")
    merged.append("")
    if tutorial:
        # Remove the header
        tutorial_content = re.sub(r'^## 📚 Step-by-Step Guide.*?\n', '', tutorial, flags=re.MULTILINE)
        merged.append(tutorial_content.strip())
    else:
        merged.append("See Quick Start section above for technical details.")
    merged.append("")
    merged.append("---")
    merged.append("")
    
    # Course connections (if mentioned in beginner guide)
    if beginner_guide and 'Course Connection' in beginner_guide:
        merged.append("## 🔗 Course Content Connections")
        merged.append("## روابط محتوى الدورة")
        merged.append("")
        merged.append("Each step in this project connects to specific course notebooks. See the tutorial section above for detailed connections marked with 📖 Course Connection.")
        merged.append("")
        merged.append("---")
        merged.append("")
    
    # Troubleshooting
    if troubleshooting:
        merged.append(troubleshooting)
        merged.append("")
        merged.append("---")
        merged.append("")
    
    # Write merged guide
    output_file = project_dir / 'PROJECT_GUIDE.md'
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write('\n'.join(merged))
    
    return True

def main():
    root = Path('.')
    project_dirs = [d for d in root.rglob('*/PROJECTS/*') if d.is_dir() and 'Template' not in str(d)]
    
    print("Fixing empty PROJECT_GUIDE.md files...\n")
    
    fixed = 0
    for project_dir in sorted(project_dirs):
        guide_file = project_dir / 'PROJECT_GUIDE.md'
        if not guide_file.exists():
            continue
        
        # Check if empty (less than 100 lines)
        with open(guide_file, 'r', encoding='utf-8') as f:
            lines = len(f.readlines())
        
        if lines < 100:
            print(f"Fixing: {project_dir.relative_to(root)}")
            if create_proper_guide(project_dir):
                fixed += 1
                print(f"  ✅ Fixed ({lines} -> {len(open(guide_file).readlines())} lines)")
            else:
                print(f"  ❌ Failed")
    
    print(f"\n✅ Fixed {fixed} guides")

if __name__ == '__main__':
    main()

