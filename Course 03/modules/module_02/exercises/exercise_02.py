"""
Exercise 02: Gradient Descent Implementation

This exercise helps you implement gradient descent, the fundamental
optimization algorithm used in machine learning.

Instructions:
1. Implement gradient descent from scratch
2. Understand how learning rate affects convergence
3. Visualize the optimization process
"""

import numpy as np


def gradient_descent(func, gradient_func, initial_x, learning_rate=0.1, iterations=100):
    """
    Implement gradient descent to minimize a function.
    
    WHY: Find optimal parameters that minimize loss
    HOW: Iteratively move in direction opposite to gradient
    
    Args:
        func: Function to minimize
        gradient_func: Function that computes gradient
        initial_x: Starting point
        learning_rate: Step size
        iterations: Number of iterations
        
    Returns:
        Tuple of (final_x, history) where history contains all x values
    """
    x = initial_x
    history = [x]
    
    # TODO: Implement gradient descent loop
    # For each iteration:
    #   1. Compute gradient at current point
    #   2. Update: x = x - learning_rate * gradient
    #   3. Store x in history
    
    return x, history


def analyze_learning_rate(func, gradient_func, initial_x, learning_rates, iterations=50):
    """
    Analyze how different learning rates affect convergence.
    
    WHY: Learning rate is crucial - too small = slow, too large = divergence
    HOW: Try different learning rates and see convergence behavior
    
    Args:
        func: Function to minimize
        gradient_func: Gradient function
        initial_x: Starting point
        learning_rates: List of learning rates to try
        iterations: Number of iterations
        
    Returns:
        Dictionary mapping learning rate to final value
    """
    results = {}
    
    # TODO: For each learning rate, run gradient descent
    # Store the final value in results dictionary
    
    return results


# Test your solutions
if __name__ == "__main__":
    print("Testing Exercise 02: Gradient Descent")
    print("=" * 60)
    
    # Test 1: Gradient descent
    print("\n1. Testing gradient_descent:")
    def f(x):
        return (x - 3)**2  # Minimum at x = 3
    
    def grad_f(x):
        return 2 * (x - 3)  # Gradient of (x-3)²
    
    initial_x = 5.0
    final_x, history = gradient_descent(f, grad_f, initial_x, learning_rate=0.1, iterations=20)
    
    print(f"   Function: f(x) = (x - 3)² (minimum at x = 3)")
    print(f"   Starting at: {initial_x}")
    print(f"   Final value: {final_x:.4f}")
    print(f"   Expected: close to 3.0")
    print(f"   Converged: {abs(final_x - 3) < 0.1}")
    assert abs(final_x - 3) < 0.5, "Should converge close to minimum"
    print("   ✅ Passed!")
    
    # Test 2: Learning rate analysis
    print("\n2. Testing analyze_learning_rate:")
    learning_rates = [0.01, 0.1, 0.5, 1.0]
    results = analyze_learning_rate(f, grad_f, initial_x, learning_rates, iterations=30)
    
    print(f"   Learning Rate Analysis:")
    for lr, final_val in results.items():
        converged = abs(final_val - 3) < 0.5
        status = "✅ Converged" if converged else "❌ Diverged"
        print(f"   LR = {lr:.2f}: Final x = {final_val:.4f} {status}")
    
    print("\n" + "=" * 60)
    print("🎉 All tests passed!")

