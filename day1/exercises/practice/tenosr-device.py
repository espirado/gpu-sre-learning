# Basic GPU Info and Memory Management
import torch

def explore_gpu_basics():
    # Check CUDA availability
    print(f"CUDA Available: {torch.cuda.is_available()}")
    if torch.cuda.is_available():
        # Get device count and properties
        device_count = torch.cuda.device_count()
        print(f"Number of GPUs: {device_count}")
        
        # Get current device properties
        current_device = torch.cuda.current_device()
        print(f"Current Device ID: {current_device}")
        print(f"Device Name: {torch.cuda.get_device_name(current_device)}")
        
        # Memory Information
        print(f"Total Memory: {torch.cuda.get_device_properties(current_device).total_memory / 1e9:.2f} GB")
        print(f"Memory Allocated: {torch.cuda.memory_allocated() / 1e9:.2f} GB")
        print(f"Memory Cached: {torch.cuda.memory_reserved() / 1e9:.2f} GB")

# Memory Transfer Example
def memory_transfer_example():
    # Create tensor on CPU
    cpu_tensor = torch.randn(1000, 1000)
    
    # Time the transfer to GPU
    start = torch.cuda.Event(enable_timing=True)
    end = torch.cuda.Event(enable_timing=True)
    
    start.record()
    gpu_tensor = cpu_tensor.cuda()  # Transfer to GPU
    end.record()
    
    torch.cuda.synchronize()  # Wait for completion
    print(f"Transfer Time: {start.elapsed_time(end):.2f} ms")