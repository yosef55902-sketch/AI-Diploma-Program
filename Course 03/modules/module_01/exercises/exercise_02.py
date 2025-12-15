"""
Exercise 02: Matrix Properties and Operations

This exercise focuses on understanding matrix properties that are important
for machine learning, such as determinants, inverses, and eigenvalues.

Instructions:
1. Complete the functions below
2. Understand what each property means for ML
3. Test your solutions
"""

import numpy as np


def compute_determinant(matrix):
    """
    Compute the determinant of a square matrix.
    
    The determinant tells us if a transformation is invertible.
    In ML, this is important for understanding if operations can be reversed.
    
    Args:
        matrix: Square matrix (n, n)
        
    Returns:
        Determinant value (scalar)
    """
    # TODO: Compute determinant using np.linalg.det()
    pass


def compute_matrix_inverse(matrix):
    """
    Compute the inverse of a matrix.
    
    Matrix inverse is used in solving linear systems and some ML algorithms.
    
    Args:
        matrix: Square, invertible matrix
        
    Returns:
        Inverse matrix
    """
    # TODO: Compute inverse using np.linalg.inv()
    # Note: Matrix must be square and have non-zero determinant
    pass


def compute_eigenvalues_eigenvectors(matrix):
    """
    Compute eigenvalues and eigenvectors of a matrix.
    
    This is crucial for PCA (Module 04) and understanding data transformations.
    
    Args:
        matrix: Square matrix
        
    Returns:
        Tuple of (eigenvalues, eigenvectors)
    """
    # TODO: Use np.linalg.eig() to compute eigenvalues and eigenvectors
    pass


def verify_inverse(matrix, inverse):
    """
    Verify that a matrix and its inverse multiply to identity.
    
    Args:
        matrix: Original matrix
        inverse: Computed inverse
        
    Returns:
        True if matrix @ inverse ≈ identity matrix
    """
    # TODO: Multiply matrix by inverse and check if result is identity
    # Use np.allclose() for floating point comparison
    pass


# Test your solutions
if __name__ == "__main__":
    print("Testing Exercise 02: Matrix Properties")
    print("=" * 60)
    
    # Test 1: Determinant
    print("\n1. Testing compute_determinant:")
    matrix = np.array([[1, 2], [3, 4]])
    det = compute_determinant(matrix)
    expected = -2.0  # 1*4 - 2*3 = 4 - 6 = -2
    print(f"   Determinant: {det:.2f}")
    print(f"   Expected: {expected:.2f}")
    assert np.isclose(det, expected), "Determinant incorrect"
    print("   ✅ Passed!")
    
    # Test 2: Matrix inverse
    print("\n2. Testing compute_matrix_inverse:")
    matrix = np.array([[1, 2], [3, 4]])
    inv = compute_matrix_inverse(matrix)
    expected = np.array([[-2.0, 1.0], [1.5, -0.5]])
    print(f"   Inverse:\n{inv}")
    print(f"   Expected:\n{expected}")
    assert np.allclose(inv, expected), "Inverse incorrect"
    print("   ✅ Passed!")
    
    # Test 3: Verify inverse
    print("\n3. Testing verify_inverse:")
    is_valid = verify_inverse(matrix, inv)
    print(f"   Matrix @ Inverse = Identity: {is_valid}")
    assert is_valid, "Inverse verification failed"
    print("   ✅ Passed!")
    
    # Test 4: Eigenvalues and eigenvectors
    print("\n4. Testing compute_eigenvalues_eigenvectors:")
    matrix = np.array([[2, 1], [1, 2]])
    eigenvals, eigenvecs = compute_eigenvalues_eigenvectors(matrix)
    print(f"   Eigenvalues: {eigenvals}")
    print(f"   Eigenvectors:\n{eigenvecs}")
    print("   ✅ Computed successfully!")
    
    print("\n" + "=" * 60)
    print("🎉 All tests passed!")

