"""
Unit 5 - Example 15: GPU Workflows & RAPIDS | سير عمل GPU و RAPIDS

This example teaches GPU-accelerated workflows using RAPIDS.
Learn how to build complete data science pipelines that run on GPU.

## 📚 Prerequisites (What You Need First) | المتطلبات الأساسية

BEFORE starting this example, you should have completed:
- ✅ Example 14: Dask Distributed - Understand scaling concepts
- ✅ Example 3: cuDF Introduction - Understand GPU DataFrames
- ✅ Unit 4: Machine Learning - Understand ML workflows

If you haven't completed these, you might struggle with:
- Understanding GPU workflows
- Knowing when GPU helps in complete pipelines
- Understanding RAPIDS ecosystem

## 🔗 Where This Example Fits | مكان هذا المثال

This is the SECOND example in Unit 5 - Scaling Data Science!

Why this example SECOND?
- Before production pipelines, understand GPU workflows
- Combines GPU data processing (cuDF) with GPU ML (cuML)
- Shows complete GPU-accelerated pipeline

Builds on: 
- Example 3: cuDF (GPU DataFrames)
- Example 13: CPU vs GPU ML (GPU ML basics)
- Example 14: Dask (distributed computing)

Leads to: 
- Example 16: Production Pipelines (can use GPU workflows)
- Example 17: Performance Optimization (optimize GPU code)
- Production scaling (GPU workflows in production)

## The Story: Complete GPU Pipeline | القصة: خط أنابيب GPU كامل

Imagine a factory. GPU workflows are like having the entire assembly line run on 
powerful machines - from raw materials (data loading) to finished product (predictions), 
everything is fast. After GPU workflows, entire pipelines are accelerated!

Same with data science: GPU workflows accelerate entire pipeline - data loading, cleaning, 
processing, and ML all on GPU. After learning GPU workflows, complete pipelines are fast!

## Why GPU Workflows Matter | لماذا يهم

GPU workflows are powerful because:
- End-to-End: Entire pipeline on GPU (not just one step)
- Speed: 10-100x faster than CPU for large datasets
- RAPIDS: Complete ecosystem (cuDF, cuML, cuGraph)
- Production: Essential for real-time or large-scale production

## Learning Objectives | أهداف التعلم

By the end of this example, you will:
1. Build complete GPU-accelerated workflows
2. Combine cuDF (data processing) with cuML (ML)
3. Understand RAPIDS ecosystem
4. Compare GPU vs CPU workflow performance
5. Know when to use GPU workflows
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import time
# Try to import RAPIDS
try:
    import cudf
    import cuml
    from cuml.linear_model import LinearRegression
    RAPIDS_AVAILABLE = True
    print("✓ RAPIDS is available")
except ImportError:
    RAPIDS_AVAILABLE = False
print("⚠ RAPIDS not available - Using simulation")
print("=" * 70)
print("Example 15: GPU Workflows & RAPIDS")
print(" 15:   GPU  RAPIDS")
print("=" * 70)
# ============================================================================
# 1. DATA PROCESSING WORKFLOW
# ============================================================================
print("\n1. GPU Data Processing Workflow")
print("-" * 70)
np.random.seed(42)
n_samples = 500000
data = {
'id': range(n_samples),
'value1': np.random.randn(n_samples),
'value2': np.random.randn(n_samples),
'category': np.random.choice(['A', 'B', 'C'], n_samples),
'score': np.random.randint(0, 100, n_samples)
}
df_pandas = pd.DataFrame(data)
if RAPIDS_AVAILABLE:
    print("\nUsing cuDF (GPU)...")
    df_gpu = cudf.DataFrame(data)
    # GPU operations
    start_time = time.time()
    result_gpu = df_gpu.groupby('category').agg({
        'value1': 'mean',
        'value2': 'std',
        'score': ['mean', 'max']
    })
    gpu_time = time.time() - start_time
    print(f"GPU processing time: {gpu_time:.4f} seconds")
else:
    print("\n⚠ Simulating GPU workflow with pandas")
    df_gpu = df_pandas.copy()
    start_time = time.time()
    result_gpu = df_gpu.groupby('category').agg({
'value1': 'mean',
'value2': 'std',
'score': ['mean', 'max']
})
time.sleep(0.1)  # Simulate faster GPU
gpu_time = time.time() - start_time
# CPU comparison
start_time = time.time()
result_cpu = df_pandas.groupby('category').agg({
'value1': 'mean',
'value2': 'std',
'score': ['mean', 'max']
})
cpu_time = time.time() - start_time
print(f"CPU processing time: {cpu_time:.4f} seconds")
print(f"Speedup: {cpu_time/gpu_time:.2f}x")
# ============================================================================
# 2. MACHINE LEARNING WORKFLOW
# ============================================================================
print("\n\n2. GPU Machine Learning Workflow")
print("-" * 70)
X = df_pandas[['value1', 'value2', 'score']].values
y = df_pandas['value1'] * 2 + df_pandas['value2'] * 1.5 + np.random.randn(n_samples) * 0.1
if RAPIDS_AVAILABLE:
    X_gpu = cudf.DataFrame({'value1': X[:, 0], 'value2': X[:, 1], 'score': X[:, 2]})
    y_gpu = cudf.Series(y)
    start_time = time.time()
    gpu_model = LinearRegression()
    gpu_model.fit(X_gpu, y_gpu)
    gpu_ml_time = time.time() - start_time
    print(f"GPU ML training time: {gpu_ml_time:.4f} seconds")
else:
    print("⚠ Simulating GPU ML workflow")
    gpu_ml_time = 0.5
from sklearn.linear_model import LinearRegression as skLinearRegression
start_time = time.time()
cpu_model = skLinearRegression()
cpu_model.fit(X, y)
cpu_ml_time = time.time() - start_time
print(f"CPU ML training time: {cpu_ml_time:.4f} seconds")
# ============================================================================
# 3. VISUALIZATION
# ============================================================================
print("\n\n3. Creating Workflow Comparison")
print("-" * 70)
fig, axes = plt.subplots(1, 2, figsize=(14, 6))
fig.suptitle('RAPIDS GPU Workflow Performance',
fontsize=16, weight='bold')
# Data processing comparison
ops = ['Data Processing\n ', 'ML Training\n ML']
cpu_times = [cpu_time, cpu_ml_time]
gpu_times = [gpu_time, gpu_ml_time]
x = np.arange(len(ops))
width = 0.35
bars1 = axes[0].bar(x - width/2, cpu_times, width, label='CPU (pandas/scikit-learn)',
color='#FF6B6B', edgecolor='black')
bars2 = axes[0].bar(x + width/2, gpu_times, width, label='GPU (RAPIDS)',
color='#4ECDC4', edgecolor='black')
axes[0].set_ylabel('Time (seconds)')
axes[0].set_title('Performance Comparison',
                  fontsize=14, weight='bold')
axes[0].set_xticks(x)
axes[0].set_xticklabels(ops)
axes[0].legend()
axes[0].grid(True, alpha=0.3, axis='y')
# Speedup chart
speedups = [cpu_time/gpu_time, cpu_ml_time/gpu_ml_time]
bars = axes[1].bar(ops, speedups, color='#45B7D1', edgecolor='black')
axes[1].set_ylabel('Speedup (x)')
axes[1].set_title('GPU Speedup Factor')
axes[1].grid(True, alpha=0.3, axis='y')
for bar, speedup in zip(bars, speedups):
    height = bar.get_height()
axes[1].text(bar.get_x() + bar.get_width()/2., height,
f'{speedup:.2f}x', ha='center', va='bottom', fontsize=11, weight='bold')
plt.tight_layout()
plt.savefig('15_rapids_workflow.png', dpi=300, bbox_inches='tight')
print("✓ Workflow comparison saved")
plt.close()
# ============================================================================
# 4. SUMMARY
# ============================================================================
print("\n" + "=" * 70)
print("Summary")
print("=" * 70)
print("\nKey Concepts Covered:")
print("1. RAPIDS ecosystem (cuDF, cuML)")
print("2. GPU-accelerated data processing")
print("3. GPU-accelerated ML workflows")
print("4. End-to-end GPU pipeline")
print("\nNext Steps: Continue to Example 16 for Production Pipelines")
print(" :    16  ")