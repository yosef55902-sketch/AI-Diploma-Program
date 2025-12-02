"""
Unit 4: Interpretability, Transparency, and Accountability
Example 6: Transparency Tools

This example demonstrates transparency tools and frameworks for AI systems.
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

def compare_transparency_tools():
    tools = {
        'SHAP': {'interpretability': 9, 'ease_of_use': 8, 'model_agnostic': True, 'local_explanations': True},
        'LIME': {'interpretability': 8, 'ease_of_use': 9, 'model_agnostic': True, 'local_explanations': True},
        'Partial Dependence': {'interpretability': 7, 'ease_of_use': 7, 'model_agnostic': False, 'local_explanations': False},
        'Feature Importance': {'interpretability': 6, 'ease_of_use': 9, 'model_agnostic': False, 'local_explanations': False},
        'Counterfactuals': {'interpretability': 9, 'ease_of_use': 6, 'model_agnostic': True, 'local_explanations': True}
    }
    return tools

if __name__ == "__main__":
    print("="*80)
    print("Unit 4 - Example 6: Transparency Tools")
    print("="*80)
    
    tools = compare_transparency_tools()
    
    print("\nTransparency Tools Comparison:")
    for tool, metrics in tools.items():
        print(f"\n{tool}:")
        print(f"  Interpretability: {metrics['interpretability']}/10")
        print(f"  Ease of Use: {metrics['ease_of_use']}/10")
        print(f"  Model Agnostic: {metrics['model_agnostic']}")
        print(f"  Local Explanations: {metrics['local_explanations']}")
    
    tools_list = list(tools.keys())
    interpretability = [tools[t]['interpretability'] for t in tools_list]
    ease_of_use = [tools[t]['ease_of_use'] for t in tools_list]
    
    fig, axes = plt.subplots(1, 2, figsize=(16, 6))
    axes[0].bar(tools_list, interpretability, color='#3498db')
    axes[0].set_title('Interpretability Score', fontweight='bold')
    axes[0].set_ylabel('Score (1-10)')
    axes[0].tick_params(axis='x', rotation=15)
    axes[1].bar(tools_list, ease_of_use, color='#2ecc71')
    axes[1].set_title('Ease of Use Score', fontweight='bold')
    axes[1].set_ylabel('Score (1-10)')
    axes[1].tick_params(axis='x', rotation=15)
    plt.tight_layout()
    plt.savefig('unit4-transparency-accountability/examples/transparency_tools_comparison.png', dpi=300, bbox_inches='tight')
    print("\n✅ Saved: transparency_tools_comparison.png")
    plt.close()
    
    print("\n✅ Example completed!")

