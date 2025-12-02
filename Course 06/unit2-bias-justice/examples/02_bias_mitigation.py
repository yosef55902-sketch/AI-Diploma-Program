"""
Unit 2: Bias, Justice, and Discrimination in AI
Example 2: Bias Mitigation Techniques

This example demonstrates bias mitigation techniques at different stages of the ML pipeline:
- Pre-processing techniques (before model training)
- In-processing techniques (during model training)
- Post-processing techniques (after model training)
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from fairlearn.metrics import demographic_parity_difference, equalized_odds_difference
from fairlearn.postprocessing import ThresholdOptimizer
from fairlearn.preprocessing import CorrelationRemover
import warnings
warnings.filterwarnings('ignore')

# Set up plotting
plt.rcParams['font.size'] = 10
plt.rcParams['figure.figsize'] = (14, 8)
sns.set_style("whitegrid")

# ============================================================================
# GENERATE SYNTHETIC BIASED DATASET
# ============================================================================

def generate_biased_dataset(n_samples=2000, bias_strength=0.3):
    """
    Generate a synthetic dataset with bias in the sensitive attribute
    """
    np.random.seed(42)
    
    # Sensitive attribute (e.g., gender: 0 = group A, 1 = group B)
    sensitive = np.random.binomial(1, 0.5, n_samples)
    
    # Features
    X1 = np.random.normal(0, 1, n_samples)
    X2 = np.random.normal(0, 1, n_samples)
    
    # Introduce bias: group B has lower probability of positive outcome
    # even with similar features
    true_prob = 0.3 + 0.4 * X1 + 0.3 * X2
    bias_penalty = bias_strength * (1 - sensitive)  # Group B (0) gets penalty
    prob = true_prob - bias_penalty + np.random.normal(0, 0.1, n_samples)
    prob = np.clip(prob, 0, 1)
    
    # Target variable
    y = (prob > 0.5).astype(int)
    
    # Create DataFrame
    df = pd.DataFrame({
        'feature1': X1,
        'feature2': X2,
        'sensitive': sensitive,
        'target': y
    })
    
    return df

# ============================================================================
# PRE-PROCESSING TECHNIQUES
# ============================================================================

def preprocess_reweighing(X_train, y_train, sensitive_train):
    """
    Reweighing: Assign different weights to balance group representation
    """
    # Calculate weights to balance groups
    group_counts = pd.Series(sensitive_train).value_counts()
    total = len(sensitive_train)
    
    weights = np.ones(len(sensitive_train))
    for group in group_counts.index:
        group_size = group_counts[group]
        # Weight inversely proportional to group size
        weights[sensitive_train == group] = total / (2 * group_size)
    
    return weights

def preprocess_correlation_removal(X_train, X_test, sensitive_train):
    """
    Fair Representation Learning: Remove correlation with sensitive attribute
    """
    # Use CorrelationRemover from fairlearn
    remover = CorrelationRemover(sensitive_feature_ids=[X_train.shape[1]])
    
    # Add sensitive attribute as last column
    X_train_extended = np.column_stack([X_train, sensitive_train])
    X_test_extended = np.column_stack([X_test, np.zeros(len(X_test))])
    
    # Fit and transform
    X_train_fair = remover.fit_transform(X_train_extended)
    X_test_fair = remover.transform(X_test_extended)
    
    # Remove the last column (was sensitive attribute)
    X_train_fair = X_train_fair[:, :-1]
    X_test_fair = X_test_fair[:, :-1]
    
    return X_train_fair, X_test_fair

# ============================================================================
# IN-PROCESSING TECHNIQUES
# ============================================================================

def train_fair_model(X_train, y_train, sensitive_train, method='reweighing'):
    """
    Train model with fairness constraints during training
    """
    if method == 'reweighing':
        # Use sample weights from reweighing
        weights = preprocess_reweighing(X_train, y_train, sensitive_train)
        model = RandomForestClassifier(n_estimators=100, random_state=42)
        model.fit(X_train, y_train, sample_weight=weights)
    else:
        # Standard training
        model = RandomForestClassifier(n_estimators=100, random_state=42)
        model.fit(X_train, y_train)
    
    return model

# ============================================================================
# POST-PROCESSING TECHNIQUES
# ============================================================================

def postprocess_equalized_odds(model, X_test, y_test, sensitive_test):
    """
    Post-processing: Adjust predictions to achieve equalized odds
    """
    # Get predictions
    y_pred_proba = model.predict_proba(X_test)[:, 1]
    
    # Use ThresholdOptimizer from fairlearn
    threshold_optimizer = ThresholdOptimizer(
        estimator=model,
        constraints="equalized_odds",
        prefit=True
    )
    
    threshold_optimizer.fit(X_test, y_test, sensitive_features=sensitive_test)
    y_pred_fair = threshold_optimizer.predict(X_test, sensitive_features=sensitive_test)
    
    return y_pred_fair

# ============================================================================
# EVALUATION FUNCTIONS
# ============================================================================

def evaluate_fairness(y_true, y_pred, sensitive):
    """
    Evaluate fairness metrics
    """
    metrics = {
        'demographic_parity_diff': demographic_parity_difference(
            y_true, y_pred, sensitive_features=sensitive
        ),
        'equalized_odds_diff': equalized_odds_difference(
            y_true, y_pred, sensitive_features=sensitive
        ),
        'accuracy': accuracy_score(y_true, y_pred)
    }
    
    return metrics

def compare_mitigation_techniques(df):
    """
    Compare different bias mitigation techniques
    """
    # Prepare data
    X = df[['feature1', 'feature2']].values
    y = df['target'].values
    sensitive = df['sensitive'].values
    
    # Split data
    X_train, X_test, y_train, y_test, sensitive_train, sensitive_test = train_test_split(
        X, y, sensitive, test_size=0.3, random_state=42, stratify=y
    )
    
    # Scale features
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    
    results = {}
    
    # 1. Baseline (no mitigation)
    print("="*80)
    print("1. BASELINE MODEL (No Mitigation)")
    print("="*80)
    baseline_model = RandomForestClassifier(n_estimators=100, random_state=42)
    baseline_model.fit(X_train_scaled, y_train)
    y_pred_baseline = baseline_model.predict(X_test_scaled)
    results['Baseline'] = evaluate_fairness(y_test, y_pred_baseline, sensitive_test)
    print(f"Demographic Parity Difference: {results['Baseline']['demographic_parity_diff']:.4f}")
    print(f"Equalized Odds Difference: {results['Baseline']['equalized_odds_diff']:.4f}")
    print(f"Accuracy: {results['Baseline']['accuracy']:.4f}")
    
    # 2. Pre-processing: Reweighing
    print("\n" + "="*80)
    print("2. PRE-PROCESSING: REWEIGHING")
    print("="*80)
    weights = preprocess_reweighing(X_train_scaled, y_train, sensitive_train)
    reweigh_model = RandomForestClassifier(n_estimators=100, random_state=42)
    reweigh_model.fit(X_train_scaled, y_train, sample_weight=weights)
    y_pred_reweigh = reweigh_model.predict(X_test_scaled)
    results['Reweighing'] = evaluate_fairness(y_test, y_pred_reweigh, sensitive_test)
    print(f"Demographic Parity Difference: {results['Reweighing']['demographic_parity_diff']:.4f}")
    print(f"Equalized Odds Difference: {results['Reweighing']['equalized_odds_diff']:.4f}")
    print(f"Accuracy: {results['Reweighing']['accuracy']:.4f}")
    
    # 3. Pre-processing: Correlation Removal
    print("\n" + "="*80)
    print("3. PRE-PROCESSING: CORRELATION REMOVAL")
    print("="*80)
    X_train_fair, X_test_fair = preprocess_correlation_removal(
        X_train_scaled, X_test_scaled, sensitive_train
    )
    corr_removal_model = RandomForestClassifier(n_estimators=100, random_state=42)
    corr_removal_model.fit(X_train_fair, y_train)
    y_pred_corr = corr_removal_model.predict(X_test_fair)
    results['Correlation Removal'] = evaluate_fairness(y_test, y_pred_corr, sensitive_test)
    print(f"Demographic Parity Difference: {results['Correlation Removal']['demographic_parity_diff']:.4f}")
    print(f"Equalized Odds Difference: {results['Correlation Removal']['equalized_odds_diff']:.4f}")
    print(f"Accuracy: {results['Correlation Removal']['accuracy']:.4f}")
    
    # 4. Post-processing: Equalized Odds
    print("\n" + "="*80)
    print("4. POST-PROCESSING: EQUALIZED ODDS")
    print("="*80)
    y_pred_post = postprocess_equalized_odds(
        baseline_model, X_test_scaled, y_test, sensitive_test
    )
    results['Post-processing'] = evaluate_fairness(y_test, y_pred_post, sensitive_test)
    print(f"Demographic Parity Difference: {results['Post-processing']['demographic_parity_diff']:.4f}")
    print(f"Equalized Odds Difference: {results['Post-processing']['equalized_odds_diff']:.4f}")
    print(f"Accuracy: {results['Post-processing']['accuracy']:.4f}")
    
    return results, {
        'baseline': (y_test, y_pred_baseline, sensitive_test),
        'reweighing': (y_test, y_pred_reweigh, sensitive_test),
        'correlation_removal': (y_test, y_pred_corr, sensitive_test),
        'post_processing': (y_test, y_pred_post, sensitive_test)
    }

# ============================================================================
# VISUALIZATIONS
# ============================================================================

def plot_mitigation_comparison(results):
    """
    Plot comparison of different mitigation techniques
    """
    methods = list(results.keys())
    dp_diffs = [abs(results[m]['demographic_parity_diff']) for m in methods]
    eo_diffs = [abs(results[m]['equalized_odds_diff']) for m in methods]
    accuracies = [results[m]['accuracy'] for m in methods]
    
    fig, axes = plt.subplots(1, 3, figsize=(18, 6))
    
    # Demographic Parity Difference
    axes[0].bar(methods, dp_diffs, color=['#e74c3c', '#3498db', '#2ecc71', '#f39c12'])
    axes[0].set_title('Demographic Parity Difference (Lower is Better)', fontsize=12, fontweight='bold')
    axes[0].set_ylabel('Absolute Difference')
    axes[0].tick_params(axis='x', rotation=15)
    axes[0].grid(axis='y', alpha=0.3)
    
    # Equalized Odds Difference
    axes[1].bar(methods, eo_diffs, color=['#e74c3c', '#3498db', '#2ecc71', '#f39c12'])
    axes[1].set_title('Equalized Odds Difference (Lower is Better)', fontsize=12, fontweight='bold')
    axes[1].set_ylabel('Absolute Difference')
    axes[1].tick_params(axis='x', rotation=15)
    axes[1].grid(axis='y', alpha=0.3)
    
    # Accuracy
    axes[2].bar(methods, accuracies, color=['#e74c3c', '#3498db', '#2ecc71', '#f39c12'])
    axes[2].set_title('Model Accuracy', fontsize=12, fontweight='bold')
    axes[2].set_ylabel('Accuracy')
    axes[2].tick_params(axis='x', rotation=15)
    axes[2].grid(axis='y', alpha=0.3)
    axes[2].set_ylim([0, 1])
    
    plt.tight_layout()
    plt.savefig('unit2-bias-justice/examples/bias_mitigation_comparison.png', 
                dpi=300, bbox_inches='tight')
    print("\n✅ Saved: bias_mitigation_comparison.png")
    plt.close()

def plot_confusion_matrices(predictions_dict):
    """
    Plot confusion matrices for each method
    """
    fig, axes = plt.subplots(2, 2, figsize=(14, 12))
    axes = axes.flatten()
    
    titles = ['Baseline', 'Reweighing', 'Correlation Removal', 'Post-processing']
    
    for idx, (method, (y_true, y_pred, sensitive)) in enumerate(predictions_dict.items()):
        cm = confusion_matrix(y_true, y_pred)
        sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', ax=axes[idx])
        axes[idx].set_title(f'{titles[idx]}\nAccuracy: {accuracy_score(y_true, y_pred):.3f}', 
                           fontsize=11, fontweight='bold')
        axes[idx].set_xlabel('Predicted')
        axes[idx].set_ylabel('Actual')
    
    plt.tight_layout()
    plt.savefig('unit2-bias-justice/examples/bias_mitigation_confusion_matrices.png', 
                dpi=300, bbox_inches='tight')
    print("✅ Saved: bias_mitigation_confusion_matrices.png")
    plt.close()

def plot_fairness_by_group(predictions_dict):
    """
    Plot fairness metrics by sensitive group
    """
    fig, axes = plt.subplots(2, 2, figsize=(14, 12))
    axes = axes.flatten()
    
    titles = ['Baseline', 'Reweighing', 'Correlation Removal', 'Post-processing']
    
    for idx, (method, (y_true, y_pred, sensitive)) in enumerate(predictions_dict.items()):
        # Calculate metrics by group
        group_0 = sensitive == 0
        group_1 = sensitive == 1
        
        acc_group_0 = accuracy_score(y_true[group_0], y_pred[group_0])
        acc_group_1 = accuracy_score(y_true[group_1], y_pred[group_1])
        
        tpr_group_0 = np.sum((y_true[group_0] == 1) & (y_pred[group_0] == 1)) / max(np.sum(y_true[group_0] == 1), 1)
        tpr_group_1 = np.sum((y_true[group_1] == 1) & (y_pred[group_1] == 1)) / max(np.sum(y_true[group_1] == 1), 1)
        
        groups = ['Group A', 'Group B']
        accuracies = [acc_group_0, acc_group_1]
        tprs = [tpr_group_0, tpr_group_1]
        
        x = np.arange(len(groups))
        width = 0.35
        
        axes[idx].bar(x - width/2, accuracies, width, label='Accuracy', alpha=0.8)
        axes[idx].bar(x + width/2, tprs, width, label='True Positive Rate', alpha=0.8)
        axes[idx].set_title(titles[idx], fontsize=11, fontweight='bold')
        axes[idx].set_ylabel('Score')
        axes[idx].set_xticks(x)
        axes[idx].set_xticklabels(groups)
        axes[idx].legend()
        axes[idx].grid(axis='y', alpha=0.3)
        axes[idx].set_ylim([0, 1])
    
    plt.tight_layout()
    plt.savefig('unit2-bias-justice/examples/bias_mitigation_by_group.png', 
                dpi=300, bbox_inches='tight')
    print("✅ Saved: bias_mitigation_by_group.png")
    plt.close()

# ============================================================================
# MAIN EXECUTION
# ============================================================================

if __name__ == "__main__":
    print("="*80)
    print("Unit 2 - Example 2: Bias Mitigation Techniques")
    print("="*80)
    
    # Generate biased dataset
    print("\nGenerating synthetic biased dataset...")
    df = generate_biased_dataset(n_samples=2000, bias_strength=0.3)
    print(f"Dataset shape: {df.shape}")
    print(f"\nTarget distribution:")
    print(df['target'].value_counts())
    print(f"\nSensitive attribute distribution:")
    print(df['sensitive'].value_counts())
    
    # Compare mitigation techniques
    results, predictions = compare_mitigation_techniques(df)
    
    # Create visualizations
    print("\n" + "="*80)
    print("Creating Visualizations...")
    print("="*80)
    
    plot_mitigation_comparison(results)
    plot_confusion_matrices(predictions)
    plot_fairness_by_group(predictions)
    
    # Summary
    print("\n" + "="*80)
    print("SUMMARY")
    print("="*80)
    print("\nKey Takeaways:")
    print("1. Pre-processing techniques modify data before training")
    print("2. In-processing techniques modify the learning algorithm")
    print("3. Post-processing techniques adjust predictions after training")
    print("4. Each technique has trade-offs between fairness and accuracy")
    print("5. The best technique depends on the specific use case and requirements")
    print("="*80 + "\n")

