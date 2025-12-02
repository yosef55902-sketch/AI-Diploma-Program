"""
Unit 4: Interpretability, Transparency, and Accountability
Example 5: Human-in-the-Loop (HITL) Approaches

This example demonstrates human-in-the-loop approaches for AI fairness evaluation.
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score
from fairlearn.metrics import demographic_parity_difference
import warnings
warnings.filterwarnings('ignore')

plt.rcParams['font.size'] = 10
plt.rcParams['figure.figsize'] = (14, 8)
sns.set_style("whitegrid")

def generate_dataset(n_samples=1000):
    np.random.seed(42)
    sensitive = np.random.choice([0, 1], n_samples, p=[0.6, 0.4])
    X1 = np.random.normal(0, 1, n_samples)
    X2 = np.random.normal(0, 1, n_samples)
    y = (0.4 * X1 + 0.3 * X2 + np.random.normal(0, 0.1, n_samples) > 0).astype(int)
    return pd.DataFrame({'feature1': X1, 'feature2': X2, 'sensitive': sensitive, 'target': y})

def hitl_fairness_evaluation(model, X_test, y_test, sensitive_test, uncertainty_threshold=0.1):
    y_pred_proba = model.predict_proba(X_test)[:, 1]
    y_pred = (y_pred_proba > 0.5).astype(int)
    uncertainty = np.abs(y_pred_proba - 0.5)
    uncertain_mask = uncertainty < uncertainty_threshold
    
    human_reviewed = y_pred.copy()
    if uncertain_mask.sum() > 0:
        human_predictions = y_test[uncertain_mask].copy()
        human_reviewed[uncertain_mask] = human_predictions
    
    return {
        'automated': y_pred,
        'hitl': human_reviewed,
        'uncertain_count': uncertain_mask.sum(),
        'uncertain_mask': uncertain_mask
    }

if __name__ == "__main__":
    print("="*80)
    print("Unit 4 - Example 5: Human-in-the-Loop Approaches")
    print("="*80)
    
    df = generate_dataset()
    X = df[['feature1', 'feature2']].values
    y = df['target'].values
    sensitive = df['sensitive'].values
    
    X_train, X_test, y_train, y_test, sensitive_train, sensitive_test = train_test_split(
        X, y, sensitive, test_size=0.3, random_state=42, stratify=y
    )
    
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train_scaled, y_train)
    
    results = hitl_fairness_evaluation(model, X_test_scaled, y_test, sensitive_test)
    
    auto_acc = accuracy_score(y_test, results['automated'])
    hitl_acc = accuracy_score(y_test, results['hitl'])
    auto_dp = abs(demographic_parity_difference(y_test, results['automated'], sensitive_features=sensitive_test))
    hitl_dp = abs(demographic_parity_difference(y_test, results['hitl'], sensitive_features=sensitive_test))
    
    print(f"\nAutomated Model:")
    print(f"  Accuracy: {auto_acc:.4f}")
    print(f"  Demographic Parity Difference: {auto_dp:.4f}")
    print(f"\nHITL Model:")
    print(f"  Accuracy: {hitl_acc:.4f}")
    print(f"  Demographic Parity Difference: {hitl_dp:.4f}")
    print(f"  Human Reviews: {results['uncertain_count']}")
    
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))
    axes[0].bar(['Automated', 'HITL'], [auto_acc, hitl_acc], color=['#e74c3c', '#2ecc71'])
    axes[0].set_title('Accuracy Comparison', fontweight='bold')
    axes[0].set_ylabel('Accuracy')
    axes[1].bar(['Automated', 'HITL'], [auto_dp, hitl_dp], color=['#e74c3c', '#2ecc71'])
    axes[1].set_title('Fairness Comparison', fontweight='bold')
    axes[1].set_ylabel('Demographic Parity Difference')
    plt.tight_layout()
    plt.savefig('unit4-transparency-accountability/examples/hitl_comparison.png', dpi=300, bbox_inches='tight')
    print("\n✅ Saved: hitl_comparison.png")
    plt.close()
    
    print("\n✅ Example completed!")

