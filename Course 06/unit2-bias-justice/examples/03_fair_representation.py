"""
Unit 2: Bias, Justice, and Discrimination in AI
Example 3: Fair Representation Learning

This example demonstrates fair representation learning techniques:
- PCA for bias removal
- Autoencoders for feature transformation
- Adversarial debiasing
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.neural_network import MLPRegressor
import warnings
warnings.filterwarnings('ignore')

plt.rcParams['font.size'] = 10
plt.rcParams['figure.figsize'] = (14, 8)
sns.set_style("whitegrid")

# ============================================================================
# GENERATE BIASED DATASET
# ============================================================================

def generate_biased_dataset(n_samples=2000):
    """
    Generate dataset with bias correlated with sensitive attribute
    """
    np.random.seed(42)
    
    # Sensitive attribute
    sensitive = np.random.binomial(1, 0.5, n_samples)
    
    # Features correlated with sensitive attribute
    X1 = np.random.normal(0, 1, n_samples) + 0.5 * sensitive
    X2 = np.random.normal(0, 1, n_samples) + 0.3 * sensitive
    X3 = np.random.normal(0, 1, n_samples)
    X4 = np.random.normal(0, 1, n_samples)
    
    # Target (should be independent of sensitive attribute after fair representation)
    y = (0.4 * X1 + 0.3 * X2 + 0.2 * X3 + 0.1 * X4 + np.random.normal(0, 0.1, n_samples) > 0).astype(int)
    
    df = pd.DataFrame({
        'feature1': X1,
        'feature2': X2,
        'feature3': X3,
        'feature4': X4,
        'sensitive': sensitive,
        'target': y
    })
    
    return df

# ============================================================================
# FAIR REPRESENTATION USING PCA
# ============================================================================

def fair_representation_pca(X, sensitive, n_components=2):
    """
    Use PCA to remove correlation with sensitive attribute
    """
    # Standardize features
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    
    # Apply PCA
    pca = PCA(n_components=n_components)
    X_transformed = pca.fit_transform(X_scaled)
    
    # Check correlation with sensitive attribute
    correlations = []
    for i in range(n_components):
        corr = np.abs(np.corrcoef(X_transformed[:, i], sensitive)[0, 1])
        correlations.append(corr)
    
    return X_transformed, correlations, pca, scaler

# ============================================================================
# FAIR REPRESENTATION USING AUTOENCODER
# ============================================================================

def create_autoencoder(input_dim, encoding_dim=2):
    """
    Create a simple autoencoder for fair representation
    """
    # Simple MLP-based autoencoder
    encoder = MLPRegressor(
        hidden_layer_sizes=(input_dim, encoding_dim),
        activation='relu',
        solver='adam',
        max_iter=500,
        random_state=42
    )
    
    decoder = MLPRegressor(
        hidden_layer_sizes=(encoding_dim, input_dim),
        activation='relu',
        solver='adam',
        max_iter=500,
        random_state=42
    )
    
    return encoder, decoder

def train_autoencoder(X, encoding_dim=2):
    """
    Train autoencoder to learn fair representation
    """
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    
    encoder, decoder = create_autoencoder(X.shape[1], encoding_dim)
    
    # Train encoder-decoder
    encoder.fit(X_scaled, X_scaled)
    encoded = encoder.predict(X_scaled)
    decoder.fit(encoded, X_scaled)
    
    return encoder, decoder, scaler, encoded

# ============================================================================
# ADVERSARIAL DEBIASING (SIMPLIFIED)
# ============================================================================

def adversarial_debiasing_simple(X, y, sensitive, epochs=100):
    """
    Simplified adversarial debiasing approach
    Main model predicts target, adversary predicts sensitive attribute
    Goal: Make it hard for adversary to predict sensitive attribute
    """
    from sklearn.linear_model import LogisticRegression
    
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    
    # Main model (predicts target)
    main_model = LogisticRegression(random_state=42, max_iter=1000)
    main_model.fit(X_scaled, y)
    
    # Adversary model (tries to predict sensitive attribute from main model's features)
    # In practice, this would be trained adversarially
    adversary = LogisticRegression(random_state=42, max_iter=1000)
    adversary.fit(X_scaled, sensitive)
    
    # Measure how well adversary can predict sensitive attribute
    adversary_pred = adversary.predict(X_scaled)
    adversary_acc = accuracy_score(sensitive, adversary_pred)
    
    return main_model, adversary, scaler, adversary_acc

# ============================================================================
# EVALUATION
# ============================================================================

def evaluate_fairness(X_transformed, sensitive, method_name):
    """
    Evaluate how well the transformation removes correlation with sensitive attribute
    """
    correlations = []
    for i in range(X_transformed.shape[1]):
        corr = np.abs(np.corrcoef(X_transformed[:, i], sensitive)[0, 1])
        correlations.append(corr)
    
    avg_correlation = np.mean(correlations)
    max_correlation = np.max(correlations)
    
    print(f"\n{method_name}:")
    print(f"  Average correlation with sensitive attribute: {avg_correlation:.4f}")
    print(f"  Maximum correlation: {max_correlation:.4f}")
    
    return avg_correlation, max_correlation

def compare_representations(df):
    """
    Compare different fair representation learning methods
    """
    X = df[['feature1', 'feature2', 'feature3', 'feature4']].values
    y = df['target'].values
    sensitive = df['sensitive'].values
    
    # Split data
    X_train, X_test, y_train, y_test, sensitive_train, sensitive_test = train_test_split(
        X, y, sensitive, test_size=0.3, random_state=42, stratify=y
    )
    
    results = {}
    
    # 1. Original features (baseline)
    print("="*80)
    print("1. BASELINE: Original Features")
    print("="*80)
    corr_orig = []
    for i in range(X_train.shape[1]):
        corr = np.abs(np.corrcoef(X_train[:, i], sensitive_train)[0, 1])
        corr_orig.append(corr)
    print(f"Average correlation with sensitive attribute: {np.mean(corr_orig):.4f}")
    
    # Train classifier on original features
    scaler_orig = StandardScaler()
    X_train_scaled = scaler_orig.fit_transform(X_train)
    X_test_scaled = scaler_orig.transform(X_test)
    model_orig = RandomForestClassifier(n_estimators=100, random_state=42)
    model_orig.fit(X_train_scaled, y_train)
    acc_orig = accuracy_score(y_test, model_orig.predict(X_test_scaled))
    print(f"Classification accuracy: {acc_orig:.4f}")
    results['Original'] = {
        'correlation': np.mean(corr_orig),
        'accuracy': acc_orig,
        'features': X_train_scaled
    }
    
    # 2. PCA-based fair representation
    print("\n" + "="*80)
    print("2. PCA-BASED FAIR REPRESENTATION")
    print("="*80)
    X_pca, correlations, pca, scaler_pca = fair_representation_pca(X_train, sensitive_train, n_components=2)
    avg_corr, max_corr = evaluate_fairness(X_pca, sensitive_train, "PCA")
    
    # Train classifier on PCA features
    X_test_pca = pca.transform(scaler_pca.transform(X_test))
    model_pca = RandomForestClassifier(n_estimators=100, random_state=42)
    model_pca.fit(X_pca, y_train)
    acc_pca = accuracy_score(y_test, model_pca.predict(X_test_pca))
    print(f"Classification accuracy: {acc_pca:.4f}")
    results['PCA'] = {
        'correlation': avg_corr,
        'accuracy': acc_pca,
        'features': X_pca
    }
    
    # 3. Autoencoder-based fair representation
    print("\n" + "="*80)
    print("3. AUTOENCODER-BASED FAIR REPRESENTATION")
    print("="*80)
    encoder, decoder, scaler_ae, X_encoded = train_autoencoder(X_train, encoding_dim=2)
    avg_corr, max_corr = evaluate_fairness(X_encoded, sensitive_train, "Autoencoder")
    
    # Train classifier on encoded features
    X_test_encoded = encoder.predict(scaler_ae.transform(X_test))
    model_ae = RandomForestClassifier(n_estimators=100, random_state=42)
    model_ae.fit(X_encoded, y_train)
    acc_ae = accuracy_score(y_test, model_ae.predict(X_test_encoded))
    print(f"Classification accuracy: {acc_ae:.4f}")
    results['Autoencoder'] = {
        'correlation': avg_corr,
        'accuracy': acc_ae,
        'features': X_encoded
    }
    
    # 4. Adversarial debiasing
    print("\n" + "="*80)
    print("4. ADVERSARIAL DEBIASING")
    print("="*80)
    main_model, adversary, scaler_adv, adv_acc = adversarial_debiasing_simple(
        X_train, y_train, sensitive_train
    )
    print(f"Adversary accuracy (predicting sensitive attribute): {adv_acc:.4f}")
    print(f"Main model accuracy: {accuracy_score(y_test, main_model.predict(scaler_adv.transform(X_test))):.4f}")
    results['Adversarial'] = {
        'correlation': adv_acc,  # Adversary accuracy as proxy
        'accuracy': accuracy_score(y_test, main_model.predict(scaler_adv.transform(X_test))),
        'features': scaler_adv.transform(X_train)
    }
    
    return results

# ============================================================================
# VISUALIZATIONS
# ============================================================================

def plot_correlation_comparison(results):
    """
    Plot correlation comparison across methods
    """
    methods = list(results.keys())
    correlations = [results[m]['correlation'] for m in methods]
    accuracies = [results[m]['accuracy'] for m in methods]
    
    fig, axes = plt.subplots(1, 2, figsize=(16, 6))
    
    # Correlation plot
    axes[0].bar(methods, correlations, color=['#e74c3c', '#3498db', '#2ecc71', '#f39c12'])
    axes[0].set_title('Correlation with Sensitive Attribute (Lower is Better)', 
                     fontsize=12, fontweight='bold')
    axes[0].set_ylabel('Correlation')
    axes[0].tick_params(axis='x', rotation=15)
    axes[0].grid(axis='y', alpha=0.3)
    
    # Accuracy plot
    axes[1].bar(methods, accuracies, color=['#e74c3c', '#3498db', '#2ecc71', '#f39c12'])
    axes[1].set_title('Classification Accuracy', fontsize=12, fontweight='bold')
    axes[1].set_ylabel('Accuracy')
    axes[1].tick_params(axis='x', rotation=15)
    axes[1].grid(axis='y', alpha=0.3)
    axes[1].set_ylim([0, 1])
    
    plt.tight_layout()
    plt.savefig('unit2-bias-justice/examples/fair_representation_comparison.png', 
                dpi=300, bbox_inches='tight')
    print("\n✅ Saved: fair_representation_comparison.png")
    plt.close()

def plot_feature_space(results, sensitive):
    """
    Plot 2D feature space for PCA and Autoencoder
    """
    fig, axes = plt.subplots(1, 2, figsize=(16, 6))
    
    # PCA features
    if 'PCA' in results and results['PCA']['features'].shape[1] >= 2:
        pca_features = results['PCA']['features']
        scatter = axes[0].scatter(pca_features[:, 0], pca_features[:, 1], 
                                 c=sensitive, cmap='coolwarm', alpha=0.6)
        axes[0].set_title('PCA Feature Space', fontsize=12, fontweight='bold')
        axes[0].set_xlabel('First Principal Component')
        axes[0].set_ylabel('Second Principal Component')
        axes[0].grid(alpha=0.3)
        plt.colorbar(scatter, ax=axes[0], label='Sensitive Attribute')
    
    # Autoencoder features
    if 'Autoencoder' in results and results['Autoencoder']['features'].shape[1] >= 2:
        ae_features = results['Autoencoder']['features']
        scatter = axes[1].scatter(ae_features[:, 0], ae_features[:, 1], 
                                 c=sensitive, cmap='coolwarm', alpha=0.6)
        axes[1].set_title('Autoencoder Feature Space', fontsize=12, fontweight='bold')
        axes[1].set_xlabel('First Encoded Dimension')
        axes[1].set_ylabel('Second Encoded Dimension')
        axes[1].grid(alpha=0.3)
        plt.colorbar(scatter, ax=axes[1], label='Sensitive Attribute')
    
    plt.tight_layout()
    plt.savefig('unit2-bias-justice/examples/fair_representation_feature_space.png', 
                dpi=300, bbox_inches='tight')
    print("✅ Saved: fair_representation_feature_space.png")
    plt.close()

# ============================================================================
# MAIN EXECUTION
# ============================================================================

if __name__ == "__main__":
    print("="*80)
    print("Unit 2 - Example 3: Fair Representation Learning")
    print("="*80)
    
    # Generate dataset
    print("\nGenerating biased dataset...")
    df = generate_biased_dataset(n_samples=2000)
    print(f"Dataset shape: {df.shape}")
    
    # Compare methods
    results = compare_representations(df)
    
    # Create visualizations
    print("\n" + "="*80)
    print("Creating Visualizations...")
    print("="*80)
    
    plot_correlation_comparison(results)
    plot_feature_space(results, df['sensitive'].values[:len(results['PCA']['features'])])
    
    # Summary
    print("\n" + "="*80)
    print("SUMMARY")
    print("="*80)
    print("\nKey Takeaways:")
    print("1. Fair representation learning transforms features to remove bias")
    print("2. PCA can reduce correlation with sensitive attributes")
    print("3. Autoencoders learn compressed representations")
    print("4. Adversarial debiasing makes it hard to predict sensitive attributes")
    print("5. Trade-off between fairness and predictive performance")
    print("="*80 + "\n")

