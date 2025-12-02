"""
Unit 2: Bias, Justice, and Discrimination in AI
Exercise 2: Bias Mitigation Techniques

This exercise requires you to implement and compare different bias mitigation techniques.
"""

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score
from fairlearn.metrics import demographic_parity_difference, equalized_odds_difference

# ============================================================================
# TASK 1: Generate Biased Dataset
# ============================================================================

def generate_biased_dataset(n_samples=2000):
    """
    TODO: Generate a synthetic dataset with bias.
    
    Requirements:
    - Create a dataset with features and a sensitive attribute (e.g., gender: 0 or 1)
    - Introduce bias such that one group has lower probability of positive outcome
    - Return a DataFrame with columns: feature1, feature2, sensitive, target
    """
    np.random.seed(42)
    
    # TODO: Your code here
    # Hint: Use np.random functions to generate features
    # Hint: Make the target depend on features but add bias based on sensitive attribute
    
    pass

# ============================================================================
# TASK 2: Implement Pre-processing Bias Mitigation
# ============================================================================

def preprocess_reweighing(X_train, y_train, sensitive_train):
    """
    TODO: Implement reweighing technique.
    
    Requirements:
    - Calculate weights to balance representation across groups
    - Return array of weights for each training sample
    """
    # TODO: Your code here
    # Hint: Calculate weights inversely proportional to group size
    
    pass

# ============================================================================
# TASK 3: Train Models with Different Mitigation Techniques
# ============================================================================

def train_baseline_model(X_train, y_train):
    """
    TODO: Train a baseline model without any bias mitigation.
    """
    # TODO: Your code here
    # Hint: Use RandomForestClassifier
    
    pass

def train_reweighed_model(X_train, y_train, sensitive_train):
    """
    TODO: Train a model using reweighing technique.
    """
    # TODO: Your code here
    # Hint: Use the preprocess_reweighing function and pass weights to fit()
    
    pass

# ============================================================================
# TASK 4: Evaluate Fairness Metrics
# ============================================================================

def evaluate_fairness(y_true, y_pred, sensitive):
    """
    TODO: Evaluate fairness metrics.
    
    Requirements:
    - Calculate demographic parity difference
    - Calculate equalized odds difference
    - Calculate accuracy
    - Return a dictionary with these metrics
    """
    # TODO: Your code here
    # Hint: Use fairlearn.metrics functions
    
    pass

# ============================================================================
# TASK 5: Compare Techniques
# ============================================================================

def compare_mitigation_techniques(df):
    """
    TODO: Compare baseline vs reweighing techniques.
    
    Requirements:
    - Split data into train/test
    - Train baseline and reweighed models
    - Evaluate fairness metrics for both
    - Print comparison results
    """
    # TODO: Your code here
    
    pass

# ============================================================================
# MAIN EXECUTION
# ============================================================================

if __name__ == "__main__":
    print("="*80)
    print("Unit 2 - Exercise 2: Bias Mitigation Techniques")
    print("="*80)
    
    # Generate dataset
    print("\nTask 1: Generating biased dataset...")
    df = generate_biased_dataset()
    print(f"Dataset shape: {df.shape}")
    print(f"Sensitive attribute distribution:")
    print(df['sensitive'].value_counts())
    
    # Compare techniques
    print("\nTask 5: Comparing mitigation techniques...")
    compare_mitigation_techniques(df)
    
    print("\n" + "="*80)
    print("Exercise completed! Check your results against the solution.")
    print("="*80)

