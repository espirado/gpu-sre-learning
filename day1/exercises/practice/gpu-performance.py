# Basic Performance Comparison
import torch
import time

def compare_cpu_gpu_performance(size=1000):
    # Create random matrices
    a_cpu = torch.randn(size, size)
    b_cpu = torch.randn(size, size)
    
    # CPU Computation
    start_time = time.time()
    c_cpu = torch.mm(a_cpu, b_cpu)
    cpu_time = time.time() - start_time
    
    # GPU Computation
    if torch.cuda.is_available():
        a_gpu = a_cpu.cuda()
        b_gpu = b_cpu.cuda()
        
        # Warm-up run
        c_gpu = torch.mm(a_gpu, b_gpu)
        torch.cuda.synchronize()
        
        # Timed run
        start_time = time.time()
        c_gpu = torch.mm(a_gpu, b_gpu)
        torch.cuda.synchronize()
        gpu_time = time.time() - start_time
        
        print(f"Matrix Size: {size}x{size}")
        print(f"CPU Time: {cpu_time:.4f} seconds")
        print(f"GPU Time: {gpu_time:.4f} seconds")
        print(f"Speedup: {cpu_time/gpu_time:.2f}x")