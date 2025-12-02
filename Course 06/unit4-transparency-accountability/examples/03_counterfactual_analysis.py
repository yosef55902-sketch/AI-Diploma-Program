"""
Unit 4: Interpretability, Transparency, and Accountability
Example 3: Counterfactual Analysis

This example demonstrates counterfactual analysis for model interpretability:
- Generating counterfactual examples
- What-if analysis
- Model decision explanations
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

plt.rcParams['font.size'] = 10
plt.rcParams['figure.figsize'] = (14, 8)
sns.set_style("whitegrid")

# ============================================================================
# COUNTERFACTUAL GENERATION
# ============================================================================

def generate_counterfactual(model, X_instance, X_train, feature_names, target_class=1, max_iterations=100):
    """
    Generate counterfactual example by perturbing features
    """
    # Get original prediction
    original_pred = model.predict_proba(X_instance)[0, 1]
    original_class = model.predict(X_instance)[0]
    
    if original_class == target_class:
        return X_instance.copy(), 0, "Already in target class"
    
    # Initialize counterfactual
    counterfactual = X_instance.copy()
    
    # Feature ranges from training data
    feature_ranges = {
        i: (X_train[:, i].min(), X_train[:, i].max())
        for i in range(X_train.shape[1])
    }
    
    # Iteratively modify features
    for iteration in range(max_iterations):
        # Try modifying each feature
        best_change = None
        best_score = original_pred
        
        for feature_idx in range(X_instance.shape[1]):
            # Try increasing feature
            test_cf = counterfactual.copy()
            step = (feature_ranges[feature_idx][1] - feature_ranges[feature_idx][0]) * 0.1
            test_cf[0, feature_idx] = min(
                test_cf[0, feature_idx] + step,
                feature_ranges[feature_idx][1]
            )
            
            new_pred = model.predict_proba(test_cf)[0, 1]
            
            # Check if we're moving toward target class
            if target_class == 1 and new_pred > best_score:
                best_score = new_pred
                best_change = (feature_idx, step)
            elif target_class == 0 and new_pred < best_score:
                best_score = new_pred
                best_change = (feature_idx, -step)
        
        if best_change is None:
            break
        
        # Apply best change
        feature_idx, change = best_change
        counterfactual[0, feature_idx] += change
        counterfactual[0, feature_idx] = np.clip(
            counterfactual[0, feature_idx],
            feature_ranges[feature_idx][0],
            feature_ranges[feature_idx][1]
        )
        
        # Check if we've reached target class
        new_pred = model.predict_proba(counterfactual)[0, 1]
        new_class = model.predict(counterfactual)[0]
        
        if new_class == target_class:
            return counterfactual, iteration + 1, "Target class reached"
    
    return counterfactual, max_iterations, "Max iterations reached"

# ============================================================================
# WHAT-IF ANALYSIS
# ============================================================================

def what_if_analysis(model, X_instance, feature_names, feature_to_change, values_to_test):
    """
    Perform what-if analysis by changing a single feature
    """
    results = []
    
    for value in values_to_test:
        X_test = X_instance.copy()
        feature_idx = feature_names.index(feature_to_change)
        X_test[0, feature_idx] = value
        
        pred_proba = model.predict_proba(X_test)[0, 1]
        pred_class = model.predict(X_test)[0]
        
        results.append({
            'value': value,
            'prediction_probability': pred_proba,
            'prediction_class': pred_class
        })
    
    return pd.DataFrame(results)

# ============================================================================
# GENERATE DATASET
# ============================================================================

def generate_dataset(n_samples=1000):
    """
    Generate synthetic dataset for counterfactual analysis
    """
    np.random.seed(42)
    
    age = np.random.randint(25, 70, n_samples)
    income = np.random.normal(60000, 25000, n_samples)
    credit_score = np.random.normal(650, 100, n_samples)
    debt_ratio = np.random.uniform(0.1, 0.6, n_samples)
    
    approval_prob = (credit_score / 850 * 0.4 +
                     (income / 100000) * 0.3 +
                     (1 - debt_ratio) * 0.2 +
                     (age / 70) * 0.1 +
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
# VISUALIZATIONS
# ============================================================================

def plot_counterfactual_comparison(X_original, X_counterfactual, feature_names, original_pred, cf_pred):
    """
    Plot comparison between original and counterfactual
    """
    fig, axes = plt.subplots(1, 2, figsize=(16, 6))
    
    # Feature comparison
    features = feature_names
    original_values = X_original[0]
    cf_values = X_counterfactual[0]
    changes = cf_values - original_values
    
    x = np.arange(len(features))
    width = 0.35
    
    axes[0].bar(x - width/2, original_values, width, label='Original', alpha=0.8, color='#e74c3c')
    axes[0].bar(x + width/2, cf_values, width, label='Counterfactual', alpha=0.8, color='#2ecc71')
    axes[0].set_xlabel('Features', fontsize=11, fontweight='bold')
    axes[0].set_ylabel('Feature Values', fontsize=11, fontweight='bold')
    axes[0].set_title('Original vs Counterfactual Feature Values', fontsize=12, fontweight='bold')
    axes[0].set_xticks(x)
    axes[0].set_xticklabels(features, rotation=15)
    axes[0].legend()
    axes[0].grid(axis='y', alpha=0.3)
    
    # Feature changes
    colors = ['green' if c > 0 else 'red' for c in changes]
    axes[1].barh(features, changes, color=colors, alpha=0.7)
    axes[1].set_xlabel('Change in Feature Value', fontsize=11, fontweight='bold')
    axes[1].set_title('Feature Changes to Achieve Counterfactual', fontsize=12, fontweight='bold')
    axes[1].axvline(x=0, color='black', linestyle='--', linewidth=1)
    axes[1].grid(axis='x', alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('unit4-transparency-accountability/examples/counterfactual_comparison.png', 
                dpi=300, bbox_inches='tight')
    print("✅ Saved: counterfactual_comparison.png")
    plt.close()

def plot_what_if_analysis(what_if_df, feature_name):
    """
    Plot what-if analysis results
    """
    fig, ax = plt.subplots(figsize=(12, 6))
    
    ax.plot(what_if_df['value'], what_if_df['prediction_probability'], 
           marker='o', linewidth=2, markersize=8, color='#3498db')
    ax.axhline(y=0.5, color='red', linestyle='--', linewidth=1, label='Decision Threshold')
    ax.set_xlabel(feature_name, fontsize=11, fontweight='bold')
    ax.set_ylabel('Prediction Probability', fontsize=11, fontweight='bold')
    ax.set_title(f'What-If Analysis: {feature_name}', fontsize=12, fontweight='bold')
    ax.grid(alpha=0.3)
    ax.legend()
    
    plt.tight_layout()
    plt.savefig('unit4-transparency-accountability/examples/what_if_analysis.png', 
                dpi=300, bbox_inches='tight')
    print("✅ Saved: what_if_analysis.png")
    plt.close()

# ============================================================================
# MAIN EXECUTION
# ============================================================================

if __name__ == "__main__":
    print("="*80)
    print("Unit 4 - Example 3: Counterfactual Analysis")
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
    
    test_acc = accuracy_score(y_test, model.predict(X_test_scaled))
    print(f"Test Accuracy: {test_acc:.4f}")
    
    # Find a rejected instance to generate counterfactual
    rejected_indices = np.where(model.predict(X_test_scaled) == 0)[0]
    if len(rejected_indices) > 0:
        sample_idx = rejected_indices[0]
        X_instance = X_test_scaled[sample_idx:sample_idx+1]
        
        print(f"\nOriginal instance (rejected):")
        print(f"  Features: {dict(zip(feature_names, X_test[sample_idx]))}")
        print(f"  Prediction probability: {model.predict_proba(X_instance)[0, 1]:.4f}")
        print(f"  Prediction: {model.predict(X_instance)[0]}")
        
        # Generate counterfactual
        print("\nGenerating counterfactual (to get approved)...")
        X_counterfactual, iterations, status = generate_counterfactual(
            model, X_instance, X_train_scaled, feature_names, target_class=1
        )
        
        print(f"Counterfactual found after {iterations} iterations: {status}")
        print(f"  Prediction probability: {model.predict_proba(X_counterfactual)[0, 1]:.4f}")
        print(f"  Prediction: {model.predict(X_counterfactual)[0]}")
        
        # What-if analysis
        print("\nPerforming what-if analysis on credit_score...")
        credit_scores = np.linspace(500, 800, 50)
        what_if_df = what_if_analysis(
            model, X_instance, feature_names, 'credit_score', credit_scores
        )
        
        # Create visualizations
        print("\n" + "="*80)
        print("Creating Visualizations...")
        print("="*80)
        
        original_pred = model.predict_proba(X_instance)[0, 1]
        cf_pred = model.predict_proba(X_counterfactual)[0, 1]
        plot_counterfactual_comparison(X_instance, X_counterfactual, feature_names, 
                                      original_pred, cf_pred)
        plot_what_if_analysis(what_if_df, 'credit_score')
    
    # Summary
    print("\n" + "="*80)
    print("SUMMARY")
    print("="*80)
    print("\nKey Takeaways:")
    print("1. Counterfactuals show what needs to change to get a different outcome")
    print("2. What-if analysis explores how changes in features affect predictions")
    print("3. Counterfactuals help explain model decisions")
    print("4. Counterfactuals are useful for actionable insights")
    print("5. Counterfactual analysis improves model transparency")
    print("="*80 + "\n")

