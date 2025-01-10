import torch
import sys

def check_gpu_availability():
    '''
    Exercise: GPU Environment Check
    
    1. Check GPU availability
    2. Get GPU properties
    3. Test basic tensor operations
    4. Measure GPU vs CPU performance
    '''
    try:
        # Check CUDA availability
        cuda_available = torch.cuda.is_available()
        
        if cuda_available:
            device_count = torch.cuda.device_count()
            device_name = torch.cuda.get_device_name(0)
            cuda_version = torch.version.cuda
            
            return {
                'cuda_available': cuda_available,
                'device_count': device_count,
                'device_name': device_name,
                'cuda_version': cuda_version
            }
        return {'cuda_available': False}
    
    except Exception as e:
        print(f"Error checking GPU: {e}")
        return None

def benchmark_comparison():
    '''
    Compare CPU vs GPU performance for matrix operations
    '''
    try:
        sizes = [1000, 2000, 4000]
        results = {}
        
        for size in sizes:
            # Create random matrices
            mat1 = torch.randn(size, size)
            mat2 = torch.randn(size, size)
            
            # CPU timing
            start = time.time()
            cpu_result = torch.mm(mat1, mat2)
            cpu_time = time.time() - start
            
            # GPU timing
            if torch.cuda.is_available():
                mat1_gpu = mat1.cuda()
                mat2_gpu = mat2.cuda()
                
                start = time.time()
                gpu_result = torch.mm(mat1_gpu, mat2_gpu)
                gpu_time = time.time() - start
                
                results[size] = {
                    'cpu_time': cpu_time,
                    'gpu_time': gpu_time,
                    'speedup': cpu_time/gpu_time
                }
            else:
                results[size] = {'cpu_time': cpu_time}
        
        return results
    
    except Exception as e:
        print(f"Error in benchmark: {e}")
        return None

if __name__ == "__main__":
    print("GPU Check Results:", check_gpu_availability())
    print("Benchmark Results:", benchmark_comparison())
