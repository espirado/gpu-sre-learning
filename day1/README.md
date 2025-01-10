# Day 1: GPU Basics and System Programming

## Environment Setup
- Google Colab GPU activation
- Basic GPU operations and verification
- System metrics collection

## Exercises
1. GPU Environment Check
   ```python
   # Verify GPU availability
   import torch
   print(torch.cuda.is_available())
   print(torch.cuda.get_device_name(0))
   ```

2. Matrix Operations Benchmark
   - Compare CPU vs GPU performance
   - Measure memory transfer overhead
   - Profile different matrix sizes

## Tasks
1. Create a metrics collector
2. Implement parallel processing
3. Build a resource monitor

## Success Criteria
- Working GPU environment
- Successful benchmarks
- Basic metrics collection
