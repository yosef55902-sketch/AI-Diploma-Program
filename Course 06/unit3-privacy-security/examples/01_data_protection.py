"""
Unit 3: Privacy, Security, and Data Protection
Example 1: Data Protection Strategies

This example demonstrates data protection strategies including:
- Encryption techniques
- Secure data storage
- Anonymization and pseudonymization
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from cryptography.fernet import Fernet
import hashlib
import warnings
warnings.filterwarnings('ignore')

plt.rcParams['font.size'] = 10
plt.rcParams['figure.figsize'] = (14, 8)
sns.set_style("whitegrid")

# ============================================================================
# ENCRYPTION TECHNIQUES
# ============================================================================

def generate_encryption_key():
    """Generate a symmetric encryption key"""
    return Fernet.generate_key()

def encrypt_data(data, key):
    """Encrypt data using Fernet symmetric encryption"""
    f = Fernet(key)
    if isinstance(data, str):
        encrypted = f.encrypt(data.encode())
    else:
        encrypted = f.encrypt(str(data).encode())
    return encrypted

def decrypt_data(encrypted_data, key):
    """Decrypt data using Fernet symmetric encryption"""
    f = Fernet(key)
    decrypted = f.decrypt(encrypted_data)
    return decrypted.decode()

# ============================================================================
# ANONYMIZATION TECHNIQUES
# ============================================================================

def anonymize_data(df, columns_to_anonymize):
    """
    Anonymize data by removing or masking identifying information
    """
    df_anonymized = df.copy()
    
    for col in columns_to_anonymize:
        if col in df_anonymized.columns:
            # Replace with generic identifiers
            df_anonymized[col] = [f'ID_{i}' for i in range(len(df_anonymized))]
    
    return df_anonymized

def pseudonymize_data(df, columns_to_pseudonymize, salt='default_salt'):
    """
    Pseudonymize data by replacing with hashed values
    """
    df_pseudonymized = df.copy()
    
    for col in columns_to_pseudonymize:
        if col in df_pseudonymized.columns:
            # Create hash-based pseudonyms
            df_pseudonymized[col] = df_pseudonymized[col].apply(
                lambda x: hashlib.sha256((str(x) + salt).encode()).hexdigest()[:16]
            )
    
    return df_pseudonymized

# ============================================================================
# DATA PROTECTION COMPARISON
# ============================================================================

def demonstrate_data_protection():
    """
    Demonstrate different data protection techniques
    """
    # Create sample sensitive data
    np.random.seed(42)
    n_samples = 100
    
    data = {
        'name': [f'Person_{i}' for i in range(n_samples)],
        'email': [f'user{i}@example.com' for i in range(n_samples)],
        'ssn': [f'{np.random.randint(100,999)}-{np.random.randint(10,99)}-{np.random.randint(1000,9999)}' 
                for _ in range(n_samples)],
        'salary': np.random.normal(50000, 15000, n_samples),
        'age': np.random.randint(25, 65, n_samples)
    }
    
    df = pd.DataFrame(data)
    
    print("="*80)
    print("ORIGINAL DATA (First 5 rows):")
    print("="*80)
    print(df.head())
    
    # 1. Anonymization
    print("\n" + "="*80)
    print("1. ANONYMIZATION")
    print("="*80)
    df_anonymized = anonymize_data(df, ['name', 'email', 'ssn'])
    print("\nAnonymized Data (First 5 rows):")
    print(df_anonymized.head())
    
    # 2. Pseudonymization
    print("\n" + "="*80)
    print("2. PSEUDONYMIZATION")
    print("="*80)
    df_pseudonymized = pseudonymize_data(df, ['name', 'email', 'ssn'])
    print("\nPseudonymized Data (First 5 rows):")
    print(df_pseudonymized.head())
    
    # 3. Encryption
    print("\n" + "="*80)
    print("3. ENCRYPTION")
    print("="*80)
    key = generate_encryption_key()
    print(f"Generated encryption key: {key[:20]}...")
    
    # Encrypt sensitive column
    sample_email = df['email'].iloc[0]
    encrypted_email = encrypt_data(sample_email, key)
    decrypted_email = decrypt_data(encrypted_email, key)
    
    print(f"\nOriginal email: {sample_email}")
    print(f"Encrypted: {encrypted_email[:50]}...")
    print(f"Decrypted: {decrypted_email}")
    
    return df, df_anonymized, df_pseudonymized

# ============================================================================
# VISUALIZATIONS
# ============================================================================

def plot_data_protection_comparison(df, df_anonymized, df_pseudonymized):
    """
    Visualize data protection techniques comparison
    """
    fig, axes = plt.subplots(2, 2, figsize=(16, 12))
    
    # Original data distribution
    axes[0, 0].hist(df['salary'], bins=20, color='#e74c3c', alpha=0.7, edgecolor='black')
    axes[0, 0].set_title('Original Data: Salary Distribution', fontsize=12, fontweight='bold')
    axes[0, 0].set_xlabel('Salary')
    axes[0, 0].set_ylabel('Frequency')
    axes[0, 0].grid(alpha=0.3)
    
    # Anonymized data (same distribution, different identifiers)
    axes[0, 1].hist(df_anonymized['salary'], bins=20, color='#3498db', alpha=0.7, edgecolor='black')
    axes[0, 1].set_title('Anonymized Data: Salary Distribution', fontsize=12, fontweight='bold')
    axes[0, 1].set_xlabel('Salary')
    axes[0, 1].set_ylabel('Frequency')
    axes[0, 1].grid(alpha=0.3)
    
    # Pseudonymized data
    axes[1, 0].hist(df_pseudonymized['salary'], bins=20, color='#2ecc71', alpha=0.7, edgecolor='black')
    axes[1, 0].set_title('Pseudonymized Data: Salary Distribution', fontsize=12, fontweight='bold')
    axes[1, 0].set_xlabel('Salary')
    axes[1, 0].set_ylabel('Frequency')
    axes[1, 0].grid(alpha=0.3)
    
    # Protection techniques comparison
    techniques = ['Original', 'Anonymized', 'Pseudonymized', 'Encrypted']
    privacy_level = [1, 7, 8, 10]  # Privacy level (1-10)
    utility_level = [10, 9, 8, 7]  # Data utility (1-10)
    
    x = np.arange(len(techniques))
    width = 0.35
    
    axes[1, 1].bar(x - width/2, privacy_level, width, label='Privacy Level', alpha=0.8, color='#9b59b6')
    axes[1, 1].bar(x + width/2, utility_level, width, label='Data Utility', alpha=0.8, color='#f39c12')
    axes[1, 1].set_xlabel('Protection Technique', fontsize=11, fontweight='bold')
    axes[1, 1].set_ylabel('Score (1-10)', fontsize=11, fontweight='bold')
    axes[1, 1].set_title('Privacy vs Utility Trade-off', fontsize=12, fontweight='bold')
    axes[1, 1].set_xticks(x)
    axes[1, 1].set_xticklabels(techniques, rotation=15)
    axes[1, 1].legend()
    axes[1, 1].grid(axis='y', alpha=0.3)
    axes[1, 1].set_ylim([0, 11])
    
    plt.tight_layout()
    plt.savefig('unit3-privacy-security/examples/data_protection_comparison.png', 
                dpi=300, bbox_inches='tight')
    print("\n✅ Saved: data_protection_comparison.png")
    plt.close()

# ============================================================================
# MAIN EXECUTION
# ============================================================================

if __name__ == "__main__":
    print("="*80)
    print("Unit 3 - Example 1: Data Protection Strategies")
    print("="*80)
    
    # Demonstrate data protection techniques
    df, df_anonymized, df_pseudonymized = demonstrate_data_protection()
    
    # Create visualizations
    print("\n" + "="*80)
    print("Creating Visualizations...")
    print("="*80)
    
    plot_data_protection_comparison(df, df_anonymized, df_pseudonymized)
    
    # Summary
    print("\n" + "="*80)
    print("SUMMARY")
    print("="*80)
    print("\nKey Takeaways:")
    print("1. Anonymization removes identifying information completely")
    print("2. Pseudonymization replaces identifiers with reversible hashes")
    print("3. Encryption protects data at rest and in transit")
    print("4. Each technique has trade-offs between privacy and utility")
    print("5. Choose protection technique based on use case requirements")
    print("="*80 + "\n")
