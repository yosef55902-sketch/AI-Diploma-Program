"""
Unit 4: Interpretability, Transparency, and Accountability
Example 1: SHAP Explanations

This example demonstrates SHAP (SHapley Additive exPlanations) for model interpretability:
- SHAP values calculation
- Global and local explanations
- Feature importance visualization
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score
import warnings
warnings.filterwarnings('ignore')

# Try to import SHAP, use simplified version if not available
try:
    import shap
    SHAP_AVAILABLE = True
except ImportError:
    SHAP_AVAILABLE = False
    print("Note: SHAP library not available. Using simplified SHAP implementation.")

plt.rcParams['font.size'] = 10
plt.rcParams['figure.figsize'] = (14, 8)
sns.set_style("whitegrid")

# ============================================================================
# SIMPLIFIED SHAP IMPLEMENTATION (if SHAP not available)
# ============================================================================

def calculate_shap_values_simple(model, X, feature_names):
    """
    Simplified SHAP value calculation using permutation importance
    """
    baseline_pred = model.predict_proba(X)[:, 1].mean()
    shap_values = []
    
    for i in range(len(X)):
        sample = X[i:i+1]
        base_pred = model.predict_proba(sample)[0, 1]
        
        sample_shap = []
        for j in range(X.shape[1]):
            # Permute feature j
            X_permuted = X.copy()
            X_permuted[:, j] = sample[0, j]
            perm_pred = model.predict_proba(X_permuted)[:, 1].mean()
            
            # SHAP value approximation
            shap_val = base_pred - perm_pred
            sample_shap.append(shap_val)
        
        shap_values.append(sample_shap)
    
    return np.array(shap_values)

# ============================================================================
# GENERATE DATASET
# ============================================================================

def generate_dataset(n_samples=1000):
    """
    Generate synthetic dataset for SHAP demonstration
    """
    np.random.seed(42)
    
    # Features
    age = np.random.randint(18, 80, n_samples)
    income = np.random.normal(50000, 20000, n_samples)
    credit_score = np.random.normal(650, 100, n_samples)
    debt_ratio = np.random.uniform(0.1, 0.6, n_samples)
    
    # Target (loan approval)
    approval_prob = (credit_score / 850 * 0.4 +
                     (income / 100000) * 0.3 +
                     (1 - debt_ratio) * 0.2 +
                     (age / 80) * 0.1 +
                     np.random.normal(0, 0.05, n_samples))
    approval = (approval_prob > 0.5).astype(int)
    
    df = pd.DataFrame({
        'age': age,
        'income': income,
        'credit_score': credit_score,
        'debt_ratio': debt_ratio,
        'approved': approval
    })
    
    return df

# ============================================================================
# SHAP EXPLANATIONS
# ============================================================================

def explain_with_shap(model, X, feature_names, use_library=True):
    """
    Generate SHAP explanations for the model
    """
    if SHAP_AVAILABLE and use_library:
        # Use actual SHAP library
        explainer = shap.TreeExplainer(model)
        shap_values = explainer.shap_values(X)
        
        if isinstance(shap_values, list):
            shap_values = shap_values[1]  # For binary classification, use positive class
        
        return shap_values, explainer
    else:
        # Use simplified implementation
        shap_values = calculate_shap_values_simple(model, X, feature_names)
        return shap_values, None

# ============================================================================
# VISUALIZATIONS
# ============================================================================

def plot_shap_summary(shap_values, X, feature_names):
    """
    Plot SHAP summary plot
    """
    fig, ax = plt.subplots(figsize=(12, 8))
    
    # Calculate mean absolute SHAP values for feature importance
    mean_shap = np.abs(shap_values).mean(axis=0)
    
    # Sort by importance
    indices = np.argsort(mean_shap)
    
    y_pos = np.arange(len(feature_names))
    colors = plt.cm.RdYlGn(mean_shap / mean_shap.max())
    
    ax.barh(y_pos, mean_shap[indices], color=colors[indices])
    ax.set_yticks(y_pos)
    ax.set_yticklabels([feature_names[i] for i in indices])
    ax.set_xlabel('Mean |SHAP Value|', fontsize=11, fontweight='bold')
    ax.set_title('SHAP Feature Importance Summary', fontsize=12, fontweight='bold')
    ax.grid(axis='x', alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('unit4-transparency-accountability/examples/shap_summary.png', 
                dpi=300, bbox_inches='tight')
    print("✅ Saved: shap_summary.png")
    plt.close()

def plot_shap_waterfall(shap_values, X, feature_names, sample_idx=0):
    """
    Plot SHAP waterfall plot for a single prediction
    """
    sample_shap = shap_values[sample_idx]
    sample_values = X[sample_idx]
    
    # Sort by absolute SHAP value
    indices = np.argsort(np.abs(sample_shap))[::-1]
    
    fig, ax = plt.subplots(figsize=(12, 8))
    
    # Calculate cumulative SHAP values
    cumulative = np.cumsum([0] + list(sample_shap[indices]))
    
    # Plot waterfall
    for i in range(len(indices)):
        idx = indices[i]
        color = 'red' if sample_shap[idx] < 0 else 'green'
        ax.barh(i, sample_shap[idx], left=cumulative[i], color=color, alpha=0.7)
        ax.text(cumulative[i] + sample_shap[idx]/2, i, 
               f'{feature_names[idx]}\n={sample_values[idx]:.2f}',
               ha='center', va='center', fontsize=9)
    
    ax.set_yticks(range(len(indices)))
    ax.set_yticklabels([feature_names[i] for i in indices])
    ax.set_xlabel('SHAP Value', fontsize=11, fontweight='bold')
    ax.set_title(f'SHAP Waterfall Plot (Sample {sample_idx})', 
                fontsize=12, fontweight='bold')
    ax.axvline(x=0, color='black', linestyle='--', linewidth=1)
    ax.grid(axis='x', alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('unit4-transparency-accountability/examples/shap_waterfall.png', 
                dpi=300, bbox_inches='tight')
    print("✅ Saved: shap_waterfall.png")
    plt.close()

def plot_shap_dependence(shap_values, X, feature_names, feature_idx=0):
    """
    Plot SHAP dependence plot for a specific feature
    """
    fig, ax = plt.subplots(figsize=(10, 6))
    
    feature_values = X[:, feature_idx]
    feature_shap = shap_values[:, feature_idx]
    
    scatter = ax.scatter(feature_values, feature_shap, alpha=0.5, c=feature_shap, 
                        cmap='RdBu_r', s=30)
    ax.set_xlabel(feature_names[feature_idx], fontsize=11, fontweight='bold')
    ax.set_ylabel('SHAP Value', fontsize=11, fontweight='bold')
    ax.set_title(f'SHAP Dependence Plot: {feature_names[feature_idx]}', 
                fontsize=12, fontweight='bold')
    ax.axhline(y=0, color='black', linestyle='--', linewidth=1)
    ax.grid(alpha=0.3)
    plt.colorbar(scatter, ax=ax, label='SHAP Value')
    
    plt.tight_layout()
    plt.savefig('unit4-transparency-accountability/examples/shap_dependence.png', 
                dpi=300, bbox_inches='tight')
    print("✅ Saved: shap_dependence.png")
    plt.close()

# ============================================================================
# MAIN EXECUTION
# ============================================================================

if __name__ == "__main__":
    print("="*80)
    print("Unit 4 - Example 1: SHAP Explanations")
    print("="*80)
    
    # Generate dataset
    print("\nGenerating dataset...")
    df = generate_dataset(n_samples=1000)
    print(f"Dataset shape: {df.shape}")
    
    # Prepare data
    feature_names = ['age', 'income', 'credit_score', 'debt_ratio']
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
    
    # Calculate SHAP values
    print("\nCalculating SHAP values...")
    shap_values, explainer = explain_with_shap(
        model, X_test_scaled[:100], feature_names, use_library=SHAP_AVAILABLE
    )
    print(f"SHAP values shape: {shap_values.shape}")
    
    # Create visualizations
    print("\n" + "="*80)
    print("Creating Visualizations...")
    print("="*80)
    
    plot_shap_summary(shap_values, X_test_scaled[:100], feature_names)
    plot_shap_waterfall(shap_values, X_test_scaled[:100], feature_names, sample_idx=0)
    plot_shap_dependence(shap_values, X_test_scaled[:100], feature_names, feature_idx=2)
    
    # Summary
    print("\n" + "="*80)
    print("SUMMARY")
    print("="*80)
    print("\nKey Takeaways:")
    print("1. SHAP values explain individual predictions")
    print("2. SHAP summary shows global feature importance")
    print("3. Waterfall plots show how features contribute to a specific prediction")
    print("4. Dependence plots show how SHAP values vary with feature values")
    print("5. SHAP provides model-agnostic explanations")
    print("="*80 + "\n")

