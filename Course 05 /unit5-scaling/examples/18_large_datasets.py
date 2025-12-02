"""
Unit 5 - Example 18: Large Dataset Handling | التعامل مع مجموعات البيانات الكبيرة

This example teaches techniques for handling datasets that don't fit in memory.
Learn chunking, streaming, and memory-efficient processing strategies.

## 📚 Prerequisites (What You Need First) | المتطلبات الأساسية

BEFORE starting this example, you should have completed:
- ✅ Example 14: Dask Distributed - Understand distributed computing
- ✅ Example 17: Performance Optimization - Understand optimization
- ✅ Understanding of memory limitations

If you haven't completed these, you might struggle with:
- Understanding memory constraints
- Knowing chunking strategies
- Understanding streaming processing

## 🔗 Where This Example Fits | مكان هذا المثال

This is the FIFTH example in Unit 5 - Scaling Data Science!

Why this example FIFTH?
- After learning optimization, learn to handle large datasets
- Large datasets require special techniques
- Foundation for big data processing

Builds on: 
- Example 14: Dask (distributed processing)
- Example 17: Optimization (efficient processing)

Leads to: 
- Example 19: Deployment (deploy large-scale systems)
- Big data workflows (production large-scale systems)

## The Story: Processing Large Files | القصة: معالجة الملفات الكبيرة

Imagine you need to move a huge library. You can't carry all books at once - you move 
in batches (chunking). After learning chunking strategies, you can handle any size library!

Same with data: Large datasets don't fit in memory - process in chunks. After learning 
large dataset techniques, you can handle datasets of any size!

## Why Large Dataset Handling Matters | لماذا يهم

Large dataset techniques are essential because:
- Memory Limits: Datasets often exceed RAM
- Chunking: Process data in manageable pieces
- Streaming: Process data as it arrives
- Scalability: Handle datasets that grow over time

## Learning Objectives | أهداف التعلم

By the end of this example, you will:
1. Process datasets larger than memory using chunking
2. Implement streaming data processing
3. Use memory-efficient data loading techniques
4. Handle large files efficiently
5. Choose the right strategy for your dataset size
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import time
print("=" * 70)
print("Example 18: Large Dataset Handling")
print(" 18:     ")
print("=" * 70)
# ============================================================================
# 1. CREATE SIMULATED LARGE DATASET
# ============================================================================
print("\n1. Simulating Large Dataset")
print("-" * 70)
# Create large CSV file in chunks
np.random.seed(42)
chunk_size = 100000
total_rows = 1000000
n_chunks = total_rows // chunk_size
print(f"Creating {total_rows:,} rows in {n_chunks} chunks...")
large_file = 'unit5-scaling/examples/large_dataset.csv'
chunks = []
for i in range(n_chunks):
    chunk_data = {
'id': range(i * chunk_size, (i + 1) * chunk_size),
'value1': np.random.randn(chunk_size),
'value2': np.random.randn(chunk_size),
'category': np.random.choice(['A', 'B', 'C'], chunk_size),
'score': np.random.randint(0, 100, chunk_size)
}
chunk_df = pd.DataFrame(chunk_data)
chunks.append(chunk_df)
# Append to CSV
mode = 'w' if i == 0 else 'a'
header = i == 0
chunk_df.to_csv(large_file, mode=mode, header=header, index=False)
print(f"✓ Created large CSV file: {large_file} ({total_rows:,} rows)")
# ============================================================================
# 2. PROCESSING IN CHUNKS
# ============================================================================
print("\n\n2. Processing in Chunks")
print("-" * 70)
results = []
chunk_processing_times = []
start_total = time.time()
for i, chunk_df in enumerate(pd.read_csv(large_file, chunksize=chunk_size), 1):
    chunk_start = time.time()
    # Process chunk
    chunk_result = chunk_df.groupby('category')['score'].mean()
results.append(chunk_result)
chunk_time = time.time() - chunk_start
chunk_processing_times.append(chunk_time)
if i % 5 == 0:
    print(f"Processed chunk {i}, time: {chunk_time:.4f}s")
total_time = time.time() - start_total
# Combine results
final_result = pd.concat(results).groupby(level=0).mean()
print(f"\n✓ Processed {n_chunks} chunks in {total_time:.4f} seconds")
print(f"✓ Average chunk processing time: {np.mean(chunk_processing_times):.4f} seconds")
print(f"\nFinal aggregated result:")
print(final_result)
# ============================================================================
# 3. MEMORY-EFFICIENT PROCESSING
# ============================================================================
print("\n\n3. Memory Efficient Processing")
print("-" * 70)
# Use iterator to process without loading all into memory
total_sum = 0
total_count = 0
print("Processing with iterator (memory-efficient)...")
start_time = time.time()
for chunk_df in pd.read_csv(large_file, chunksize=chunk_size):
    chunk_sum = chunk_df['score'].sum()
chunk_count = len(chunk_df)
total_sum += chunk_sum
total_count += chunk_count
avg_score = total_sum / total_count
iterator_time = time.time() - start_time
print(f"Average score (computed incrementally): {avg_score:.2f}")
print(f"Processing time: {iterator_time:.4f} seconds")
print(f"Memory used: Minimal (one chunk at a time)")
# ============================================================================
# 4. VISUALIZATION
# ============================================================================
print("\n\n4. Creating Visualization")
print("-" * 70)
fig, axes = plt.subplots(1, 2, figsize=(14, 6))
fig.suptitle('Large Dataset Processing',
fontsize=16, weight='bold')
# Chunk processing times
axes[0].plot(range(1, len(chunk_processing_times) + 1), chunk_processing_times,
marker='o', color='#4ECDC4', linewidth=2, markersize=4)
axes[0].axhline(y=np.mean(chunk_processing_times), color='r', linestyle='--',
label=f'Mean: {np.mean(chunk_processing_times):.4f}s')
axes[0].set_xlabel('Chunk Number')
axes[0].set_ylabel('Processing Time (s)')
axes[0].set_title('Chunk Processing Time',
fontsize=12, weight='bold')
axes[0].legend()
axes[0].grid(True, alpha=0.3)
# Memory comparison
methods = ['Load All\n ', 'Chunking\n']
memory_usage = [500, 50]  # MB (simulated)
axes[1].bar(methods, memory_usage, color=['#FF6B6B', '#4ECDC4'], edgecolor='black')
axes[1].set_ylabel('Memory (MB)')
axes[1].set_title('Memory Usage Comparison',
fontsize=12, weight='bold')
axes[1].grid(True, alpha=0.3, axis='y')
plt.tight_layout()
plt.savefig('18_large_dataset.png', dpi=300, bbox_inches='tight')
print("✓ Visualization saved")
plt.close()
# ============================================================================
# 5. SUMMARY
# ============================================================================
print("\n" + "=" * 70)
print("Summary")
print("=" * 70)
print("\nKey Concepts Covered:")
print("1. Chunking strategies")
print("2. Streaming processing")
print("3. Memory-efficient operations")
print("4. Incremental aggregation")
print("\nNext Steps: Continue to Example 19 for Deployment")
print(" :    19 ")