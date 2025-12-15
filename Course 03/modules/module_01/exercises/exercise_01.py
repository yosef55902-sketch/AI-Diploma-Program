"""
Exercise 01: Vector and Matrix Operations

This exercise helps you practice fundamental linear algebra operations that are
essential for machine learning.

Instructions:
1. Complete the functions below
2. Test your solutions with the provided test cases
3. Compare with the solution in solutions/solution_01.py
"""

import numpy as np


def create_data_matrix(samples, features):
    """
    Create a data matrix representing ML data.
    
    In ML, data is organized as a matrix where:
    - Each row = one data point (sample)
    - Each column = one feature
    
    Args:
        samples: Number of data points (rows)
        features: Number of features (columns)
        
    Returns:
        A matrix of shape (samples, features) with random values
    """
    # TODO: Create a matrix with the specified shape
    # Use np.random.randn() to generate random values
    pass


def compute_dot_product(v1, v2):
    """
    Compute the dot product of two vectors.
    
    The dot product is used in neural networks for weighted sums.
    
    Args:
        v1: First vector (numpy array)
        v2: Second vector (numpy array)
        
    Returns:
        The dot product (scalar)
    """
    # TODO: Compute dot product using np.dot() or v1 @ v2
    pass


def matrix_multiplication(A, B):
    """
    Perform matrix multiplication.
    
    This is the core operation in neural network layers.
    
    Args:
        A: First matrix (n, m)
        B: Second matrix (m, p)
        
    Returns:
        Result matrix (n, p)
    """
    # TODO: Perform matrix multiplication
    # Remember: A @ B or np.dot(A, B)
    pass


def compute_transpose(matrix):
    """
    Compute the transpose of a matrix.
    
    Transpose is used when computing gradients in ML.
    
    Args:
        matrix: Input matrix
        
    Returns:
        Transposed matrix
    """
    # TODO: Compute transpose using .T or np.transpose()
    pass


# Test your solutions
if __name__ == "__main__":
    print("Testing Exercise 01: Vector and Matrix Operations")
    print("=" * 60)
    
    # Test 1: Create data matrix
    print("\n1. Testing create_data_matrix:")
    data = create_data_matrix(5, 3)
    print(f"   Created matrix shape: {data.shape}")
    print(f"   Expected: (5, 3)")
    assert data.shape == (5, 3), "Shape should be (5, 3)"
    print("   ✅ Passed!")
    
    # Test 2: Dot product
    print("\n2. Testing compute_dot_product:")
    v1 = np.array([1, 2, 3])
    v2 = np.array([4, 5, 6])
    result = compute_dot_product(v1, v2)
    expected = 32  # 1*4 + 2*5 + 3*6 = 4 + 10 + 18 = 32
    print(f"   Result: {result}")
    print(f"   Expected: {expected}")
    assert result == expected, f"Expected {expected}, got {result}"
    print("   ✅ Passed!")
    
    # Test 3: Matrix multiplication
    print("\n3. Testing matrix_multiplication:")
    A = np.array([[1, 2], [3, 4]])
    B = np.array([[5, 6], [7, 8]])
    result = matrix_multiplication(A, B)
    expected = np.array([[19, 22], [43, 50]])
    print(f"   Result:\n{result}")
    print(f"   Expected:\n{expected}")
    assert np.allclose(result, expected), "Matrix multiplication incorrect"
    print("   ✅ Passed!")
    
    # Test 4: Transpose
    print("\n4. Testing compute_transpose:")
    matrix = np.array([[1, 2, 3], [4, 5, 6]])
    result = compute_transpose(matrix)
    expected = np.array([[1, 4], [2, 5], [3, 6]])
    print(f"   Original shape: {matrix.shape}")
    print(f"   Transposed shape: {result.shape}")
    assert np.allclose(result, expected), "Transpose incorrect"
    print("   ✅ Passed!")
    
    print("\n" + "=" * 60)
    print("🎉 All tests passed! Great job!")
