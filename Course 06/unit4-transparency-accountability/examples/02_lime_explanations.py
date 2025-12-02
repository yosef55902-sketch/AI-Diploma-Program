"""
Unit 4: Interpretability, Transparency, and Accountability
Example 2: LIME Explanations

This example demonstrates LIME (Local Interpretable Model-agnostic Explanations):
- LIME for tabular data
- LIME for text data (simplified)
- Local interpretability
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import Ridge
from sklearn.metrics import accuracy_score
import warnings
warnings.filterwarnings('ignore')

# Try to import LIME, use simplified version if not available
try:
    import lime
    import lime.lime_tabular
    LIME_AVAILABLE = True
except ImportError:
    LIME_AVAILABLE = False
    print("Note: LIME library not available. Using simplified LIME implementation.")

plt.rcParams['font.size'] = 10
plt.rcParams['figure.figsize'] = (14, 8)
sns.set_style("whitegrid")

# ============================================================================
# SIMPLIFIED LIME IMPLEMENTATION
# ============================================================================

def lime_explanation_simple(model, X_sample, X_train, feature_names, n_samples=5000):
    """
    Simplified LIME implementation using local linear approximation
    """
    # Generate perturbed samples around the instance
    np.random.seed(42)
    perturbations = np.random.normal(0, 0.1, (n_samples, X_sample.shape[1]))
    X_perturbed = X_sample + perturbations
    
    # Get predictions for perturbed samples
    y_perturbed = model.predict_proba(X_perturbed)[:, 1]
    
    # Calculate distances (weights)
    distances = np.exp(-np.sum((X_perturbed - X_sample) ** 2, axis=1))
    
    # Fit linear model to approximate local behavior
    linear_model = Ridge(alpha=0.1)
    linear_model.fit(X_perturbed, y_perturbed, sample_weight=distances)
    
    # Get feature importance (coefficients)
    feature_importance = linear_model.coef_
    
    return feature_importance, linear_model

# ============================================================================
# GENERATE DATASET
# ============================================================================

def generate_dataset(n_samples=1000):
    """
    Generate synthetic dataset for LIME demonstration
    """
    np.random.seed(42)
    
    # Features
    age = np.random.randint(25, 70, n_samples)
    income = np.random.normal(60000, 25000, n_samples)
    credit_history = np.random.choice([0, 1, 2, 3], n_samples)  # 0=bad, 3=excellent
    loan_amount = np.random.uniform(10000, 200000, n_samples)
    
    # Target (loan approval)
    approval_prob = (credit_history / 3 * 0.5 +
                     (income / 100000) * 0.3 +
                     (1 - loan_amount / 200000) * 0.15 +
                     (age / 70) * 0.05 +
                     np.random.normal(0, 0.05, n_samples))
    approval = (approval_prob > 0.5).astype(int)
    
    df = pd.DataFrame({
        'age': age,
        'income': income,
        'credit_history': credit_history,
        'loan_amount': loan_amount,
        'approved': approval
    })
    
    return df

# ============================================================================
# LIME EXPLANATIONS
# ============================================================================

def explain_with_lime(model, X_sample, X_train, feature_names, use_library=True):
    """
    Generate LIME explanations for a single instance
    """
    if LIME_AVAILABLE and use_library:
        # Use actual LIME library
        explainer = lime.lime_tabular.LimeTabularExplainer(
            X_train, feature_names=feature_names, mode='classification'
        )
        explanation = explainer.explain_instance(
            X_sample[0], model.predict_proba, num_features=len(feature_names)
        )
        return explanation, explainer
    else:
        # Use simplified implementation
        feature_importance, linear_model = lime_explanation_simple(
            model, X_sample, X_train, feature_names
        )
        return feature_importance, linear_model

# ============================================================================
# VISUALIZATIONS
# ============================================================================

def plot_lime_explanation(feature_importance, feature_names, X_sample, sample_idx=0):
    """
    Plot LIME explanation for a single instance
    """
    fig, ax = plt.subplots(figsize=(12, 8))
    
    # Sort by absolute importance
    indices = np.argsort(np.abs(feature_importance))[::-1]
    
    colors = ['red' if feature_importance[i] < 0 else 'green' for i in indices]
    
    bars = ax.barh(range(len(feature_names)), 
                   [feature_importance[i] for i in indices],
                   color=colors, alpha=0.7)
    
    # Add value labels
    for i, (bar, idx) in enumerate(zip(bars, indices)):
        height = bar.get_height()
        width = bar.get_width()
        label = f'{feature_names[idx]}\n={X_sample[0, idx]:.2f}'
        ax.text(width/2 if width > 0 else width/2, i, label,
               ha='center' if width > 0 else 'right', va='center', fontsize=9)
    
    ax.set_yticks(range(len(feature_names)))
    ax.set_yticklabels([feature_names[i] for i in indices])
    ax.set_xlabel('LIME Feature Importance', fontsize=11, fontweight='bold')
    ax.set_title(f'LIME Explanation (Sample {sample_idx})', 
                fontsize=12, fontweight='bold')
    ax.axvline(x=0, color='black', linestyle='--', linewidth=1)
    ax.grid(axis='x', alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('unit4-transparency-accountability/examples/lime_explanation.png', 
                dpi=300, bbox_inches='tight')
    print("✅ Saved: lime_explanation.png")
    plt.close()

def plot_lime_comparison(explanations, feature_names, n_samples=5):
    """
    Plot LIME explanations for multiple samples
    """
    fig, axes = plt.subplots(1, n_samples, figsize=(20, 6))
    
    for idx, (importance, X_sample) in enumerate(explanations[:n_samples]):
        if idx >= len(axes):
            break
        
        # Sort by absolute importance
        indices = np.argsort(np.abs(importance))[::-1]
        top_k = min(4, len(indices))
        
        top_indices = indices[:top_k]
        top_importance = importance[top_indices]
        top_names = [feature_names[i] for i in top_indices]
        
        colors = ['red' if imp < 0 else 'green' for imp in top_importance]
        
        axes[idx].barh(range(len(top_names)), top_importance, color=colors, alpha=0.7)
        axes[idx].set_yticks(range(len(top_names)))
        axes[idx].set_yticklabels(top_names, fontsize=8)
        axes[idx].set_title(f'Sample {idx}', fontsize=10, fontweight='bold')
        axes[idx].axvline(x=0, color='black', linestyle='--', linewidth=0.5)
        axes[idx].grid(axis='x', alpha=0.3)
    
    plt.suptitle('LIME Explanations for Multiple Samples', 
                fontsize=12, fontweight='bold', y=1.02)
    plt.tight_layout()
    plt.savefig('unit4-transparency-accountability/examples/lime_comparison.png', 
                dpi=300, bbox_inches='tight')
    print("✅ Saved: lime_comparison.png")
    plt.close()

# ============================================================================
# MAIN EXECUTION
# ============================================================================

if __name__ == "__main__":
    print("="*80)
    print("Unit 4 - Example 2: LIME Explanations")
    print("="*80)
    
    # Generate dataset
    print("\nGenerating dataset...")
    df = generate_dataset(n_samples=1000)
    print(f"Dataset shape: {df.shape}")
    
    # Prepare data
    feature_names = ['age', 'income', 'credit_history', 'loan_amount']
    X = df[feature_names].values
    y = df['approved'].values
    
    # Split data
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.3, random_state=42, stratify=y
    )
    
    # Scale features
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    
    # Train model
    print("\nTraining Random Forest model...")
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train_scaled, y_train)
    
    train_acc = accuracy_score(y_train, model.predict(X_train_scaled))
    test_acc = accuracy_score(y_test, model.predict(X_test_scaled))
    print(f"Training Accuracy: {train_acc:.4f}")
    print(f"Test Accuracy: {test_acc:.4f}")
    
    # Generate LIME explanations for multiple samples
    print("\nGenerating LIME explanations...")
    explanations = []
    for i in range(min(10, len(X_test_scaled))):
        X_sample = X_test_scaled[i:i+1]
        explanation, _ = explain_with_lime(
            model, X_sample, X_train_scaled, feature_names, use_library=LIME_AVAILABLE
        )
        
        if isinstance(explanation, np.ndarray):
            explanations.append((explanation, X_test[i:i+1]))
        else:
            # If using LIME library, extract feature importance
            exp_list = explanation.as_list()
            importance = np.zeros(len(feature_names))
            for feature_name, value in exp_list:
                idx = feature_names.index(feature_name)
                importance[idx] = value
            explanations.append((importance, X_test[i:i+1]))
    
    print(f"Generated {len(explanations)} LIME explanations")
    
    # Create visualizations
    print("\n" + "="*80)
    print("Creating Visualizations...")
    print("="*80)
    
    plot_lime_explanation(explanations[0][0], feature_names, explanations[0][1], sample_idx=0)
    plot_lime_comparison(explanations, feature_names, n_samples=5)
    
    # Summary
    print("\n" + "="*80)
    print("SUMMARY")
    print("="*80)
    print("\nKey Takeaways:")
    print("1. LIME provides local, interpretable explanations")
    print("2. LIME approximates complex models with simple linear models locally")
    print("3. LIME works for any black-box model")
    print("4. LIME explanations are instance-specific")
    print("5. LIME helps understand individual predictions")
    print("="*80 + "\n")

