"""
Exercise 01: Optimization Algorithms

This exercise helps you understand different optimization algorithms
used in machine learning.

Instructions:
1. Implement different optimizers
2. Compare their performance
3. Understand when to use each
"""

import numpy as np


class SimpleGDOptimizer:
    """
    Simple Gradient Descent optimizer.
    
    WHY: Simple and works for convex problems
    HOW: params = params - lr * gradient
    """
    def __init__(self, lr=0.01):
        self.lr = lr
    
    def update(self, params, grads):
        """
        Update parameters using simple gradient descent.
        
        Args:
            params: Current parameters
            grads: Gradients
            
        Returns:
            Updated parameters
        """
        # TODO: Implement simple gradient descent update
        pass


class MomentumOptimizer:
    """
    Gradient descent with momentum.
    
    WHY: Remembers previous gradients for smoother path
    HOW: Uses moving average of gradients
    """
    def __init__(self, lr=0.01, momentum=0.9):
        self.lr = lr
        self.momentum = momentum
        self.velocity = None
    
    def update(self, params, grads):
        """
        Update parameters using momentum.
        
        Args:
            params: Current parameters
            grads: Gradients
            
        Returns:
            Updated parameters
        """
        # TODO: Initialize velocity if first call
        # TODO: Update velocity: v = momentum * v + lr * grads
        # TODO: Update params: params = params - velocity
        pass


def compare_optimizers(loss_func, grad_func, initial_params, optimizers, iterations=100):
    """
    Compare different optimizers on the same problem.
    
    Args:
        loss_func: Loss function
        grad_func: Gradient function
        initial_params: Starting parameters
        optimizers: Dictionary of {name: optimizer}
        iterations: Number of iterations
        
    Returns:
        Dictionary of {optimizer_name: final_params}
    """
    results = {}
    
    # TODO: For each optimizer:
    #   1. Start with initial_params
    #   2. Run for 'iterations' steps
    #   3. Store final parameters
    
    return results


# Test your solutions
if __name__ == "__main__":
    print("Testing Exercise 01: Optimization Algorithms")
    print("=" * 60)
    
    # Test 1: Simple GD
    print("\n1. Testing SimpleGDOptimizer:")
    def loss(x):
        return (x - 3)**2
    
    def grad(x):
        return 2 * (x - 3)
    
    optimizer = SimpleGDOptimizer(lr=0.1)
    x = 5.0
    for i in range(20):
        g = grad(x)
        x = optimizer.update(x, g)
    
    print(f"   Starting: 5.0, Final: {x:.4f}, Target: 3.0")
    assert abs(x - 3) < 0.5, "Should converge close to 3"
    print("   ✅ Passed!")
    
    # Test 2: Momentum
    print("\n2. Testing MomentumOptimizer:")
    momentum_opt = MomentumOptimizer(lr=0.1, momentum=0.9)
    x = 5.0
    for i in range(20):
        g = grad(x)
        x = momentum_opt.update(x, g)
    
    print(f"   Starting: 5.0, Final: {x:.4f}, Target: 3.0")
    assert abs(x - 3) < 0.5, "Should converge close to 3"
    print("   ✅ Passed!")
    
    print("\n" + "=" * 60)
    print("🎉 All tests passed!")
