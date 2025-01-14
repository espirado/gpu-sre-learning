# GPU Architecture and Programming Model

## Introduction
The Graphics Processing Unit (GPU) provides much higher instruction throughput and memory bandwidth than the CPU within a similar price and power envelope.

This difference in capabilities exists because of distinct design goals:
- CPU: Optimized for executing sequential operations (threads) quickly
- GPU: Designed for executing thousands of threads in parallel

## Scalable Programming Model

Modern processor evolution has led to parallel systems becoming mainstream, with multicore CPUs and manycore GPUs. The key challenge is developing software that can scale its parallelism to utilize increasing processor cores.

### Core Abstractions
Three key abstractions form the foundation:
1. Hierarchy of thread groups
2. Shared memories
3. Barrier synchronization

These are exposed through minimal language extensions and provide:
- Fine-grained data parallelism
- Thread parallelism
- Nested within coarse-grained data parallelism
- Task parallelism

### Problem Decomposition
- Partition into coarse sub-problems (solved independently by thread blocks)
- Further divide into finer pieces (solved cooperatively by threads within block)
- Enables automatic scalability while preserving language expressivity

## Programming Model

### Kernels
- CUDA C++ extends C++ with kernel functions
- Kernels are executed N times in parallel by N different CUDA threads
- Defined using `__global__` declaration specifier
- Uses `<<<...>>>` syntax for execution configuration

### Thread Hierarchy
- `threadIdx`: 3-component vector
- Supports 1D, 2D, or 3D thread indices
- Forms thread blocks
- Limitation: threads per block (due to core memory resources)

### Memory Hierarchy
CUDA threads can access multiple memory spaces:
- Private local memory (per thread)
- Shared memory (per block)
  - Visible to all threads in block
  - Same lifetime as block
- Global memory (all threads)
- Thread blocks in cluster: read/write/atomic operations on shared memory

### Advanced Concepts
1. Heterogeneous Programming
2. Asynchronous SIMT Programming Model
   - Thread: lowest level abstraction
   - Asynchronous operations (NVIDIA Ampere GPU+)
   - Operations executed as-if by another thread

### Compute Capability
- Represented by version number ("SM version")
- Identifies supported GPU hardware features
- Used at runtime for feature detection