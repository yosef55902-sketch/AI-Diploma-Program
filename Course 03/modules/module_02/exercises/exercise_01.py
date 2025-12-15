"""
Exercise 01: Derivatives and Gradients

This exercise helps you understand how derivatives and gradients work,
which are fundamental for training machine learning models.

Instructions:
1. Complete the functions below
2. Understand how derivatives relate to optimization
3. Test your solutions
"""

import numpy as np
from scipy.misc import derivative


def compute_derivative(func, x, h=1e-6):
    """
    Compute the derivative of a function at a point.
    
    WHY: Derivatives tell us the direction to minimize loss
    HOW: Use the definition of derivative: (f(x+h) - f(x)) / h
    
    Args:
        func: Function to differentiate
        x: Point at which to compute derivative
        h: Small step size (default: 1e-6)
        
    Returns:
        Derivative value at x
    """
    # TODO: Implement numerical derivative
    # Formula: (f(x+h) - f(x)) / h
    pass


def compute_gradient(func, point):
    """
    Compute the gradient of a multivariable function.
    
    WHY: ML models have many parameters - need direction for each
    HOW: Gradient = vector of partial derivatives
    
    Args:
        func: Function f(x, y) that takes a point [x, y]
        point: Point [x, y] at which to compute gradient
        
    Returns:
        Gradient vector [∂f/∂x, ∂f/∂y]
    """
    # TODO: Compute partial derivatives
    # Use compute_derivative for each variable
    h = 1e-6
    pass


def gradient_descent_step(func, x, learning_rate=0.1):
    """
    Perform one step of gradient descent.
    
    WHY: Find optimal parameters that minimize loss
    HOW: Move in direction opposite to gradient
    
    Args:
        func: Function to minimize (e.g., loss function)
        x: Current parameter value
        learning_rate: Step size
        
    Returns:
        Updated parameter value
    """
    # TODO: 
    # 1. Compute gradient at current point
    # 2. Move in opposite direction: x_new = x - lr * gradient
    pass


# Test your solutions
if __name__ == "__main__":
    print("Testing Exercise 01: Derivatives and Gradients")
    print("=" * 60)
    
    # Test 1: Derivative
    print("\n1. Testing compute_derivative:")
    def f(x):
        return x**2 + 3*x + 2
    
    x0 = 2.0
    deriv = compute_derivative(f, x0)
    expected = 2*x0 + 3  # d/dx(x² + 3x + 2) = 2x + 3
    print(f"   Function: f(x) = x² + 3x + 2")
    print(f"   At x = {x0}:")
    print(f"   Computed derivative: {deriv:.4f}")
    print(f"   Expected: {expected:.4f}")
    assert abs(deriv - expected) < 0.01, "Derivative incorrect"
    print("   ✅ Passed!")
    
    # Test 2: Gradient
    print("\n2. Testing compute_gradient:")
    def multivariable_func(point):
        x, y = point
        return x**2 + y**2 + x*y
    
    point = np.array([1.0, 2.0])
    grad = compute_gradient(multivariable_func, point)
    expected = np.array([2*point[0] + point[1], 2*point[1] + point[0]])
    print(f"   Function: f(x, y) = x² + y² + xy")
    print(f"   At point ({point[0]}, {point[1]}):")
    print(f"   Computed gradient: {grad}")
    print(f"   Expected: {expected}")
    assert np.allclose(grad, expected, atol=0.1), "Gradient incorrect"
    print("   ✅ Passed!")
    
    # Test 3: Gradient descent
    print("\n3. Testing gradient_descent_step:")
    def loss_func(x):
        return (x - 3)**2  # Minimum at x = 3
    
    x = 5.0
    x_new = gradient_descent_step(loss_func, x, learning_rate=0.1)
    print(f"   Loss function: f(x) = (x - 3)²")
    print(f"   Starting at x = {x}")
    print(f"   After one step: x = {x_new:.4f}")
    print(f"   Expected: x should move closer to 3")
    assert abs(x_new - 3) < abs(x - 3), "Should move toward minimum"
    print("   ✅ Passed!")
    
    print("\n" + "=" * 60)
    print("🎉 All tests passed!")
