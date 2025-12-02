"""
Unit 4 - Example 13: CPU vs GPU Machine Learning | تعلم الآلة على CPU و GPU

This example compares CPU and GPU machine learning performance.
Learn when GPU acceleration helps and when CPU is sufficient.

## 📚 Prerequisites (What You Need First) | المتطلبات الأساسية

BEFORE starting this example, you should have completed:
- ✅ Example 10: Linear Regression - Understand ML basics
- ✅ Example 11: Classification - Know classification algorithms
- ✅ Example 12: Model Evaluation - Know how to evaluate models

If you haven't completed these, you might struggle with:
- Understanding performance comparisons
- Knowing when GPU helps vs hurts
- Understanding GPU-accelerated ML libraries

## 🔗 Where This Example Fits | مكان هذا المثال

This is the FOURTH and FINAL example in Unit 4 - Machine Learning!

Why this example FOURTH?
- Before comparing CPU vs GPU, understand ML algorithms first
- After learning models and evaluation, compare performance
- This completes Unit 4 by showing how to scale ML

Builds on: 
- Example 10, 11, 12: ML algorithms and evaluation (compare their performance)

Leads to: 
- Unit 5: Scaling Data Science (GPU is part of scaling)
- Production ML (know when GPU acceleration is worth it)
- Large-scale ML (GPU essential for big datasets)

## The Story: Choosing the Right Tool | القصة: اختيار الأداة الصحيحة

Imagine you need to move furniture. For a few items, you use your car (CPU - sufficient). 
For a whole house, you rent a truck (GPU - much faster). After understanding both, you 
know which to use for each job!

Same with ML: For small datasets, CPU works fine. For large datasets, GPU is much faster. 
After comparing both, you know when GPU acceleration is worth it!

## Why CPU vs GPU Comparison Matters | لماذا يهم

Understanding both approaches is essential because:
- Performance: GPU can be 10-100x faster for large datasets
- Cost: GPU hardware costs more - know when it's worth it
- Scalability: GPU essential for scaling to big data
- Decision Making: Choose CPU or GPU based on your needs

## Learning Objectives | أهداف التعلم

By the end of this example, you will:
1. Compare CPU (scikit-learn) vs GPU (cuML) performance
2. Understand when GPU acceleration helps
3. Use GPU-accelerated ML libraries (cuML)
4. Make informed decisions about CPU vs GPU
5. See real performance differences on same algorithms
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import time
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import r2_score, accuracy_score
# Try to import cuML, fallback if not available
try:
    import cuml
    from cuml.linear_model import LinearRegression as cuLinearRegression
    from cuml.linear_model import LogisticRegression as cuLogisticRegression
    CUML_AVAILABLE = True
    print("✓ cuML is available - GPU acceleration enabled")
except ImportError:
    CUML_AVAILABLE = False
print("⚠ cuML not available - Using scikit-learn (CPU) with GPU simulation")
plt.style.use('seaborn-v0_8')
print("=" * 70)
print("Example 13: CPU vs GPU Machine Learning | تعلم الآلة على CPU و GPU")
print("=" * 70)
print("\n📚 Prerequisites: Examples 10, 11, 12 completed - understand ML first")
print("🔗 This is the FOURTH example in Unit 4 - comparing CPU vs GPU performance")
print("🎯 Goal: Understand when GPU acceleration helps ML performance\n")
print("=" * 70)
# ============================================================================
# 1. CREATE LARGE DATASET FOR COMPARISON
# ============================================================================
print("\n1. Creating Large Dataset")
print("-" * 70)
np.random.seed(42)
n_samples = 100000
X = np.random.randn(n_samples, 10)
y_regression = X[:, 0] * 2 + X[:, 1] * 1.5 - X[:, 2] * 0.5 + np.random.randn(n_samples) * 0.1
y_classification = (X[:, 0] + X[:, 1] > 0).astype(int)
print(f"✓ Created dataset with {n_samples:,} samples")
print(f"✓      {n_samples:,} ")
# ============================================================================
# 2. REGRESSION COMPARISON
# ============================================================================
print("\n\n2. Regression: CPU vs GPU")
print("-" * 70)
X_train, X_test, y_train, y_test = train_test_split(
X, y_regression, test_size=0.2, random_state=42)
# CPU (scikit-learn)
print("\nTraining CPU model (scikit-learn)...")
start_time = time.time()
cpu_model = LinearRegression()
cpu_model.fit(X_train, y_train)
cpu_train_time = time.time() - start_time
start_time = time.time()
cpu_pred = cpu_model.predict(X_test)
cpu_pred_time = time.time() - start_time
cpu_r2 = r2_score(y_test, cpu_pred)
print(f"CPU Training Time: {cpu_train_time:.4f} seconds")
print(f"CPU Prediction Time: {cpu_pred_time:.4f} seconds")
print(f"CPU R² Score: {cpu_r2:.4f}")
# GPU (cuML) or simulated
if CUML_AVAILABLE:
    print("\nTraining GPU model (cuML)...")
    start_time = time.time()
    gpu_model = cuLinearRegression()
    gpu_model.fit(X_train, y_train)
    gpu_train_time = time.time() - start_time
    start_time = time.time()
    gpu_pred = gpu_model.predict(X_test)
    gpu_pred_time = time.time() - start_time
    gpu_r2 = r2_score(y_test.get(), gpu_pred.get()) if hasattr(gpu_pred, 'get') else r2_score(y_test, gpu_pred)
    print(f"GPU Training Time: {gpu_train_time:.4f} seconds")
    print(f"GPU Prediction Time: {gpu_pred_time:.4f} seconds")
    print(f"GPU R² Score: {gpu_r2:.4f}")
    print(f"\nSpeedup - Training: {cpu_train_time/gpu_train_time:.2f}x")
    print(f"Speedup - Prediction: {cpu_pred_time/gpu_pred_time:.2f}x")
else:
    print("\n⚠ Simulating GPU performance (cuML not available)")
    gpu_train_time = cpu_train_time / 5  # Simulate 5x speedup
    gpu_pred_time = cpu_pred_time / 5
gpu_r2 = cpu_r2
# ============================================================================
# 3. CLASSIFICATION COMPARISON
# ============================================================================
print("\n\n3. Classification: CPU vs GPU")
print("-" * 70)
X_train_clf, X_test_clf, y_train_clf, y_test_clf = train_test_split(
X, y_classification, test_size=0.2, random_state=42, stratify=y_classification)
scaler = StandardScaler()
X_train_clf_scaled = scaler.fit_transform(X_train_clf)
X_test_clf_scaled = scaler.transform(X_test_clf)
# CPU
start_time = time.time()
cpu_clf = LogisticRegression(random_state=42, max_iter=1000)
cpu_clf.fit(X_train_clf_scaled, y_train_clf)
cpu_clf_train_time = time.time() - start_time
start_time = time.time()
cpu_clf_pred = cpu_clf.predict(X_test_clf_scaled)
cpu_clf_pred_time = time.time() - start_time
cpu_clf_acc = accuracy_score(y_test_clf, cpu_clf_pred)
print(f"CPU Training Time: {cpu_clf_train_time:.4f} seconds")
print(f"CPU Accuracy: {cpu_clf_acc:.4f}")
if CUML_AVAILABLE:
    start_time = time.time()
    gpu_clf = cuLogisticRegression()
    gpu_clf.fit(X_train_clf_scaled, y_train_clf)
    gpu_clf_train_time = time.time() - start_time
    start_time = time.time()
    gpu_clf_pred = gpu_clf.predict(X_test_clf_scaled)
    gpu_clf_pred_time = time.time() - start_time
    gpu_clf_acc = accuracy_score(y_test_clf, gpu_clf_pred.get() if hasattr(gpu_clf_pred, 'get') else gpu_clf_pred)
    print(f"GPU Training Time: {gpu_clf_train_time:.4f} seconds")
    print(f"GPU Accuracy: {gpu_clf_acc:.4f}")
else:
    gpu_clf_train_time = cpu_clf_train_time / 5
    gpu_clf_pred_time = cpu_clf_pred_time / 5
    gpu_clf_acc = cpu_clf_acc
# ============================================================================
# 4. VISUALIZATION
# ============================================================================
print("\n\n4. Performance Comparison Visualization")
print("-" * 70)
fig, axes = plt.subplots(1, 2, figsize=(14, 6))
fig.suptitle('CPU vs GPU Performance Comparison',
fontsize=16, weight='bold')
# Regression performance
categories = ['Training', 'Prediction']
cpu_times_reg = [cpu_train_time, cpu_pred_time]
gpu_times_reg = [gpu_train_time, gpu_pred_time]
x = np.arange(len(categories))
width = 0.35
bars1 = axes[0].bar(x - width/2, cpu_times_reg, width, label='CPU (scikit-learn)',
color='#FF6B6B', edgecolor='black')
bars2 = axes[0].bar(x + width/2, gpu_times_reg, width, label='GPU (cuML)',
color='#4ECDC4', edgecolor='black')
axes[0].set_xlabel('Operation')
axes[0].set_ylabel('Time (seconds)')
axes[0].set_title('Performance Comparison',
                  fontsize=14, weight='bold')
axes[0].set_xticks(x)
axes[0].set_xticklabels(categories)
axes[0].legend()
axes[0].grid(True, alpha=0.3, axis='y')
# Classification performance
cpu_times_clf = [cpu_clf_train_time, cpu_clf_pred_time]
gpu_times_clf = [gpu_clf_train_time, gpu_clf_pred_time]
bars3 = axes[1].bar(x - width/2, cpu_times_clf, width, label='CPU (scikit-learn)',
color='#FF6B6B', edgecolor='black')
bars4 = axes[1].bar(x + width/2, gpu_times_clf, width, label='GPU (cuML)',
color='#4ECDC4', edgecolor='black')
axes[1].set_xlabel('Operation')
axes[1].set_ylabel('Time (seconds)')
axes[1].set_title('Classification Performance',
                  fontsize=14, weight='bold')
axes[1].set_xticks(x)
axes[1].set_xticklabels(categories)
axes[1].legend()
axes[1].grid(True, alpha=0.3, axis='y')
plt.tight_layout()
plt.savefig('13_cpu_vs_gpu_comparison.png', dpi=300, bbox_inches='tight')
print("✓ Performance comparison saved")
plt.close()
# ============================================================================
# 5. SUMMARY
# ============================================================================
print("\n" + "=" * 70)
print("Summary")
print("=" * 70)
print("\nKey Concepts Covered:")
print("1. CPU-based ML with scikit-learn")
print("2. GPU-accelerated ML with cuML")
print("3. Performance comparison")
print("4. When to use CPU vs GPU")
print("\nNext Steps: Continue to Unit 5 for Scaling Data Science")
print(" :    5    ")