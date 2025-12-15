"""
Exercise 02: Statistical Measures and Model Evaluation

This exercise helps you understand statistical measures used to
evaluate machine learning models.

Instructions:
1. Implement statistical evaluation functions
2. Understand different metrics
3. Apply to model evaluation
"""

import numpy as np


def calculate_mse(predictions, targets):
    """
    Calculate Mean Squared Error.
    
    WHY: Penalizes large errors more (for regression)
    HOW: Average of squared differences
    
    Args:
        predictions: Model predictions
        targets: True values
        
    Returns:
        MSE value
    """
    # TODO: Calculate MSE
    # Formula: mean((predictions - targets)^2)
    pass


def calculate_rmse(predictions, targets):
    """
    Calculate Root Mean Squared Error.
    
    WHY: Same units as target variable, easier to interpret
    HOW: Square root of MSE
    
    Args:
        predictions: Model predictions
        targets: True values
        
    Returns:
        RMSE value
    """
    # TODO: Calculate RMSE
    # Formula: sqrt(MSE)
    pass


def calculate_r2_score(predictions, targets):
    """
    Calculate R² (coefficient of determination).
    
    WHY: Shows how much variance is explained by model
    HOW: 1 - (SS_res / SS_tot)
    
    Args:
        predictions: Model predictions
        targets: True values
        
    Returns:
        R² score (between -∞ and 1, higher is better)
    """
    # TODO: Calculate R²
    # Formula: 1 - sum((targets - predictions)^2) / sum((targets - mean(targets))^2)
    pass


def evaluate_model(predictions, targets):
    """
    Comprehensive model evaluation.
    
    Args:
        predictions: Model predictions
        targets: True values
        
    Returns:
        Dictionary with all metrics
    """
    # TODO: Calculate all metrics and return as dictionary
    pass


# Test your solutions
if __name__ == "__main__":
    print("Testing Exercise 02: Statistical Measures")
    print("=" * 60)
    
    # Test data
    predictions = np.array([2.1, 3.2, 4.0, 5.1, 6.0])
    targets = np.array([2.0, 3.0, 4.0, 5.0, 6.0])
    
    # Test 1: MSE
    print("\n1. Testing calculate_mse:")
    mse = calculate_mse(predictions, targets)
    expected = np.mean((predictions - targets)**2)
    print(f"   MSE: {mse:.4f}")
    print(f"   Expected: {expected:.4f}")
    assert np.isclose(mse, expected), "MSE incorrect"
    print("   ✅ Passed!")
    
    # Test 2: RMSE
    print("\n2. Testing calculate_rmse:")
    rmse = calculate_rmse(predictions, targets)
    expected = np.sqrt(expected)
    print(f"   RMSE: {rmse:.4f}")
    print(f"   Expected: {expected:.4f}")
    assert np.isclose(rmse, expected), "RMSE incorrect"
    print("   ✅ Passed!")
    
    # Test 3: R²
    print("\n3. Testing calculate_r2_score:")
    r2 = calculate_r2_score(predictions, targets)
    print(f"   R²: {r2:.4f}")
    print(f"   Expected: close to 1.0 (perfect predictions)")
    assert r2 > 0.9, "R² should be high for good predictions"
    print("   ✅ Passed!")
    
    # Test 4: Comprehensive evaluation
    print("\n4. Testing evaluate_model:")
    metrics = evaluate_model(predictions, targets)
    print(f"   All metrics: {metrics}")
    assert 'MSE' in metrics and 'RMSE' in metrics and 'R²' in metrics
    print("   ✅ Passed!")
    
    print("\n" + "=" * 60)
    print("🎉 All tests passed!")

