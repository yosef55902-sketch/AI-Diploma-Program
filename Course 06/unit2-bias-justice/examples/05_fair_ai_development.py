"""
Unit 2: Bias, Justice, and Discrimination in AI
Example 5: Practical Approaches to Fair AI Development

This example demonstrates practical approaches for developing fair AI systems:
- Inclusive Data Collection
- Bias-Aware Algorithms
- Human-in-the-Loop Approaches for Fairness Evaluation
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, classification_report
from fairlearn.metrics import demographic_parity_difference, equalized_odds_difference
import warnings
warnings.filterwarnings('ignore')

plt.rcParams['font.size'] = 10
plt.rcParams['figure.figsize'] = (14, 8)
sns.set_style("whitegrid")

# ============================================================================
# INCLUSIVE DATA COLLECTION
# ============================================================================

def inclusive_data_collection():
    """
    Demonstrate inclusive data collection strategies
    """
    print("="*80)
    print("1. INCLUSIVE DATA COLLECTION")
    print("="*80)
    
    # Simulate data collection scenarios
    scenarios = {
        'Unbalanced': {
            'Group_A': 800,
            'Group_B': 200,
            'Group_C': 0
        },
        'Balanced': {
            'Group_A': 400,
            'Group_B': 400,
            'Group_C': 200
        },
        'Oversampled_Minority': {
            'Group_A': 400,
            'Group_B': 400,
            'Group_C': 400
        }
    }
    
    print("\nData Collection Strategies:")
    for scenario, counts in scenarios.items():
        total = sum(counts.values())
        print(f"\n{scenario}:")
        for group, count in counts.items():
            percentage = count / total * 100
            print(f"  {group}: {count} samples ({percentage:.1f}%)")
    
    return scenarios

# ============================================================================
# BIAS-AWARE ALGORITHMS
# ============================================================================

def generate_fair_dataset(n_samples=2000):
    """
    Generate dataset for fair AI development
    """
    np.random.seed(42)
    
    # Multiple sensitive attributes
    sensitive_1 = np.random.choice([0, 1], n_samples, p=[0.6, 0.4])
    sensitive_2 = np.random.choice([0, 1], n_samples, p=[0.7, 0.3])
    
    # Features
    X1 = np.random.normal(0, 1, n_samples)
    X2 = np.random.normal(0, 1, n_samples)
    X3 = np.random.normal(0, 1, n_samples)
    
    # Target (should be independent of sensitive attributes)
    y = (0.4 * X1 + 0.3 * X2 + 0.3 * X3 + np.random.normal(0, 0.1, n_samples) > 0).astype(int)
    
    df = pd.DataFrame({
        'feature1': X1,
        'feature2': X2,
        'feature3': X3,
        'sensitive_1': sensitive_1,
        'sensitive_2': sensitive_2,
        'target': y
    })
    
    return df

def bias_aware_training(X_train, y_train, sensitive_train, method='fairness_constraint'):
    """
    Train model with bias-aware techniques
    """
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    
    if method == 'fairness_constraint':
        # Use sample weights to balance groups
        group_counts = pd.Series(sensitive_train).value_counts()
        total = len(sensitive_train)
        weights = np.ones(len(sensitive_train))
        for group in group_counts.index:
            weights[sensitive_train == group] = total / (len(group_counts) * group_counts[group])
        
        model = RandomForestClassifier(n_estimators=100, random_state=42)
        model.fit(X_train_scaled, y_train, sample_weight=weights)
    else:
        model = RandomForestClassifier(n_estimators=100, random_state=42)
        model.fit(X_train_scaled, y_train)
    
    return model, scaler

# ============================================================================
# HUMAN-IN-THE-LOOP FAIRNESS EVALUATION
# ============================================================================

def human_in_the_loop_evaluation(model, X_test, y_test, sensitive_test, threshold=0.5):
    """
    Simulate human-in-the-loop fairness evaluation
    """
    # Get model predictions
    y_pred_proba = model.predict_proba(X_test)[:, 1]
    y_pred = (y_pred_proba > threshold).astype(int)
    
    # Identify uncertain cases (close to threshold)
    uncertainty = np.abs(y_pred_proba - threshold)
    uncertain_mask = uncertainty < 0.1  # Cases within 10% of threshold
    
    # Human review for uncertain cases
    human_reviewed = y_pred.copy()
    human_correct = 0
    human_reviewed_count = uncertain_mask.sum()
    
    if human_reviewed_count > 0:
        # Simulate human review (assume 80% accuracy for human)
        human_predictions = y_test[uncertain_mask].copy()
        # Add some human error
        human_error = np.random.random(human_reviewed_count) < 0.2
        human_predictions[human_error] = 1 - human_predictions[human_error]
        human_reviewed[uncertain_mask] = human_predictions
        human_correct = (human_predictions == y_test[uncertain_mask]).sum()
    
    return {
        'automated': y_pred,
        'human_reviewed': human_reviewed,
        'uncertain_count': human_reviewed_count,
        'human_correct': human_correct,
        'uncertain_mask': uncertain_mask
    }

# ============================================================================
# COMPREHENSIVE FAIR AI DEVELOPMENT PIPELINE
# ============================================================================

def fair_ai_development_pipeline(df):
    """
    Complete pipeline for fair AI development
    """
    X = df[['feature1', 'feature2', 'feature3']].values
    y = df['target'].values
    sensitive = df['sensitive_1'].values
    
    # Split data
    X_train, X_test, y_train, y_test, sensitive_train, sensitive_test = train_test_split(
        X, y, sensitive, test_size=0.3, random_state=42, stratify=y
    )
    
    results = {}
    
    # 1. Standard training (baseline)
    print("\n" + "="*80)
    print("2. BIAS-AWARE ALGORITHMS")
    print("="*80)
    print("\nBaseline Model (No Fairness Constraints):")
    baseline_model, baseline_scaler = bias_aware_training(
        X_train, y_train, sensitive_train, method='standard'
    )
    X_test_scaled = baseline_scaler.transform(X_test)
    y_pred_baseline = baseline_model.predict(X_test_scaled)
    
    results['Baseline'] = {
        'model': baseline_model,
        'scaler': baseline_scaler,
        'predictions': y_pred_baseline,
        'accuracy': accuracy_score(y_test, y_pred_baseline),
        'dp_diff': demographic_parity_difference(y_test, y_pred_baseline, sensitive_features=sensitive_test),
        'eo_diff': equalized_odds_difference(y_test, y_pred_baseline, sensitive_features=sensitive_test)
    }
    
    print(f"  Accuracy: {results['Baseline']['accuracy']:.4f}")
    print(f"  Demographic Parity Difference: {results['Baseline']['dp_diff']:.4f}")
    print(f"  Equalized Odds Difference: {results['Baseline']['eo_diff']:.4f}")
    
    # 2. Fairness-constrained training
    print("\nFairness-Constrained Model:")
    fair_model, fair_scaler = bias_aware_training(
        X_train, y_train, sensitive_train, method='fairness_constraint'
    )
    X_test_fair = fair_scaler.transform(X_test)
    y_pred_fair = fair_model.predict(X_test_fair)
    
    results['Fair'] = {
        'model': fair_model,
        'scaler': fair_scaler,
        'predictions': y_pred_fair,
        'accuracy': accuracy_score(y_test, y_pred_fair),
        'dp_diff': demographic_parity_difference(y_test, y_pred_fair, sensitive_features=sensitive_test),
        'eo_diff': equalized_odds_difference(y_test, y_pred_fair, sensitive_features=sensitive_test)
    }
    
    print(f"  Accuracy: {results['Fair']['accuracy']:.4f}")
    print(f"  Demographic Parity Difference: {results['Fair']['dp_diff']:.4f}")
    print(f"  Equalized Odds Difference: {results['Fair']['eo_diff']:.4f}")
    
    # 3. Human-in-the-loop evaluation
    print("\n" + "="*80)
    print("3. HUMAN-IN-THE-LOOP FAIRNESS EVALUATION")
    print("="*80)
    hitl_results = human_in_the_loop_evaluation(
        fair_model, X_test_fair, y_test, sensitive_test
    )
    
    results['HITL'] = {
        'automated': hitl_results['automated'],
        'human_reviewed': hitl_results['human_reviewed'],
        'uncertain_count': hitl_results['uncertain_count'],
        'human_correct': hitl_results['human_correct']
    }
    
    print(f"\nAutomated Predictions: {len(hitl_results['automated'])}")
    print(f"Uncertain Cases (Human Review): {hitl_results['uncertain_count']}")
    print(f"Human Review Accuracy: {hitl_results['human_correct'] / max(hitl_results['uncertain_count'], 1):.2%}")
    
    # Evaluate HITL performance
    hitl_accuracy = accuracy_score(y_test, hitl_results['human_reviewed'])
    hitl_dp_diff = demographic_parity_difference(
        y_test, hitl_results['human_reviewed'], sensitive_features=sensitive_test
    )
    hitl_eo_diff = equalized_odds_difference(
        y_test, hitl_results['human_reviewed'], sensitive_features=sensitive_test
    )
    
    results['HITL']['accuracy'] = hitl_accuracy
    results['HITL']['dp_diff'] = hitl_dp_diff
    results['HITL']['eo_diff'] = hitl_eo_diff
    
    print(f"\nHITL Model Performance:")
    print(f"  Accuracy: {hitl_accuracy:.4f}")
    print(f"  Demographic Parity Difference: {hitl_dp_diff:.4f}")
    print(f"  Equalized Odds Difference: {hitl_eo_diff:.4f}")
    
    return results, sensitive_test

# ============================================================================
# VISUALIZATIONS
# ============================================================================

def plot_data_collection_strategies(scenarios):
    """
    Plot data collection strategy comparison
    """
    fig, ax = plt.subplots(figsize=(12, 6))
    
    groups = ['Group_A', 'Group_B', 'Group_C']
    x = np.arange(len(groups))
    width = 0.25
    
    for idx, (scenario, counts) in enumerate(scenarios.items()):
        values = [counts.get(g, 0) for g in groups]
        ax.bar(x + idx * width, values, width, label=scenario.replace('_', ' '), alpha=0.8)
    
    ax.set_title('Data Collection Strategies Comparison', fontsize=12, fontweight='bold')
    ax.set_ylabel('Number of Samples')
    ax.set_xlabel('Demographic Group')
    ax.set_xticks(x + width)
    ax.set_xticklabels(groups)
    ax.legend()
    ax.grid(axis='y', alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('unit2-bias-justice/examples/fair_ai_data_collection.png', 
                dpi=300, bbox_inches='tight')
    print("\n✅ Saved: fair_ai_data_collection.png")
    plt.close()

def plot_fairness_comparison(results, sensitive_test):
    """
    Plot fairness metrics comparison
    """
    methods = ['Baseline', 'Fair', 'HITL']
    dp_diffs = [abs(results[m]['dp_diff']) for m in methods]
    eo_diffs = [abs(results[m]['eo_diff']) for m in methods]
    accuracies = [results[m]['accuracy'] for m in methods]
    
    fig, axes = plt.subplots(1, 3, figsize=(18, 6))
    
    axes[0].bar(methods, dp_diffs, color=['#e74c3c', '#3498db', '#2ecc71'])
    axes[0].set_title('Demographic Parity Difference (Lower is Better)', 
                     fontsize=12, fontweight='bold')
    axes[0].set_ylabel('Absolute Difference')
    axes[0].grid(axis='y', alpha=0.3)
    
    axes[1].bar(methods, eo_diffs, color=['#e74c3c', '#3498db', '#2ecc71'])
    axes[1].set_title('Equalized Odds Difference (Lower is Better)', 
                     fontsize=12, fontweight='bold')
    axes[1].set_ylabel('Absolute Difference')
    axes[1].grid(axis='y', alpha=0.3)
    
    axes[2].bar(methods, accuracies, color=['#e74c3c', '#3498db', '#2ecc71'])
    axes[2].set_title('Model Accuracy', fontsize=12, fontweight='bold')
    axes[2].set_ylabel('Accuracy')
    axes[2].set_ylim([0, 1])
    axes[2].grid(axis='y', alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('unit2-bias-justice/examples/fair_ai_comparison.png', 
                dpi=300, bbox_inches='tight')
    print("✅ Saved: fair_ai_comparison.png")
    plt.close()

def plot_hitl_workflow(results):
    """
    Plot human-in-the-loop workflow visualization
    """
    fig, ax = plt.subplots(figsize=(12, 8))
    
    # Create workflow diagram
    stages = ['Automated\nPrediction', 'Uncertainty\nDetection', 'Human\nReview', 'Final\nDecision']
    counts = [
        len(results['HITL']['automated']),
        results['HITL']['uncertain_count'],
        results['HITL']['uncertain_count'],
        len(results['HITL']['human_reviewed'])
    ]
    
    colors = ['#3498db', '#f39c12', '#2ecc71', '#9b59b6']
    
    bars = ax.bar(stages, counts, color=colors, alpha=0.8)
    
    # Add value labels
    for bar, count in zip(bars, counts):
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height,
               f'{count}',
               ha='center', va='bottom', fontsize=11, fontweight='bold')
    
    ax.set_title('Human-in-the-Loop Fairness Evaluation Workflow', 
                fontsize=12, fontweight='bold')
    ax.set_ylabel('Number of Cases')
    ax.grid(axis='y', alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('unit2-bias-justice/examples/fair_ai_hitl_workflow.png', 
                dpi=300, bbox_inches='tight')
    print("✅ Saved: fair_ai_hitl_workflow.png")
    plt.close()

# ============================================================================
# MAIN EXECUTION
# ============================================================================

if __name__ == "__main__":
    print("="*80)
    print("Unit 2 - Example 5: Practical Approaches to Fair AI Development")
    print("="*80)
    
    # 1. Inclusive Data Collection
    scenarios = inclusive_data_collection()
    
    # 2. Generate dataset and run pipeline
    print("\nGenerating dataset for fair AI development...")
    df = generate_fair_dataset(n_samples=2000)
    print(f"Dataset shape: {df.shape}")
    
    # Run comprehensive pipeline
    results, sensitive_test = fair_ai_development_pipeline(df)
    
    # Create visualizations
    print("\n" + "="*80)
    print("Creating Visualizations...")
    print("="*80)
    
    plot_data_collection_strategies(scenarios)
    plot_fairness_comparison(results, sensitive_test)
    plot_hitl_workflow(results)
    
    # Summary
    print("\n" + "="*80)
    print("SUMMARY")
    print("="*80)
    print("\nKey Takeaways:")
    print("1. Inclusive data collection ensures representation of all groups")
    print("2. Bias-aware algorithms incorporate fairness constraints during training")
    print("3. Human-in-the-loop approaches improve fairness for uncertain cases")
    print("4. Combining these approaches leads to more fair and trustworthy AI systems")
    print("5. Continuous monitoring and evaluation are essential for maintaining fairness")
    print("="*80 + "\n")

