"""
Unit 5: AI Governance, Regulations, and Future Challenges
Example 1: Global AI Regulations

This example demonstrates global AI regulations:
- EU AI Act
- US Executive Orders and Initiatives
- China, Canada, OECD regulations
- Comparison of approaches
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

plt.rcParams['font.size'] = 10
plt.rcParams['figure.figsize'] = (14, 8)
sns.set_style("whitegrid")

# ============================================================================
# GLOBAL AI REGULATIONS
# ============================================================================

def global_ai_regulations():
    """
    Define global AI regulations and their key features
    """
    regulations = {
        'EU AI Act': {
            'region': 'European Union',
            'status': 'Enacted',
            'risk_based': True,
            'strictness': 9,
            'key_features': [
                'Risk-based classification (Unacceptable, High, Limited, Minimal)',
                'Prohibited AI practices',
                'Requirements for high-risk AI systems',
                'Transparency obligations',
                'Market surveillance'
            ],
            'enforcement': 'Strong',
            'penalties': 'Up to 7% of global revenue'
        },
        'US Executive Orders': {
            'region': 'United States',
            'status': 'Active',
            'risk_based': False,
            'strictness': 6,
            'key_features': [
                'AI Safety and Security Standards',
                'Privacy protections',
                'Equity and civil rights',
                'Consumer protections',
                'Worker support'
            ],
            'enforcement': 'Moderate',
            'penalties': 'Varies by agency'
        },
        'China AI Regulations': {
            'region': 'China',
            'status': 'Active',
            'risk_based': True,
            'strictness': 8,
            'key_features': [
                'Algorithmic recommendation rules',
                'Deep synthesis regulations',
                'Data security law',
                'Personal information protection law',
                'Content moderation requirements'
            ],
            'enforcement': 'Strong',
            'penalties': 'Fines and business restrictions'
        },
        'Canada AI Regulations': {
            'region': 'Canada',
            'status': 'Proposed',
            'risk_based': True,
            'strictness': 7,
            'key_features': [
                'AIDA (Artificial Intelligence and Data Act)',
                'High-impact AI system requirements',
                'Harm prevention',
                'Transparency and accountability',
                'Human oversight'
            ],
            'enforcement': 'Moderate',
            'penalties': 'Up to $25M or 5% of revenue'
        },
        'OECD AI Principles': {
            'region': 'International',
            'status': 'Adopted',
            'risk_based': False,
            'strictness': 5,
            'key_features': [
                'Inclusive growth and human-centered values',
                'Transparency and explainability',
                'Robustness and security',
                'Accountability',
                'International cooperation'
            ],
            'enforcement': 'Voluntary',
            'penalties': 'None (guidelines)'
        }
    }
    return regulations

# ============================================================================
# REGULATION COMPARISON
# ============================================================================

def compare_regulations(regulations):
    """
    Compare different regulatory approaches
    """
    comparison = pd.DataFrame({
        'Region': [r['region'] for r in regulations.values()],
        'Status': [r['status'] for r in regulations.values()],
        'Strictness': [r['strictness'] for r in regulations.values()],
        'Risk-Based': [r['risk_based'] for r in regulations.values()],
        'Enforcement': [r['enforcement'] for r in regulations.values()]
    })
    return comparison

# ============================================================================
# VISUALIZATIONS
# ============================================================================

def plot_regulation_comparison(regulations):
    """
    Plot comparison of global AI regulations
    """
    fig, axes = plt.subplots(2, 2, figsize=(16, 12))
    
    regions = list(regulations.keys())
    strictness = [r['strictness'] for r in regulations.values()]
    risk_based = [1 if r['risk_based'] else 0 for r in regulations.values()]
    
    # Strictness comparison
    colors = ['#e74c3c' if s >= 8 else '#f39c12' if s >= 6 else '#2ecc71' 
              for s in strictness]
    axes[0, 0].barh(regions, strictness, color=colors, alpha=0.8)
    axes[0, 0].set_title('Regulatory Strictness (1-10)', fontsize=12, fontweight='bold')
    axes[0, 0].set_xlabel('Strictness Score')
    axes[0, 0].grid(axis='x', alpha=0.3)
    axes[0, 0].set_xlim([0, 11])
    
    # Risk-based approach
    axes[0, 1].bar(regions, risk_based, color='#3498db', alpha=0.8)
    axes[0, 1].set_title('Risk-Based Approach (1=Yes, 0=No)', fontsize=12, fontweight='bold')
    axes[0, 1].set_ylabel('Risk-Based')
    axes[0, 1].tick_params(axis='x', rotation=15)
    axes[0, 1].grid(axis='y', alpha=0.3)
    axes[0, 1].set_ylim([0, 1.2])
    
    # Enforcement levels
    enforcement_map = {'Strong': 3, 'Moderate': 2, 'Voluntary': 1}
    enforcement_scores = [enforcement_map[r['enforcement']] for r in regulations.values()]
    axes[1, 0].barh(regions, enforcement_scores, color='#9b59b6', alpha=0.8)
    axes[1, 0].set_title('Enforcement Level', fontsize=12, fontweight='bold')
    axes[1, 0].set_xlabel('Enforcement (1=Voluntary, 2=Moderate, 3=Strong)')
    axes[1, 0].grid(axis='x', alpha=0.3)
    axes[1, 0].set_xlim([0, 4])
    
    # Status
    status_map = {'Enacted': 3, 'Active': 2, 'Proposed': 1, 'Adopted': 2}
    status_scores = [status_map.get(r['status'], 0) for r in regulations.values()]
    axes[1, 1].bar(regions, status_scores, color='#2ecc71', alpha=0.8)
    axes[1, 1].set_title('Regulatory Status', fontsize=12, fontweight='bold')
    axes[1, 1].set_ylabel('Status (1=Proposed, 2=Active/Adopted, 3=Enacted)')
    axes[1, 1].tick_params(axis='x', rotation=15)
    axes[1, 1].grid(axis='y', alpha=0.3)
    axes[1, 1].set_ylim([0, 4])
    
    plt.tight_layout()
    plt.savefig('unit5-governance-regulations/examples/global_regulations_comparison.png', 
                dpi=300, bbox_inches='tight')
    print("✅ Saved: global_regulations_comparison.png")
    plt.close()

def plot_regulatory_timeline(regulations):
    """
    Plot regulatory timeline
    """
    timeline_data = {
        'OECD AI Principles': 2019,
        'China AI Regulations': 2021,
        'EU AI Act': 2024,
        'US Executive Orders': 2023,
        'Canada AI Regulations': 2025  # Proposed
    }
    
    fig, ax = plt.subplots(figsize=(12, 8))
    
    regions = list(timeline_data.keys())
    years = list(timeline_data.values())
    
    colors = plt.cm.viridis(np.linspace(0, 1, len(regions)))
    
    for i, (region, year) in enumerate(timeline_data.items()):
        ax.scatter(year, i, s=300, c=[colors[i]], alpha=0.7, edgecolors='black', linewidth=2)
        ax.text(year, i, f'  {region}', va='center', fontsize=10, fontweight='bold')
    
    ax.set_xlabel('Year', fontsize=11, fontweight='bold')
    ax.set_yticks(range(len(regions)))
    ax.set_yticklabels([])
    ax.set_title('Global AI Regulations Timeline', fontsize=12, fontweight='bold')
    ax.grid(axis='x', alpha=0.3)
    ax.set_xlim([2018, 2026])
    
    plt.tight_layout()
    plt.savefig('unit5-governance-regulations/examples/regulatory_timeline.png', 
                dpi=300, bbox_inches='tight')
    print("✅ Saved: regulatory_timeline.png")
    plt.close()

# ============================================================================
# MAIN EXECUTION
# ============================================================================

if __name__ == "__main__":
    print("="*80)
    print("Unit 5 - Example 1: Global AI Regulations")
    print("="*80)
    
    # Global regulations
    regulations = global_ai_regulations()
    
    print("\nGlobal AI Regulations Overview:")
    for region, info in regulations.items():
        print(f"\n{region} ({info['region']}):")
        print(f"  Status: {info['status']}")
        print(f"  Strictness: {info['strictness']}/10")
        print(f"  Risk-Based: {info['risk_based']}")
        print(f"  Enforcement: {info['enforcement']}")
        print(f"  Key Features:")
        for feature in info['key_features'][:3]:
            print(f"    - {feature}")
    
    # Comparison
    print("\n" + "="*80)
    print("Regulation Comparison:")
    print("="*80)
    comparison = compare_regulations(regulations)
    print(comparison.to_string(index=False))
    
    # Create visualizations
    print("\n" + "="*80)
    print("Creating Visualizations...")
    print("="*80)
    
    plot_regulation_comparison(regulations)
    plot_regulatory_timeline(regulations)
    
    # Summary
    print("\n" + "="*80)
    print("SUMMARY")
    print("="*80)
    print("\nKey Takeaways:")
    print("1. Different regions have different regulatory approaches")
    print("2. EU AI Act is the most comprehensive risk-based framework")
    print("3. US focuses on executive orders and agency-specific rules")
    print("4. China has strict content and data regulations")
    print("5. International cooperation is needed for global AI governance")
    print("="*80 + "\n")
