"""
Unit 3: Privacy, Security, and Data Protection
Example 3: Differential Privacy

This example demonstrates differential privacy concepts:
- Adding noise for privacy
- Privacy-utility trade-offs
- Epsilon (ε) parameter
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
# DIFFERENTIAL PRIVACY IMPLEMENTATION
# ============================================================================

def add_laplace_noise(value, epsilon=1.0, sensitivity=1.0):
    """
    Add Laplace noise for differential privacy
    epsilon (ε): privacy parameter (smaller = more private)
    sensitivity: maximum change in output from changing one record
    """
    scale = sensitivity / epsilon
    noise = np.random.laplace(0, scale)
    return value + noise

def differentially_private_mean(data, epsilon=1.0):
    """
    Compute differentially private mean
    """
    true_mean = np.mean(data)
    sensitivity = (data.max() - data.min()) / len(data)
    noisy_mean = add_laplace_noise(true_mean, epsilon, sensitivity)
    return true_mean, noisy_mean

def differentially_private_count(data, epsilon=1.0):
    """
    Compute differentially private count
    """
    true_count = len(data)
    sensitivity = 1.0  # Adding/removing one record changes count by 1
    noisy_count = add_laplace_noise(true_count, epsilon, sensitivity)
    return true_count, max(0, int(noisy_count))  # Ensure non-negative

# ============================================================================
# PRIVACY-UTILITY TRADE-OFF
# ============================================================================

def analyze_epsilon_impact(data, epsilon_values):
    """
    Analyze how different epsilon values affect privacy and utility
    """
    results = []
    
    true_mean = np.mean(data)
    true_count = len(data)
    
    for epsilon in epsilon_values:
        # Compute multiple times to show variance
        noisy_means = []
        noisy_counts = []
        
        for _ in range(10):
            _, noisy_mean = differentially_private_mean(data, epsilon)
            _, noisy_count = differentially_private_count(data, epsilon)
            noisy_means.append(noisy_mean)
            noisy_counts.append(noisy_count)
        
        mean_error = np.mean([abs(m - true_mean) for m in noisy_means])
        count_error = np.mean([abs(c - true_count) for c in noisy_counts])
        
        results.append({
            'epsilon': epsilon,
            'privacy_level': 1.0 / epsilon,  # Higher epsilon = less private
            'mean_error': mean_error,
            'count_error': count_error,
            'noisy_mean_avg': np.mean(noisy_means),
            'noisy_count_avg': np.mean(noisy_counts)
        })
    
    return results

# ============================================================================
# VISUALIZATIONS
# ============================================================================

def plot_differential_privacy_comparison(data, epsilon_values):
    """
    Plot comparison of differential privacy with different epsilon values
    """
    results = analyze_epsilon_impact(data, epsilon_values)
    
    fig, axes = plt.subplots(2, 2, figsize=(16, 12))
    
    epsilons = [r['epsilon'] for r in results]
    mean_errors = [r['mean_error'] for r in results]
    count_errors = [r['count_error'] for r in results]
    privacy_levels = [r['privacy_level'] for r in results]
    
    # Mean error vs epsilon
    axes[0, 0].plot(epsilons, mean_errors, marker='o', linewidth=2, markersize=8, color='#e74c3c')
    axes[0, 0].set_xlabel('Epsilon (ε)', fontsize=11, fontweight='bold')
    axes[0, 0].set_ylabel('Mean Error', fontsize=11, fontweight='bold')
    axes[0, 0].set_title('Privacy vs Accuracy: Mean Estimation', fontsize=12, fontweight='bold')
    axes[0, 0].grid(alpha=0.3)
    axes[0, 0].set_xscale('log')
    
    # Count error vs epsilon
    axes[0, 1].plot(epsilons, count_errors, marker='s', linewidth=2, markersize=8, color='#3498db')
    axes[0, 1].set_xlabel('Epsilon (ε)', fontsize=11, fontweight='bold')
    axes[0, 1].set_ylabel('Count Error', fontsize=11, fontweight='bold')
    axes[0, 1].set_title('Privacy vs Accuracy: Count Estimation', fontsize=12, fontweight='bold')
    axes[0, 1].grid(alpha=0.3)
    axes[0, 1].set_xscale('log')
    
    # Privacy level
    axes[1, 0].bar(range(len(epsilons)), privacy_levels, color='#9b59b6', alpha=0.8)
    axes[1, 0].set_xlabel('Epsilon Value Index', fontsize=11, fontweight='bold')
    axes[1, 0].set_ylabel('Privacy Level (Higher is Better)', fontsize=11, fontweight='bold')
    axes[1, 0].set_title('Privacy Level by Epsilon', fontsize=12, fontweight='bold')
    axes[1, 0].set_xticks(range(len(epsilons)))
    axes[1, 0].set_xticklabels([f'ε={e:.2f}' for e in epsilons], rotation=15)
    axes[1, 0].grid(axis='y', alpha=0.3)
    
    # Privacy-utility trade-off
    axes[1, 1].scatter(privacy_levels, mean_errors, s=200, alpha=0.7, 
                      c=epsilons, cmap='RdYlGn_r', edgecolors='black', linewidth=2)
    axes[1, 1].set_xlabel('Privacy Level', fontsize=11, fontweight='bold')
    axes[1, 1].set_ylabel('Mean Error (Lower is Better)', fontsize=11, fontweight='bold')
    axes[1, 1].set_title('Privacy-Utility Trade-off', fontsize=12, fontweight='bold')
    axes[1, 1].grid(alpha=0.3)
    cbar = plt.colorbar(axes[1, 1].collections[0], ax=axes[1, 1])
    cbar.set_label('Epsilon (ε)', fontsize=10)
    
    plt.tight_layout()
    plt.savefig('unit3-privacy-security/examples/differential_privacy_analysis.png', 
                dpi=300, bbox_inches='tight')
    print("✅ Saved: differential_privacy_analysis.png")
    plt.close()

# ============================================================================
# MAIN EXECUTION
# ============================================================================

if __name__ == "__main__":
    print("="*80)
    print("Unit 3 - Example 3: Differential Privacy")
    print("="*80)
    
    # Generate sample data
    np.random.seed(42)
    data = np.random.normal(50000, 15000, 1000)  # Salary data
    
    print(f"\nDataset: {len(data)} samples")
    print(f"True mean: ${np.mean(data):,.2f}")
    print(f"True count: {len(data)}")
    
    # Demonstrate differential privacy
    print("\n" + "="*80)
    print("Differential Privacy Demonstration")
    print("="*80)
    
    epsilon_values = [0.1, 0.5, 1.0, 2.0, 5.0]
    
    for epsilon in epsilon_values:
        true_mean, noisy_mean = differentially_private_mean(data, epsilon)
        true_count, noisy_count = differentially_private_count(data, epsilon)
        
        print(f"\nEpsilon (ε) = {epsilon}:")
        print(f"  True mean: ${true_mean:,.2f}, Noisy mean: ${noisy_mean:,.2f}")
        print(f"  Error: ${abs(noisy_mean - true_mean):,.2f}")
        print(f"  True count: {true_count}, Noisy count: {noisy_count}")
        print(f"  Privacy level: {1.0/epsilon:.2f}")
    
    # Create visualizations
    print("\n" + "="*80)
    print("Creating Visualizations...")
    print("="*80)
    
    plot_differential_privacy_comparison(data, epsilon_values)
    
    # Summary
    print("\n" + "="*80)
    print("SUMMARY")
    print("="*80)
    print("\nKey Takeaways:")
    print("1. Differential privacy adds controlled noise to protect individual privacy")
    print("2. Epsilon (ε) controls privacy level: smaller ε = more private")
    print("3. There is a trade-off between privacy and data utility")
    print("4. Differential privacy provides mathematical privacy guarantees")
    print("5. Choose epsilon based on privacy requirements and acceptable error")
    print("="*80 + "\n")
