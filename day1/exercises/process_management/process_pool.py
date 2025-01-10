from multiprocessing import Pool
import torch
import time
import numpy as np

def gpu_task(data):
    '''
    Exercise: Implement GPU task processing
    '''
    try:
        # Convert input to tensor and move to GPU
        tensor = torch.tensor(data).cuda()
        
        # Simulate complex computation
        time.sleep(0.1)
        result = tensor * 2
        
        return result.cpu().numpy()
    
    except Exception as e:
        print(f"Error in GPU task: {e}")
        return None

class GPUTaskManager:
    def __init__(self, num_processes=4):
        self.pool = Pool(processes=num_processes)
    
    def process_batch(self, data_batch):
        try:
            results = self.pool.map(gpu_task, data_batch)
            return [r for r in results if r is not None]
        
        except Exception as e:
            print(f"Error processing batch: {e}")
            return []
    
    def cleanup(self):
        self.pool.close()
        self.pool.join()

def main():
    # Test implementation
    manager = GPUTaskManager(num_processes=2)
    
    # Create sample data
    data_batch = [np.random.rand(100) for _ in range(10)]
    
    try:
        # Process data
        results = manager.process_batch(data_batch)
        print(f"Processed {len(results)} tasks successfully")
    
    finally:
        manager.cleanup()

if __name__ == "__main__":
    main()
