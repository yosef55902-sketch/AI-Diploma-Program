"""
Unit 5: AI Governance, Regulations, and Future Challenges
Example 2: Industry-Specific AI Regulations

This example demonstrates industry-specific AI regulations:
- Healthcare AI regulations
- Finance AI regulations
- Autonomous Vehicles regulations
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
# INDUSTRY-SPECIFIC REGULATIONS
# ============================================================================

def industry_regulations():
    """
    Define industry-specific AI regulations
    """
    regulations = {
        'Healthcare': {
            'regulatory_bodies': ['FDA (US)', 'EMA (EU)', 'Health Canada'],
            'key_requirements': [
                'Clinical validation',
                'Safety and efficacy proof',
                'Transparency in decision-making',
                'Human oversight',
                'Data privacy (HIPAA compliance)'
            ],
            'risk_level': 'Very High',
            'compliance_complexity': 9,
            'examples': ['Medical diagnosis AI', 'Drug discovery', 'Treatment recommendations']
        },
        'Finance': {
            'regulatory_bodies': ['SEC (US)', 'FCA (UK)', 'ESMA (EU)'],
            'key_requirements': [
                'Fair lending practices',
                'Anti-discrimination compliance',
                'Explainability for credit decisions',
                'Risk management',
                'Audit trails'
            ],
            'risk_level': 'High',
            'compliance_complexity': 8,
            'examples': ['Credit scoring', 'Fraud detection', 'Algorithmic trading']
        },
        'Autonomous Vehicles': {
            'regulatory_bodies': ['NHTSA (US)', 'ECE (EU)', 'Transport Canada'],
            'key_requirements': [
                'Safety standards',
                'Testing and validation',
                'Liability frameworks',
                'Data recording',
                'Cybersecurity'
            ],
            'risk_level': 'Very High',
            'compliance_complexity': 9,
            'examples': ['Self-driving cars', 'Autonomous trucks', 'Delivery robots']
        }
    }
    return regulations

# ============================================================================
# VISUALIZATIONS
# ============================================================================

def plot_industry_regulations(regulations):
    """
    Plot industry-specific regulations comparison
    """
    fig, axes = plt.subplots(2, 2, figsize=(16, 12))
    
    industries = list(regulations.keys())
    risk_map = {'Very High': 4, 'High': 3, 'Medium': 2, 'Low': 1}
    risk_scores = [risk_map[r['risk_level']] for r in regulations.values()]
    complexity = [r['compliance_complexity'] for r in regulations.values()]
    
    # Risk levels
    axes[0, 0].barh(industries, risk_scores, color='#e74c3c', alpha=0.8)
    axes[0, 0].set_title('Risk Level by Industry', fontsize=12, fontweight='bold')
    axes[0, 0].set_xlabel('Risk Level (1=Low, 4=Very High)')
    axes[0, 0].grid(axis='x', alpha=0.3)
    axes[0, 0].set_xlim([0, 5])
    
    # Compliance complexity
    axes[0, 1].bar(industries, complexity, color='#3498db', alpha=0.8)
    axes[0, 1].set_title('Compliance Complexity (1-10)', fontsize=12, fontweight='bold')
    axes[0, 1].set_ylabel('Complexity Score')
    axes[0, 1].tick_params(axis='x', rotation=15)
    axes[0, 1].grid(axis='y', alpha=0.3)
    axes[0, 1].set_ylim([0, 11])
    
    # Number of requirements
    num_requirements = [len(r['key_requirements']) for r in regulations.values()]
    axes[1, 0].bar(industries, num_requirements, color='#2ecc71', alpha=0.8)
    axes[1, 0].set_title('Number of Key Requirements', fontsize=12, fontweight='bold')
    axes[1, 0].set_ylabel('Number of Requirements')
    axes[1, 0].tick_params(axis='x', rotation=15)
    axes[1, 0].grid(axis='y', alpha=0.3)
    
    # Risk vs Complexity
    scatter = axes[1, 1].scatter(risk_scores, complexity, s=300, alpha=0.7,
                               c=complexity, cmap='RdYlGn_r', edgecolors='black', linewidth=2)
    for i, industry in enumerate(industries):
        axes[1, 1].annotate(industry, (risk_scores[i], complexity[i]),
                           xytext=(5, 5), textcoords='offset points', fontsize=10, fontweight='bold')
    axes[1, 1].set_xlabel('Risk Level', fontsize=11, fontweight='bold')
    axes[1, 1].set_ylabel('Compliance Complexity', fontsize=11, fontweight='bold')
    axes[1, 1].set_title('Risk vs Compliance Complexity', fontsize=12, fontweight='bold')
    axes[1, 1].grid(alpha=0.3)
    plt.colorbar(scatter, ax=axes[1, 1], label='Complexity')
    
    plt.tight_layout()
    plt.savefig('unit5-governance-regulations/examples/industry_regulations.png', 
                dpi=300, bbox_inches='tight')
    print("✅ Saved: industry_regulations.png")
    plt.close()

# ============================================================================
# MAIN EXECUTION
# ============================================================================

if __name__ == "__main__":
    print("="*80)
    print("Unit 5 - Example 2: Industry-Specific AI Regulations")
    print("="*80)
    
    regulations = industry_regulations()
    
    for industry, info in regulations.items():
        print(f"\n{industry} AI Regulations:")
        print(f"  Regulatory Bodies: {', '.join(info['regulatory_bodies'])}")
        print(f"  Risk Level: {info['risk_level']}")
        print(f"  Compliance Complexity: {info['compliance_complexity']}/10")
        print(f"  Key Requirements:")
        for req in info['key_requirements']:
            print(f"    - {req}")
        print(f"  Examples: {', '.join(info['examples'])}")
    
    # Create visualizations
    print("\n" + "="*80)
    print("Creating Visualizations...")
    print("="*80)
    
    plot_industry_regulations(regulations)
    
    # Summary
    print("\n" + "="*80)
    print("SUMMARY")
    print("="*80)
    print("\nKey Takeaways:")
    print("1. Different industries have specific regulatory requirements")
    print("2. Healthcare and autonomous vehicles have highest risk levels")
    print("3. Finance requires strong explainability and fairness")
    print("4. Compliance complexity varies by industry")
    print("5. Industry-specific regulations complement general AI regulations")
    print("="*80 + "\n")
