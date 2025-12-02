"""
Unit 3: Privacy, Security, and Data Protection
Example 2: Privacy-Enhancing Technologies (PETs)

This example demonstrates privacy-enhancing technologies:
- Secure Multi-Party Computation (SMPC) concepts
- Homomorphic encryption concepts
- Privacy-utility trade-offs
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
# SECURE MULTI-PARTY COMPUTATION (SMPC) SIMULATION
# ============================================================================

def smpc_sum_simulation(parties_data, n_parties=3):
    """
    Simulate Secure Multi-Party Computation for computing sum
    without revealing individual values
    """
    # Each party adds random noise to their data
    noise = [np.random.normal(0, 100) for _ in range(n_parties)]
    noisy_data = [data + noise[i] for i, data in enumerate(parties_data)]
    
    # Sum of noisy data
    noisy_sum = sum(noisy_data)
    
    # Remove noise to get actual sum (in real SMPC, this is done securely)
    actual_sum = noisy_sum - sum(noise)
    
    return {
        'parties_data': parties_data,
        'noisy_data': noisy_data,
        'noisy_sum': noisy_sum,
        'actual_sum': actual_sum,
        'privacy_preserved': True
    }

# ============================================================================
# HOMOMORPHIC ENCRYPTION CONCEPTS
# ============================================================================

def homomorphic_encryption_demo():
    """
    Demonstrate concept of homomorphic encryption
    (simplified - real implementation is much more complex)
    """
    # Simulate encrypted values (in reality, these would be encrypted)
    encrypted_a = 100  # Encrypted value of 50
    encrypted_b = 200  # Encrypted value of 75
    
    # Homomorphic addition (can compute on encrypted data)
    encrypted_sum = encrypted_a + encrypted_b  # Result: 300 (represents 125)
    
    # In real homomorphic encryption, you can compute without decrypting
    return {
        'encrypted_a': encrypted_a,
        'encrypted_b': encrypted_b,
        'encrypted_sum': encrypted_sum,
        'actual_a': 50,
        'actual_b': 75,
        'actual_sum': 125
    }

# ============================================================================
# PRIVACY-UTILITY TRADE-OFF ANALYSIS
# ============================================================================

def analyze_privacy_utility_tradeoff():
    """
    Analyze trade-offs between privacy and utility for different PETs
    """
    technologies = {
        'No Protection': {'privacy': 1, 'utility': 10, 'cost': 1, 'performance': 10},
        'Anonymization': {'privacy': 6, 'utility': 8, 'cost': 2, 'performance': 9},
        'Pseudonymization': {'privacy': 7, 'utility': 7, 'cost': 3, 'performance': 8},
        'Differential Privacy': {'privacy': 9, 'utility': 6, 'cost': 4, 'performance': 7},
        'SMPC': {'privacy': 10, 'utility': 5, 'cost': 9, 'performance': 4},
        'Homomorphic Encryption': {'privacy': 10, 'utility': 4, 'cost': 10, 'performance': 3}
    }
    
    return technologies

# ============================================================================
# VISUALIZATIONS
# ============================================================================

def plot_pet_comparison(technologies):
    """
    Plot comparison of Privacy-Enhancing Technologies
    """
    tech_names = list(technologies.keys())
    privacy_scores = [tech['privacy'] for tech in technologies.values()]
    utility_scores = [tech['utility'] for tech in technologies.values()]
    cost_scores = [tech['cost'] for tech in technologies.values()]
    
    fig, axes = plt.subplots(1, 3, figsize=(18, 6))
    
    # Privacy scores
    axes[0].barh(tech_names, privacy_scores, color='#9b59b6', alpha=0.8)
    axes[0].set_title('Privacy Level (Higher is Better)', fontsize=12, fontweight='bold')
    axes[0].set_xlabel('Privacy Score (1-10)')
    axes[0].grid(axis='x', alpha=0.3)
    axes[0].set_xlim([0, 11])
    
    # Utility scores
    axes[1].barh(tech_names, utility_scores, color='#2ecc71', alpha=0.8)
    axes[1].set_title('Data Utility (Higher is Better)', fontsize=12, fontweight='bold')
    axes[1].set_xlabel('Utility Score (1-10)')
    axes[1].grid(axis='x', alpha=0.3)
    axes[1].set_xlim([0, 11])
    
    # Cost scores
    axes[2].barh(tech_names, cost_scores, color='#e74c3c', alpha=0.8)
    axes[2].set_title('Implementation Cost (Lower is Better)', fontsize=12, fontweight='bold')
    axes[2].set_xlabel('Cost Score (1-10)')
    axes[2].grid(axis='x', alpha=0.3)
    axes[2].set_xlim([0, 11])
    
    plt.tight_layout()
    plt.savefig('unit3-privacy-security/examples/pet_comparison.png', 
                dpi=300, bbox_inches='tight')
    print("✅ Saved: pet_comparison.png")
    plt.close()

def plot_privacy_utility_tradeoff(technologies):
    """
    Plot privacy-utility trade-off curve
    """
    fig, ax = plt.subplots(figsize=(10, 8))
    
    tech_names = list(technologies.keys())
    privacy = [tech['privacy'] for tech in technologies.values()]
    utility = [tech['utility'] for tech in technologies.values()]
    
    scatter = ax.scatter(privacy, utility, s=200, alpha=0.7, c=range(len(tech_names)), 
                        cmap='viridis', edgecolors='black', linewidth=2)
    
    for i, name in enumerate(tech_names):
        ax.annotate(name, (privacy[i], utility[i]), 
                   xytext=(5, 5), textcoords='offset points', fontsize=9)
    
    ax.set_xlabel('Privacy Level (1-10)', fontsize=11, fontweight='bold')
    ax.set_ylabel('Data Utility (1-10)', fontsize=11, fontweight='bold')
    ax.set_title('Privacy-Utility Trade-off for Different PETs', 
                fontsize=12, fontweight='bold')
    ax.grid(alpha=0.3)
    ax.set_xlim([0, 11])
    ax.set_ylim([0, 11])
    
    plt.colorbar(scatter, ax=ax, label='Technology Index')
    plt.tight_layout()
    plt.savefig('unit3-privacy-security/examples/privacy_utility_tradeoff.png', 
                dpi=300, bbox_inches='tight')
    print("✅ Saved: privacy_utility_tradeoff.png")
    plt.close()

# ============================================================================
# MAIN EXECUTION
# ============================================================================

if __name__ == "__main__":
    print("="*80)
    print("Unit 3 - Example 2: Privacy-Enhancing Technologies (PETs)")
    print("="*80)
    
    # SMPC demonstration
    print("\n1. Secure Multi-Party Computation (SMPC):")
    parties_data = [1000, 2000, 1500]  # Three parties' private data
    smpc_result = smpc_sum_simulation(parties_data, n_parties=3)
    print(f"  Party 1 data: {smpc_result['parties_data'][0]}")
    print(f"  Party 2 data: {smpc_result['parties_data'][1]}")
    print(f"  Party 3 data: {smpc_result['parties_data'][2]}")
    print(f"  Computed sum: {smpc_result['actual_sum']}")
    print(f"  Privacy preserved: {smpc_result['privacy_preserved']}")
    
    # Homomorphic encryption demonstration
    print("\n2. Homomorphic Encryption:")
    he_result = homomorphic_encryption_demo()
    print(f"  Encrypted value A: {he_result['encrypted_a']}")
    print(f"  Encrypted value B: {he_result['encrypted_b']}")
    print(f"  Encrypted sum (computed on encrypted data): {he_result['encrypted_sum']}")
    print(f"  Actual sum: {he_result['actual_sum']}")
    
    # Privacy-utility trade-off
    print("\n3. Privacy-Utility Trade-off Analysis:")
    technologies = analyze_privacy_utility_tradeoff()
    for tech, metrics in technologies.items():
        print(f"\n{tech}:")
        print(f"  Privacy: {metrics['privacy']}/10")
        print(f"  Utility: {metrics['utility']}/10")
        print(f"  Cost: {metrics['cost']}/10")
    
    # Create visualizations
    print("\n" + "="*80)
    print("Creating Visualizations...")
    print("="*80)
    
    plot_pet_comparison(technologies)
    plot_privacy_utility_tradeoff(technologies)
    
    # Summary
    print("\n" + "="*80)
    print("SUMMARY")
    print("="*80)
    print("\nKey Takeaways:")
    print("1. SMPC allows computation on data without revealing individual values")
    print("2. Homomorphic encryption enables computation on encrypted data")
    print("3. Different PETs have different privacy-utility trade-offs")
    print("4. Higher privacy often comes at the cost of utility or performance")
    print("5. Choose PET based on specific privacy and utility requirements")
    print("="*80 + "\n")
