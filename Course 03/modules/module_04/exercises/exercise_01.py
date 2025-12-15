"""
Exercise 01: Principal Component Analysis (PCA)

This exercise helps you understand and implement PCA, a fundamental
dimensionality reduction technique.

Instructions:
1. Implement PCA from scratch
2. Understand how eigenvalues are used
3. Apply to reduce dimensions
"""

import numpy as np


def compute_covariance_matrix(data):
    """
    Compute the covariance matrix of data.
    
    WHY: PCA finds eigenvectors of covariance matrix
    HOW: Covariance measures how features vary together
    
    Args:
        data: Data matrix (samples, features)
        
    Returns:
        Covariance matrix
    """
    # TODO: Compute covariance matrix
    # Hint: Center data first (subtract mean), then compute covariance
    pass


def pca_from_scratch(data, n_components=2):
    """
    Implement PCA from scratch using eigenvalue decomposition.
    
    WHY: Reduce dimensions while preserving variance
    HOW: 
    1. Compute covariance matrix
    2. Find eigenvalues and eigenvectors
    3. Select top n_components eigenvectors
    4. Project data onto these components
    
    Args:
        data: Data matrix (samples, features)
        n_components: Number of components to keep
        
    Returns:
        Tuple of (reduced_data, explained_variance_ratio)
    """
    # TODO: Implement PCA
    # Steps:
    # 1. Center the data (subtract mean)
    # 2. Compute covariance matrix
    # 3. Find eigenvalues and eigenvectors
    # 4. Sort by eigenvalues (descending)
    # 5. Select top n_components
    # 6. Project data: reduced = data @ eigenvectors
    # 7. Calculate explained variance ratio
    pass


def calculate_variance_explained(eigenvalues, n_components):
    """
    Calculate how much variance is explained by top components.
    
    Args:
        eigenvalues: All eigenvalues (sorted descending)
        n_components: Number of components to consider
        
    Returns:
        Variance explained ratio (0 to 1)
    """
    # TODO: Calculate variance explained
    # Formula: sum(top_n_eigenvalues) / sum(all_eigenvalues)
    pass


# Test your solutions
if __name__ == "__main__":
    print("Testing Exercise 01: PCA")
    print("=" * 60)
    
    # Create sample data
    np.random.seed(42)
    data = np.random.randn(100, 10)
    
    # Test 1: Covariance matrix
    print("\n1. Testing compute_covariance_matrix:")
    cov = compute_covariance_matrix(data)
    print(f"   Data shape: {data.shape}")
    print(f"   Covariance shape: {cov.shape}")
    assert cov.shape == (10, 10), "Covariance should be square"
    assert np.allclose(cov, cov.T), "Covariance should be symmetric"
    print("   ✅ Passed!")
    
    # Test 2: PCA
    print("\n2. Testing pca_from_scratch:")
    reduced, variance_ratio = pca_from_scratch(data, n_components=2)
    print(f"   Original shape: {data.shape}")
    print(f"   Reduced shape: {reduced.shape}")
    print(f"   Variance explained: {variance_ratio:.2%}")
    assert reduced.shape == (100, 2), "Should reduce to 2 dimensions"
    assert 0 <= variance_ratio <= 1, "Variance ratio should be between 0 and 1"
    print("   ✅ Passed!")
    
    print("\n" + "=" * 60)
    print("🎉 All tests passed!")
