"""
Unit 5: AI Governance, Regulations, and Future Challenges
Example 4: Legal Challenges in AI Governance

This example demonstrates legal challenges in AI governance:
- AI and Legal Liability
- Ethical AI vs. Business Profits
- Regulatory Approaches by Region
- Global vs. Local AI Laws
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

def legal_challenges():
    challenges = {
        'Liability Attribution': {'complexity': 9, 'urgency': 8, 'stakeholders': ['Legal', 'Business', 'Insurance']},
        'Ethical vs. Profit': {'complexity': 8, 'urgency': 9, 'stakeholders': ['Business', 'Ethics', 'Compliance']},
        'Regulatory Conflicts': {'complexity': 7, 'urgency': 7, 'stakeholders': ['Legal', 'Compliance', 'International']},
        'Data Ownership': {'complexity': 8, 'urgency': 8, 'stakeholders': ['Legal', 'Data', 'Privacy']},
        'Cross-Border Issues': {'complexity': 9, 'urgency': 7, 'stakeholders': ['Legal', 'International', 'Compliance']}
    }
    return challenges

if __name__ == "__main__":
    print("="*80)
    print("Unit 5 - Example 4: Legal Challenges in AI Governance")
    print("="*80)
    
    challenges = legal_challenges()
    for challenge, info in challenges.items():
        print(f"\n{challenge}:")
        print(f"  Complexity: {info['complexity']}/10")
        print(f"  Urgency: {info['urgency']}/10")
        print(f"  Stakeholders: {', '.join(info['stakeholders'])}")
    
    # Visualization
    fig, ax = plt.subplots(figsize=(12, 6))
    challenge_names = list(challenges.keys())
    complexity = [c['complexity'] for c in challenges.values()]
    urgency = [c['urgency'] for c in challenges.values()]
    
    x = np.arange(len(challenge_names))
    width = 0.35
    ax.bar(x - width/2, complexity, width, label='Complexity', alpha=0.8, color='#e74c3c')
    ax.bar(x + width/2, urgency, width, label='Urgency', alpha=0.8, color='#3498db')
    ax.set_xlabel('Legal Challenge', fontweight='bold')
    ax.set_ylabel('Score (1-10)', fontweight='bold')
    ax.set_title('Legal Challenges: Complexity vs Urgency', fontweight='bold')
    ax.set_xticks(x)
    ax.set_xticklabels(challenge_names, rotation=15)
    ax.legend()
    ax.grid(axis='y', alpha=0.3)
    plt.tight_layout()
    plt.savefig('unit5-governance-regulations/examples/legal_challenges.png', dpi=300, bbox_inches='tight')
    print("\n✅ Saved: legal_challenges.png")
    plt.close()
    
    print("\n✅ Example completed!")
