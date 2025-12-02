"""
Unit 3: Privacy, Security, and Data Protection
Example 4: GDPR Compliance

This example demonstrates GDPR compliance requirements:
- Key GDPR principles
- Data subject rights
- Compliance checklist
- Privacy by design
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime, timedelta
import warnings
warnings.filterwarnings('ignore')

plt.rcParams['font.size'] = 10
plt.rcParams['figure.figsize'] = (14, 8)
sns.set_style("whitegrid")

# ============================================================================
# GDPR PRINCIPLES
# ============================================================================

def gdpr_principles():
    """
    Define key GDPR principles
    """
    principles = {
        'Lawfulness, Fairness, Transparency': {
            'description': 'Process data lawfully, fairly, and transparently',
            'importance': 10,
            'compliance_level': 0.85
        },
        'Purpose Limitation': {
            'description': 'Collect data for specified, explicit, legitimate purposes',
            'importance': 9,
            'compliance_level': 0.80
        },
        'Data Minimization': {
            'description': 'Collect only data that is necessary',
            'importance': 9,
            'compliance_level': 0.75
        },
        'Accuracy': {
            'description': 'Keep data accurate and up-to-date',
            'importance': 8,
            'compliance_level': 0.90
        },
        'Storage Limitation': {
            'description': 'Retain data only as long as necessary',
            'importance': 8,
            'compliance_level': 0.70
        },
        'Integrity and Confidentiality': {
            'description': 'Ensure appropriate security of personal data',
            'importance': 10,
            'compliance_level': 0.85
        },
        'Accountability': {
            'description': 'Demonstrate compliance with GDPR principles',
            'importance': 9,
            'compliance_level': 0.75
        }
    }
    return principles

# ============================================================================
# DATA SUBJECT RIGHTS
# ============================================================================

def data_subject_rights():
    """
    Define data subject rights under GDPR
    """
    rights = {
        'Right to Access': {
            'description': 'Access personal data held by organization',
            'response_time_days': 30,
            'complexity': 'Medium'
        },
        'Right to Rectification': {
            'description': 'Correct inaccurate personal data',
            'response_time_days': 30,
            'complexity': 'Low'
        },
        'Right to Erasure': {
            'description': 'Request deletion of personal data',
            'response_time_days': 30,
            'complexity': 'High'
        },
        'Right to Restrict Processing': {
            'description': 'Limit how data is processed',
            'response_time_days': 30,
            'complexity': 'Medium'
        },
        'Right to Data Portability': {
            'description': 'Receive data in machine-readable format',
            'response_time_days': 30,
            'complexity': 'Medium'
        },
        'Right to Object': {
            'description': 'Object to processing of personal data',
            'response_time_days': 30,
            'complexity': 'Low'
        }
    }
    return rights

# ============================================================================
# GDPR COMPLIANCE CHECKLIST
# ============================================================================

def gdpr_compliance_checklist():
    """
    Create GDPR compliance checklist
    """
    checklist = {
        'Data Inventory': {
            'status': 'Complete',
            'items': [
                'Document all personal data collected',
                'Identify data sources and purposes',
                'Map data flows',
                'Identify data processors'
            ]
        },
        'Legal Basis': {
            'status': 'Complete',
            'items': [
                'Identify legal basis for processing',
                'Document consent mechanisms',
                'Review legitimate interests',
                'Update privacy notices'
            ]
        },
        'Data Protection': {
            'status': 'In Progress',
            'items': [
                'Implement encryption',
                'Access controls',
                'Data anonymization',
                'Security monitoring'
            ]
        },
        'Data Subject Rights': {
            'status': 'In Progress',
            'items': [
                'Request handling procedures',
                'Response time tracking',
                'Data export functionality',
                'Deletion procedures'
            ]
        },
        'Privacy by Design': {
            'status': 'In Progress',
            'items': [
                'Privacy impact assessments',
                'Default privacy settings',
                'Minimal data collection',
                'Data retention policies'
            ]
        }
    }
    return checklist

# ============================================================================
# VISUALIZATIONS
# ============================================================================

def plot_gdpr_principles(principles):
    """
    Plot GDPR principles importance and compliance
    """
    fig, axes = plt.subplots(1, 2, figsize=(16, 6))
    
    principle_names = list(principles.keys())
    importance = [p['importance'] for p in principles.values()]
    compliance = [p['compliance_level'] * 10 for p in principles.values()]
    
    y_pos = np.arange(len(principle_names))
    
    axes[0].barh(y_pos, importance, color='#3498db', alpha=0.8)
    axes[0].set_yticks(y_pos)
    axes[0].set_yticklabels(principle_names, fontsize=9)
    axes[0].set_xlabel('Importance (1-10)', fontsize=11, fontweight='bold')
    axes[0].set_title('GDPR Principles Importance', fontsize=12, fontweight='bold')
    axes[0].grid(axis='x', alpha=0.3)
    axes[0].set_xlim([0, 11])
    
    axes[1].barh(y_pos, compliance, color='#2ecc71', alpha=0.8)
    axes[1].set_yticks(y_pos)
    axes[1].set_yticklabels(principle_names, fontsize=9)
    axes[1].set_xlabel('Compliance Level (1-10)', fontsize=11, fontweight='bold')
    axes[1].set_title('Current Compliance Level', fontsize=12, fontweight='bold')
    axes[1].grid(axis='x', alpha=0.3)
    axes[1].set_xlim([0, 11])
    
    plt.tight_layout()
    plt.savefig('unit3-privacy-security/examples/gdpr_principles.png', 
                dpi=300, bbox_inches='tight')
    print("✅ Saved: gdpr_principles.png")
    plt.close()

def plot_data_subject_rights(rights):
    """
    Plot data subject rights analysis
    """
    fig, axes = plt.subplots(1, 2, figsize=(16, 6))
    
    right_names = list(rights.keys())
    response_times = [r['response_time_days'] for r in rights.values()]
    complexities = {'Low': 1, 'Medium': 2, 'High': 3}
    complexity_scores = [complexities[r['complexity']] for r in rights.values()]
    
    axes[0].bar(right_names, response_times, color='#f39c12', alpha=0.8)
    axes[0].set_title('Response Time Requirements', fontsize=12, fontweight='bold')
    axes[0].set_ylabel('Days')
    axes[0].tick_params(axis='x', rotation=15)
    axes[0].axhline(y=30, color='red', linestyle='--', linewidth=2, label='GDPR Limit (30 days)')
    axes[0].legend()
    axes[0].grid(axis='y', alpha=0.3)
    
    axes[1].bar(right_names, complexity_scores, color='#e74c3c', alpha=0.8)
    axes[1].set_title('Implementation Complexity', fontsize=12, fontweight='bold')
    axes[1].set_ylabel('Complexity (1=Low, 2=Medium, 3=High)')
    axes[1].tick_params(axis='x', rotation=15)
    axes[1].grid(axis='y', alpha=0.3)
    axes[1].set_ylim([0, 4])
    
    plt.tight_layout()
    plt.savefig('unit3-privacy-security/examples/data_subject_rights.png', 
                dpi=300, bbox_inches='tight')
    print("✅ Saved: data_subject_rights.png")
    plt.close()

def plot_compliance_checklist(checklist):
    """
    Plot GDPR compliance checklist status
    """
    categories = list(checklist.keys())
    status_counts = {'Complete': 0, 'In Progress': 0, 'Not Started': 0}
    
    for cat, info in checklist.items():
        if info['status'] in status_counts:
            status_counts[info['status']] += 1
    
    fig, ax = plt.subplots(figsize=(10, 6))
    
    colors = {'Complete': '#2ecc71', 'In Progress': '#f39c12', 'Not Started': '#e74c3c'}
    bars = ax.bar(status_counts.keys(), status_counts.values(), 
                 color=[colors[s] for s in status_counts.keys()], alpha=0.8)
    
    for bar, count in zip(bars, status_counts.values()):
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height,
               f'{int(count)}',
               ha='center', va='bottom', fontsize=11, fontweight='bold')
    
    ax.set_ylabel('Number of Categories', fontsize=11, fontweight='bold')
    ax.set_title('GDPR Compliance Checklist Status', fontsize=12, fontweight='bold')
    ax.grid(axis='y', alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('unit3-privacy-security/examples/gdpr_compliance_status.png', 
                dpi=300, bbox_inches='tight')
    print("✅ Saved: gdpr_compliance_status.png")
    plt.close()

# ============================================================================
# MAIN EXECUTION
# ============================================================================

if __name__ == "__main__":
    print("="*80)
    print("Unit 3 - Example 4: GDPR Compliance")
    print("="*80)
    
    # GDPR Principles
    print("\n1. GDPR Principles:")
    principles = gdpr_principles()
    for principle, info in principles.items():
        print(f"\n{principle}:")
        print(f"  Description: {info['description']}")
        print(f"  Importance: {info['importance']}/10")
        print(f"  Compliance Level: {info['compliance_level']*100:.0f}%")
    
    # Data Subject Rights
    print("\n" + "="*80)
    print("2. Data Subject Rights:")
    print("="*80)
    rights = data_subject_rights()
    for right, info in rights.items():
        print(f"\n{right}:")
        print(f"  Description: {info['description']}")
        print(f"  Response Time: {info['response_time_days']} days")
        print(f"  Complexity: {info['complexity']}")
    
    # Compliance Checklist
    print("\n" + "="*80)
    print("3. GDPR Compliance Checklist:")
    print("="*80)
    checklist = gdpr_compliance_checklist()
    for category, info in checklist.items():
        print(f"\n{category} ({info['status']}):")
        for item in info['items']:
            print(f"  - {item}")
    
    # Create visualizations
    print("\n" + "="*80)
    print("Creating Visualizations...")
    print("="*80)
    
    plot_gdpr_principles(principles)
    plot_data_subject_rights(rights)
    plot_compliance_checklist(checklist)
    
    # Summary
    print("\n" + "="*80)
    print("SUMMARY")
    print("="*80)
    print("\nKey Takeaways:")
    print("1. GDPR has 7 key principles for data processing")
    print("2. Data subjects have 6 fundamental rights")
    print("3. Organizations must respond to requests within 30 days")
    print("4. Privacy by design is a core requirement")
    print("5. Compliance requires ongoing monitoring and documentation")
    print("="*80 + "\n")
