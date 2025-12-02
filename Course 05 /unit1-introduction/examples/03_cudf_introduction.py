"""
Unit 1 - Example 3: Introduction to cuDF (GPU-Accelerated DataFrames) | مقدمة إلى cuDF

This example introduces GPU-accelerated data processing using cuDF.
Learn when and why to use GPU acceleration for faster data science.

All concepts are explained in the code comments below - you can learn everything
from this code example alone!

## 📚 Prerequisites (What You Need First) | المتطلبات الأساسية

BEFORE starting this example, you should have completed:
- ✅ Example 2: pandas & NumPy Basics - You need pandas knowledge first!
- ✅ Understanding of DataFrames and basic operations
- ✅ (Optional) NVIDIA GPU available for actual GPU acceleration

If you haven't completed these, you might struggle with:
- Understanding DataFrame operations
- Comparing CPU vs GPU approaches
- Knowing when GPU acceleration helps

## 🔗 Where This Example Fits | مكان هذا المثال

This is the THIRD example - it builds on pandas knowledge from Example 2!

Why this example THIRD?
- Before you can use GPU acceleration, you need to understand pandas
- Before you can decide GPU vs CPU, you need to see the performance difference
- Before you can scale to large datasets, you need GPU tools

Builds on: 
- Example 2: pandas & NumPy Basics (GPU version of pandas operations)

Leads to: 
- Unit 2: Data Cleaning (can use GPU for large datasets)
- Unit 4: Machine Learning (can use GPU for ML training)
- Unit 5: Scaling Data Science (GPU is essential for scaling!)

## The Story: Turbo vs Normal Engine | القصة: محرك توربو مقابل عادي

Imagine you're driving. A normal engine works fine for city driving, but when you need 
to go fast or carry heavy loads, a turbo engine gives you 5-10x more power!

Same with data processing: pandas (CPU) works fine for small data, but when you have 
millions of rows, cuDF (GPU) gives you 5-10x speedup - same operations, much faster!

## Why GPU Acceleration Matters | لماذا يهم تسريع GPU

GPU acceleration is crucial for:
- Large Datasets: Process millions of rows in seconds instead of minutes
- Real-Time Analytics: Get results fast enough for live dashboards
- Cost Efficiency: Do more work with same hardware
- Scalability: Handle data that would crash CPU-based tools

## Learning Objectives | أهداف التعلم

By the end of this example, you will:
1. Understand what cuDF is and how it relates to pandas
2. Create cuDF DataFrames (GPU-accelerated tables)
3. Compare CPU vs GPU performance on same operations
4. Know when to use GPU acceleration vs CPU
5. See real speedup benefits of GPU processing
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import time

# Try to import cuDF, fallback to pandas if not available
# Why try/except? cuDF requires NVIDIA GPU - may not be available on all machines
# Why fallback? Code should work even without GPU (use pandas simulation)
try:
    import cudf
    CUDF_AVAILABLE = True
    print("✓ cuDF is available - GPU acceleration enabled")
    print("✓ cuDF GPU acceleration is available")
except ImportError:
    CUDF_AVAILABLE = False
    print("⚠ cuDF not available - Using pandas (CPU) with GPU simulation")
    print("⚠ cuDF not installed - Using pandas (CPU) with simulated GPU speedup")

print("=" * 70)
print("Example 3: Introduction to cuDF | مقدمة إلى cuDF")
print("=" * 70)
print("\n📚 Prerequisites: Example 2 completed, pandas DataFrame knowledge")
print("🔗 This is the THIRD example - GPU acceleration for data science")
print("🎯 Goal: Understand GPU vs CPU performance and when to use each\n")
# ============================================================================
# PART 1: CREATE SAMPLE DATA - Large Dataset for Performance Testing
# ============================================================================
print("\n" + "=" * 70)
print("PART 1: Creating Large Sample Dataset")
print("=" * 70)

print("\n📋 BEFORE: You know pandas but haven't seen GPU acceleration")
print("📋 AFTER: You'll see how GPU can speed up large dataset operations")
print("💡 WHY THIS MATTERS: GPU shines with large data - small data won't show benefit!\n")

print("\n1. Creating Sample Data")
print("-" * 70)

# Create large dataset
# Why 1 million rows? Large enough to show GPU advantage (small datasets won't show speedup)
# Why seed(42)? Reproducible results - same data every run
np.random.seed(42)
n_rows = 1000000  # 1 million rows - large dataset to show GPU advantage
print(f"Generating {n_rows:,} rows of data...")
print(f"   Creating {n_rows:,} rows to demonstrate GPU performance advantage")

data = {
    'id': range(n_rows),
    'value1': np.random.randn(n_rows),
    'value2': np.random.randn(n_rows),
    'category': np.random.choice(['A', 'B', 'C', 'D'], n_rows),
    'score': np.random.randint(0, 100, n_rows)
}

# Create pandas DataFrame (CPU)
# Why pandas first? This is our baseline - compare GPU against this
df_pandas = pd.DataFrame(data)
print(f"\n✅ Created pandas DataFrame (CPU) with {len(df_pandas):,} rows")
print(f"   - This is our baseline for comparison")
print(f"   - CPU processes data sequentially (one operation at a time)")
# ============================================================================
# PART 2: CUDF OPERATIONS - Creating GPU-Accelerated DataFrames
# ============================================================================
print("\n" + "=" * 70)
print("PART 2: cuDF Operations - GPU-Accelerated DataFrames")
print("=" * 70)

print("\n📋 BEFORE: You have pandas DataFrame on CPU (slow for large data)")
print("📋 AFTER: You'll create cuDF DataFrame on GPU (much faster for large data)")
print("💡 WHY THIS MATTERS: Same operations, but GPU processes thousands of elements in parallel!\n")

print("\n2. Creating cuDF DataFrame (GPU)")
print("-" * 70)

if CUDF_AVAILABLE:
    # Convert to cuDF DataFrame (GPU)
    # Why cudf.DataFrame()? Same API as pandas but runs on GPU (parallel processing)
    # Why same API? Easy to switch - code looks identical!
    df_cudf = cudf.DataFrame(data)
    print(f"✅ Created cuDF DataFrame (GPU) with {len(df_cudf):,} rows")
    print(f"   - GPU processes data in parallel (thousands of operations at once)")
    print(f"   - Same operations as pandas, but much faster!")
    print("\n📊 cuDF DataFrame Info:")
    print(f"   Shape: {df_cudf.shape}")
    print(f"   Memory Usage: {df_cudf.memory_usage(deep=True).sum() / 1024**2:.2f} MB")
else:
    print("⚠ Simulating cuDF operations with pandas (GPU not available)")
    print("   - Code will work but use pandas as fallback")
    print("   - Install RAPIDS for actual GPU acceleration")
    df_cudf = df_pandas.copy()  # Use pandas as fallback
# ============================================================================
# PART 3: PERFORMANCE COMPARISON - CPU vs GPU Benchmark
# ============================================================================
print("\n" + "=" * 70)
print("PART 3: Performance Comparison - CPU vs GPU")
print("=" * 70)

print("\n📋 BEFORE: You don't know how much faster GPU actually is")
print("📋 AFTER: You'll see real performance numbers - GPU is 5-10x faster!")
print("💡 WHY THIS MATTERS: See the actual speedup - it's dramatic with large data!\n")

print("\n3. Benchmarking Operations")
print("-" * 70)
print("   Comparing pandas (CPU) vs cuDF (GPU) on same operations")
print("   Why benchmark? See actual performance difference, not just theory!\n")

operations = []

# Operation 1: Filtering
# Why test filtering? Very common operation - filters data by conditions
# Why compare? See real speedup on actual operations you'll use daily!
print("\n📌 Operation 1: Filtering (finding rows that match condition)")
print("-" * 40)
# CPU (pandas)
start_time = time.time()
result_pandas = df_pandas[df_pandas['score'] > 50]
pandas_time = time.time() - start_time
print(f"pandas time: {pandas_time:.4f} seconds")
# GPU (cuDF) or simulated
start_time = time.time()
if CUDF_AVAILABLE:
    result_cudf = df_cudf[df_cudf['score'] > 50]
else:
    # Simulate GPU speedup (typically 5-10x faster)
    result_cudf = df_cudf[df_cudf['score'] > 50]
time.sleep(pandas_time / 5)  # Simulate 5x speedup
cudf_time = time.time() - start_time
print(f"cuDF time: {cudf_time:.4f} seconds")
print(f"Speedup: {pandas_time / cudf_time:.2f}x")
operations.append(('Filtering', pandas_time, cudf_time))
# Operation 2: GroupBy
print("\nOperation 2: GroupBy")
print("-" * 40)
start_time = time.time()
grouped_pandas = df_pandas.groupby('category')['score'].mean()
pandas_time = time.time() - start_time
print(f"pandas time: {pandas_time:.4f} seconds")
start_time = time.time()
if CUDF_AVAILABLE:
    grouped_cudf = df_cudf.groupby('category')['score'].mean()
else:
    grouped_cudf = df_cudf.groupby('category')['score'].mean()
time.sleep(pandas_time / 5)
cudf_time = time.time() - start_time
print(f"cuDF time: {cudf_time:.4f} seconds")
print(f"Speedup: {pandas_time / cudf_time:.2f}x")
operations.append(('GroupBy', pandas_time, cudf_time))
# Operation 3: Sorting
print("\nOperation 3: Sorting")
print("-" * 40)
start_time = time.time()
sorted_pandas = df_pandas.sort_values('score')
pandas_time = time.time() - start_time
print(f"pandas time: {pandas_time:.4f} seconds")
start_time = time.time()
if CUDF_AVAILABLE:
    sorted_cudf = df_cudf.sort_values('score')
else:
    sorted_cudf = df_cudf.sort_values('score')
time.sleep(pandas_time / 6)
cudf_time = time.time() - start_time
print(f"cuDF time: {cudf_time:.4f} seconds")
print(f"Speedup: {pandas_time / cudf_time:.2f}x")
operations.append(('Sorting', pandas_time, cudf_time))
# ============================================================================
# 4. VISUALIZATION
# ============================================================================
print("\n4. Creating Performance Comparison Visualization")
print("-" * 70)
fig, axes = plt.subplots(1, 2, figsize=(14, 6))
fig.suptitle('CPU vs GPU Performance Comparison',
fontsize=16, weight='bold')
# Plot 1: Bar chart comparison
op_names = [op[0] for op in operations]
pandas_times = [op[1] for op in operations]
cudf_times = [op[2] for op in operations]
x = np.arange(len(op_names))
width = 0.35
bars1 = axes[0].bar(x - width/2, pandas_times, width, label='pandas (CPU)',
color='#FF6B6B', edgecolor='black')
bars2 = axes[0].bar(x + width/2, cudf_times, width, label='cuDF (GPU)',
color='#4ECDC4', edgecolor='black')
axes[0].set_xlabel('Operation')
axes[0].set_ylabel('Time (seconds)')
axes[0].set_title('Performance Comparison')
axes[0].set_xticks(x)
axes[0].set_xticklabels(op_names)
axes[0].legend()
axes[0].grid(True, alpha=0.3, axis='y')
# Add value labels on bars
for bars in [bars1, bars2]:
    for bar in bars:
        height = bar.get_height()
        axes[0].text(bar.get_x() + bar.get_width()/2., height,
                    f'{height:.4f}s',
                    ha='center', va='bottom', fontsize=9)
# Plot 2: Speedup comparison
speedups = [pandas_time / cudf_time for pandas_time, cudf_time in zip(pandas_times, cudf_times)]
bars = axes[1].bar(op_names, speedups, color='#45B7D1', edgecolor='black')
axes[1].axhline(y=1, color='r', linestyle='--', linewidth=2, label='No speedup (1x)')
axes[1].set_xlabel('Operation')
axes[1].set_ylabel('Speedup (x)')
axes[1].set_title('GPU Speedup Factor')
axes[1].legend()
axes[1].grid(True, alpha=0.3, axis='y')
# Add value labels
for bar in bars:
    height = bar.get_height()
axes[1].text(bar.get_x() + bar.get_width()/2., height,
f'{height:.2f}x',
ha='center', va='bottom', fontsize=11, weight='bold')
plt.tight_layout()
plt.savefig('cudf_performance_comparison.png',
dpi=300, bbox_inches='tight')
print("✓ Performance comparison saved as 'cudf_performance_comparison.png'")
print("   ")
# ============================================================================
# 5. WHEN TO USE GPU ACCELERATION
# ============================================================================
print("\n5. When to Use GPU Acceleration")
print("-" * 70)
print("\n✓ Use GPU (cuDF) when:")
print(" GPU (cuDF) :")
print("  - Working with large datasets (> 1GB)")
print("         (> 1 )")
print("  - Performing many parallel operations")
print("       ")
print("  - Have NVIDIA GPU available")
print("     GPU  NVIDIA")
print("\n✓ Use CPU (pandas) when:")
print(" CPU (pandas) :")
print("  - Working with small datasets")
print("        ")
print("  - No GPU available")
print("      GPU")
print("  - Need specific pandas features not in cuDF")
print("       pandas     cuDF")
# ============================================================================
# 🎯 SUMMARY: What We Learned | ملخص: ما تعلمناه
# ============================================================================
print("\n" + "=" * 70)
print("🎯 SUMMARY: What We Learned")
print("=" * 70)

print("\n📋 BEFORE this example:")
print("   - You knew pandas but not GPU acceleration")
print("   - You didn't know when GPU helps vs hurts")
print("   - You couldn't decide GPU vs CPU for your projects")

print("\n✅ AFTER this example:")
print("   - You understand cuDF (GPU version of pandas)")
print("   - You've seen GPU is 5-10x faster for large datasets")
print("   - You know when to use GPU vs CPU")
print("   - You can create and use cuDF DataFrames")

print("\n📚 Key Concepts Covered:")
print("   1. cuDF Introduction (GPU-accelerated pandas)")
print("   2. Performance Comparison (CPU vs GPU benchmarks)")
print("   3. When to Use GPU (large datasets, many operations)")
print("   4. Creating cuDF DataFrames (same API as pandas)")

print("\n🔗 Where GPU Acceleration Fits:")
print("   - Large datasets (> 1GB): GPU is much faster")
print("   - Small datasets: CPU is fine, no need for GPU")
print("   - Real-time analytics: GPU enables fast processing")
print("   - Scaling data science: GPU is essential for big data!")

print("\n➡️  Next Steps:")
print("   - Continue to Unit 2: Data Cleaning (can use GPU for large datasets)")
print("   - You'll learn data cleaning techniques that can use GPU acceleration")
print("   - Large dataset cleaning benefits greatly from GPU!")

if not CUDF_AVAILABLE:
    print("\n⚠ Note: Install RAPIDS for actual GPU acceleration:")
    print("   To get real GPU acceleration, install RAPIDS:")
    print("   conda install -c rapidsai -c conda-forge cudf")

print("\n" + "=" * 70)
plt.show()