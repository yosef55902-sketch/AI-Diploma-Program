"""
Unit 5: AI Governance, Regulations, and Future Challenges
Example 3: AI Governance Frameworks

This example demonstrates AI governance frameworks:
- Governance models
- Key components
- Implementation strategies
- Future trends
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
# GOVERNANCE FRAMEWORKS
# ============================================================================

def governance_frameworks():
    """
    Define different AI governance frameworks
    """
    frameworks = {
        'Ethics Board': {
            'type': 'Organizational',
            'scope': 'Internal',
            'components': [
                'Ethics review committee',
                'AI ethics guidelines',
                'Case review process',
                'Stakeholder representation'
            ],
            'effectiveness': 7,
            'implementation_cost': 5
        },
        'Regulatory Compliance': {
            'type': 'Legal',
            'scope': 'External',
            'components': [
                'Legal compliance team',
                'Regulatory monitoring',
                'Audit processes',
                'Documentation requirements'
            ],
            'effectiveness': 8,
            'implementation_cost': 7
        },
        'Technical Governance': {
            'type': 'Technical',
            'scope': 'Internal',
            'components': [
                'Model monitoring',
                'Bias detection systems',
                'Explainability tools',
                'Performance tracking'
            ],
            'effectiveness': 9,
            'implementation_cost': 8
        },
        'Multi-Stakeholder': {
            'type': 'Collaborative',
            'scope': 'Mixed',
            'components': [
                'Industry partnerships',
                'Academic collaboration',
                'Civil society engagement',
                'Government coordination'
            ],
            'effectiveness': 8,
            'implementation_cost': 6
        }
    }
    return frameworks

# ============================================================================
# GOVERNANCE COMPONENTS
# ============================================================================

def governance_components():
    """
    Define key components of AI governance
    """
    components = {
        'Policy Development': {
            'importance': 10,
            'complexity': 7,
            'stakeholders': ['Legal', 'Ethics', 'Management']
        },
        'Risk Assessment': {
            'importance': 9,
            'complexity': 8,
            'stakeholders': ['Technical', 'Legal', 'Business']
        },
        'Monitoring and Auditing': {
            'importance': 9,
            'complexity': 7,
            'stakeholders': ['Technical', 'Compliance', 'Quality']
        },
        'Training and Awareness': {
            'importance': 8,
            'complexity': 5,
            'stakeholders': ['HR', 'Training', 'All Employees']
        },
        'Incident Response': {
            'importance': 9,
            'complexity': 6,
            'stakeholders': ['Security', 'Legal', 'Management']
        }
    }
    return components

# ============================================================================
# VISUALIZATIONS
# ============================================================================

def plot_governance_frameworks(frameworks):
    """
    Plot governance frameworks comparison
    """
    fig, axes = plt.subplots(1, 2, figsize=(16, 6))
    
    framework_names = list(frameworks.keys())
    effectiveness = [f['effectiveness'] for f in frameworks.values()]
    cost = [f['implementation_cost'] for f in frameworks.values()]
    
    # Effectiveness vs Cost
    scatter = axes[0].scatter(cost, effectiveness, s=300, alpha=0.7,
                             c=effectiveness, cmap='RdYlGn', edgecolors='black', linewidth=2)
    for i, name in enumerate(framework_names):
        axes[0].annotate(name, (cost[i], effectiveness[i]),
                        xytext=(5, 5), textcoords='offset points', fontsize=9, fontweight='bold')
    axes[0].set_xlabel('Implementation Cost (1-10)', fontsize=11, fontweight='bold')
    axes[0].set_ylabel('Effectiveness (1-10)', fontsize=11, fontweight='bold')
    axes[0].set_title('Governance Framework: Effectiveness vs Cost', 
                     fontsize=12, fontweight='bold')
    axes[0].grid(alpha=0.3)
    axes[0].set_xlim([0, 11])
    axes[0].set_ylim([0, 11])
    plt.colorbar(scatter, ax=axes[0], label='Effectiveness')
    
    # Number of components
    num_components = [len(f['components']) for f in frameworks.values()]
    axes[1].bar(framework_names, num_components, color='#3498db', alpha=0.8)
    axes[1].set_title('Number of Framework Components', fontsize=12, fontweight='bold')
    axes[1].set_ylabel('Number of Components')
    axes[1].tick_params(axis='x', rotation=15)
    axes[1].grid(axis='y', alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('unit5-governance-regulations/examples/governance_frameworks.png', 
                dpi=300, bbox_inches='tight')
    print("✅ Saved: governance_frameworks.png")
    plt.close()

def plot_governance_components(components):
    """
    Plot governance components analysis
    """
    fig, axes = plt.subplots(1, 2, figsize=(16, 6))
    
    component_names = list(components.keys())
    importance = [c['importance'] for c in components.values()]
    complexity = [c['complexity'] for c in components.values()]
    
    # Importance
    axes[0].barh(component_names, importance, color='#2ecc71', alpha=0.8)
    axes[0].set_title('Component Importance (1-10)', fontsize=12, fontweight='bold')
    axes[0].set_xlabel('Importance Score')
    axes[0].grid(axis='x', alpha=0.3)
    axes[0].set_xlim([0, 11])
    
    # Complexity
    axes[1].barh(component_names, complexity, color='#f39c12', alpha=0.8)
    axes[1].set_title('Implementation Complexity (1-10)', fontsize=12, fontweight='bold')
    axes[1].set_xlabel('Complexity Score')
    axes[1].grid(axis='x', alpha=0.3)
    axes[1].set_xlim([0, 11])
    
    plt.tight_layout()
    plt.savefig('unit5-governance-regulations/examples/governance_components.png', 
                dpi=300, bbox_inches='tight')
    print("✅ Saved: governance_components.png")
    plt.close()

# ============================================================================
# MAIN EXECUTION
# ============================================================================

if __name__ == "__main__":
    print("="*80)
    print("Unit 5 - Example 3: AI Governance Frameworks")
    print("="*80)
    
    # Governance frameworks
    frameworks = governance_frameworks()
    print("\nAI Governance Frameworks:")
    for framework, info in frameworks.items():
        print(f"\n{framework} ({info['type']}):")
        print(f"  Scope: {info['scope']}")
        print(f"  Effectiveness: {info['effectiveness']}/10")
        print(f"  Implementation Cost: {info['implementation_cost']}/10")
        print(f"  Components:")
        for component in info['components']:
            print(f"    - {component}")
    
    # Governance components
    print("\n" + "="*80)
    print("Key Governance Components:")
    print("="*80)
    components = governance_components()
    for component, info in components.items():
        print(f"\n{component}:")
        print(f"  Importance: {info['importance']}/10")
        print(f"  Complexity: {info['complexity']}/10")
        print(f"  Key Stakeholders: {', '.join(info['stakeholders'])}")
    
    # Create visualizations
    print("\n" + "="*80)
    print("Creating Visualizations...")
    print("="*80)
    
    plot_governance_frameworks(frameworks)
    plot_governance_components(components)
    
    # Summary
    print("\n" + "="*80)
    print("SUMMARY")
    print("="*80)
    print("\nKey Takeaways:")
    print("1. Multiple governance frameworks can be combined")
    print("2. Technical governance is highly effective but costly")
    print("3. Ethics boards provide internal oversight")
    print("4. Regulatory compliance ensures legal adherence")
    print("5. Effective governance requires multiple components working together")
    print("="*80 + "\n")
