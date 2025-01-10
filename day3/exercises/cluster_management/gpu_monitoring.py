import GPUtil
import time
from datetime import datetime
import json
from typing import Dict, List
import logging

class GPUMonitor:
    def __init__(self, log_file: str = "gpu_monitor.log"):
        logging.basicConfig(
            filename=log_file,
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s'
        )
        self.logger = logging.getLogger(__name__)
    
    def collect_metrics(self) -> List[Dict]:
        '''Collect GPU metrics'''
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
            self.logger.error(f"Error collecting metrics: {e}")
            return []
    
    def monitor_with_alerts(self, interval: int = 60, 
                          temp_threshold: float = 80.0,
                          util_threshold: float = 90.0):
        '''Monitor GPUs with alerting'''
        try:
            while True:
                metrics = self.collect_metrics()
                for gpu in metrics:
                    # Check temperature
                    if gpu['temperature'] > temp_threshold:
                        self.logger.warning(
                            f"High temperature on GPU {gpu['id']}: {gpu['temperature']}°C"
                        )
                    
                    # Check utilization
                    if gpu['load'] > util_threshold:
                        self.logger.warning(
                            f"High utilization on GPU {gpu['id']}: {gpu['load']}%"
                        )
                    
                    # Log metrics
                    self.logger.info(f"GPU {gpu['id']} metrics: {json.dumps(gpu)}")
                
                time.sleep(interval)
        
        except KeyboardInterrupt:
            self.logger.info("Monitoring stopped by user")
        except Exception as e:
            self.logger.error(f"Monitoring error: {e}")

if __name__ == "__main__":
    monitor = GPUMonitor()
    monitor.monitor_with_alerts()
