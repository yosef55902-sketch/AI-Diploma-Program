"""
Unit 3: Privacy, Security, and Data Protection
Exercise 1: Privacy Techniques

This exercise requires you to implement privacy-preserving techniques.
"""

import numpy as np
import pandas as pd

# ============================================================================
# TASK 1: Implement Anonymization
# ============================================================================

def anonymize_data(df, columns_to_anonymize):
    """
    TODO: Implement data anonymization.
    
    Requirements:
    - Replace identifying columns with generic identifiers
    - Return anonymized DataFrame
    """
    # TODO: Your code here
    pass

# ============================================================================
# TASK 2: Implement Pseudonymization
# ============================================================================

def pseudonymize_data(df, columns_to_pseudonymize, salt='default_salt'):
    """
    TODO: Implement data pseudonymization using hashing.
    
    Requirements:
    - Use hash function to create pseudonyms
    - Return pseudonymized DataFrame
    """
    # TODO: Your code here
    # Hint: Use hashlib.sha256()
    pass

# ============================================================================
# TASK 3: Implement Differential Privacy
# ============================================================================

def add_differential_privacy_noise(value, epsilon=1.0):
    """
    TODO: Add Laplace noise for differential privacy.
    
    Requirements:
    - Use Laplace distribution
    - Scale noise based on epsilon
    - Return noisy value
    """
    # TODO: Your code here
    # Hint: Use np.random.laplace()
    pass

# ============================================================================
# MAIN EXECUTION
# ============================================================================

if __name__ == "__main__":
    print("="*80)
    print("Unit 3 - Exercise 1: Privacy Techniques")
    print("="*80)
    print("\nComplete the TODO sections in this file.")
    print("="*80)
