import psutil
import GPUtil
from datetime import datetime
import json
import time

class GPUMetricsCollector:
    '''
    Exercise: Implement GPU metrics collection system
    '''
    def __init__(self, collection_interval=1):
        self.collection_interval = collection_interval
        self.metrics_history = []
    
    def collect_gpu_metrics(self):
        try:
            gpus = GPUtil.getGPUs()
            metrics = []
            
            for gpu in gpus:
                metrics.append({
                    'id': gpu.id,
                    'name': gpu.name,
                    'load': gpu.load * 100,
                    'memory_used': gpu.memoryUsed,
                    'memory_total': gpu.memoryTotal,
                    'temperature': gpu.temperature,
                    'timestamp': datetime.now().isoformat()
                })
            
            return metrics
        except Exception as e:
            print(f"Error collecting GPU metrics: {e}")
            return None
    
    def start_collection(self, duration=None):
        try:
            start_time = time.time()
            while True:
                metrics = self.collect_gpu_metrics()
                if metrics:
                    self.metrics_history.append(metrics)
                    print(f"Collected metrics for {len(metrics)} GPUs")
                
                if duration and (time.time() - start_time) >= duration:
                    break
                    
                time.sleep(self.collection_interval)
        
        except KeyboardInterrupt:
            print("Stopping metrics collection...")
        finally:
            self.save_metrics()
    
    def save_metrics(self):
        if self.metrics_history:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"gpu_metrics_{timestamp}.json"
            
            with open(filename, 'w') as f:
                json.dump(self.metrics_history, f, indent=2)
            print(f"Metrics saved to {filename}")

if __name__ == "__main__":
    collector = GPUMetricsCollector(collection_interval=1)
    # Collect for 60 seconds
    collector.start_collection(duration=60)
