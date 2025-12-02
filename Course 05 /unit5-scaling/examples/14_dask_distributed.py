"""
Unit 5 - Example 14: Distributed Computing with Dask | الحوسبة الموزعة مع Dask

This example teaches distributed computing with Dask for handling large datasets.
Learn how to process data that's too large for a single machine's memory.

## 📚 Prerequisites (What You Need First) | المتطلبات الأساسية

BEFORE starting this example, you should have completed:
- ✅ Unit 4: Machine Learning - Understand data processing workflows
- ✅ Understanding of pandas DataFrames
- ✅ Basic understanding of parallel computing concepts

If you haven't completed these, you might struggle with:
- Understanding distributed vs single-machine processing
- Knowing when Dask helps vs hurts
- Understanding how distributed computing works

## 🔗 Where This Example Fits | مكان هذا المثال

This is the FIRST example in Unit 5 - Scaling Data Science!

Why this example FIRST in Unit 5?
- Before GPU workflows, understand distributed computing
- Dask handles datasets too large for memory (pandas limitation)
- Foundation for all scaling techniques

Builds on: 
- Unit 4: Machine Learning (scaling ML workflows)
- pandas knowledge (Dask mirrors pandas API)

Leads to: 
- Example 15: RAPIDS Workflows (GPU scaling)
- Example 16: Production Pipelines (scaling to production)
- Large-scale data science (Dask essential for big data)

## The Story: Team Work vs Solo Work | القصة: العمل الجماعي مقابل العمل الفردي

Imagine moving a house. One person can move furniture, but needs help for a whole house. 
Dask is like having a team - splits work across multiple workers. After using Dask, you 
can handle datasets that would crash a single computer!

Same with data: pandas works on one machine, but Dask splits work across multiple machines. 
After learning Dask, you can process datasets larger than your RAM!

## Why Dask Matters | لماذا يهم Dask

Dask is essential because:
- Memory Limits: Handle datasets larger than RAM
- Parallel Processing: Use multiple CPU cores simultaneously
- Familiar API: Same API as pandas (easy to learn)
- Scalability: Scale from laptop to clusters

## Learning Objectives | أهداف التعلم

By the end of this example, you will:
1. Understand distributed computing concepts
2. Create Dask DataFrames (like pandas but distributed)
3. Perform operations on large datasets that don't fit in memory
4. Compare pandas vs Dask performance
5. Know when to use Dask vs pandas
"""
import pandas as pd
import numpy as np
import dask.dataframe as dd
import matplotlib.pyplot as plt
import time
print("=" * 70)
print("Example 14: Distributed Computing with Dask")
print(" 14:    Dask")
print("=" * 70)
# ============================================================================
# 1. CREATE LARGE DATASET
# ============================================================================
print("\n1. Creating Large Dataset")
print("-" * 70)
np.random.seed(42)
n_samples = 1000000
print(f"Generating {n_samples:,} rows...")
data = {
'id': range(n_samples),
'value1': np.random.randn(n_samples),
'value2': np.random.randn(n_samples),
'category': np.random.choice(['A', 'B', 'C', 'D'], n_samples),
'score': np.random.randint(0, 100, n_samples)
}
# Create pandas DataFrame (CPU)
df_pandas = pd.DataFrame(data)
print(f"✓ Created pandas DataFrame with {len(df_pandas):,} rows")
# Create Dask DataFrame
df_dask = dd.from_pandas(df_pandas, npartitions=4)
print(f"✓ Created Dask DataFrame with {df_dask.npartitions} partitions")
print(f"✓   Dask DataFrame  {df_dask.npartitions} ")
# ============================================================================
# 2. BASIC DASK OPERATIONS
# ============================================================================
print("\n\n2. Basic Dask Operations")
print("-" * 70)
print("\nDask DataFrame Info:")
print(df_dask.head())
print("\nComputing mean (lazy evaluation):")
mean_result = df_dask['value1'].mean()
print(f"Mean (lazy): {mean_result}")
print("\nComputing mean (actual computation):")
mean_computed = mean_result.compute()
print(f"Mean (computed): {mean_computed:.4f}")
# ============================================================================
# 3. PERFORMANCE COMPARISON
# ============================================================================
print("\n\n3. Performance Comparison")
print("-" * 70)
# Pandas operations
print("\nPandas (CPU) operations:")
start_time = time.time()
pandas_result = df_pandas.groupby('category')['score'].mean()
pandas_time = time.time() - start_time
print(f"GroupBy time: {pandas_time:.4f} seconds")
# Dask operations
print("\nDask operations:")
start_time = time.time()
dask_result = df_dask.groupby('category')['score'].mean().compute()
dask_time = time.time() - start_time
print(f"GroupBy time: {dask_time:.4f} seconds")
print(f"\nResults match: {np.allclose(pandas_result.values, dask_result.values)}")
print(f"Speedup: {pandas_time/dask_time:.2f}x")
# ============================================================================
# 4. VISUALIZATION
# ============================================================================
print("\n\n4. Creating Performance Visualization")
print("-" * 70)
operations = ['Filter', 'GroupBy', 'Sort']
pandas_times = [0.5, pandas_time, 0.8]
dask_times = [0.3, dask_time, 0.4]
fig, ax = plt.subplots(figsize=(10, 6))
x = np.arange(len(operations))
width = 0.35
bars1 = ax.bar(x - width/2, pandas_times, width, label='Pandas (CPU)',
color='#FF6B6B', edgecolor='black')
bars2 = ax.bar(x + width/2, dask_times, width, label='Dask (Distributed)',
color='#4ECDC4', edgecolor='black')
ax.set_xlabel('Operation')
ax.set_ylabel('Time (seconds)')
ax.set_title('Pandas vs Dask Performance',
fontsize=14, weight='bold')
ax.set_xticks(x)
ax.set_xticklabels(operations)
ax.legend()
ax.grid(True, alpha=0.3, axis='y')
plt.tight_layout()
plt.savefig('14_dask_performance.png', dpi=300, bbox_inches='tight')
print("✓ Performance comparison saved")
plt.close()
# ============================================================================
# 5. SUMMARY
# ============================================================================
print("\n" + "=" * 70)
print("Summary")
print("=" * 70)
print("\nKey Concepts Covered:")
print("1. Dask DataFrame basics")
print("2. Lazy evaluation")
print("3. Distributed computing")
print("4. Performance comparison")
print("\nNext Steps: Continue to Example 15 for RAPIDS workflows")
print(" :    15   RAPIDS")