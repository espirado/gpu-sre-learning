import iperf3
import json
import time
from typing import Dict, List
import logging

class NetworkBenchmark:
    def __init__(self, server: str, port: int = 5201):
        self.server = server
        self.port = port
        self.logger = logging.getLogger(__name__)
    
    def run_benchmark(self, duration: int = 10) -> Dict:
        '''Run network performance benchmark'''
        try:
            client = iperf3.Client()
            client.duration = duration
            client.server_hostname = self.server
            client.port = self.port
            
            result = client.run()
            
            return {
                'bandwidth_mbps': result.sent_Mbps,
                'retransmits': result.retransmits,
                'jitter_ms': result.jitter_ms,
                'lost_packets': result.lost_packets,
                'lost_percent': result.lost_percent
            }
        
        except Exception as e:
            self.logger.error(f"Benchmark error: {e}")
            return {}
    
    def monitor_network_performance(self, interval: int = 300):
        '''Continuous network monitoring'''
        try:
            while True:
                results = self.run_benchmark()
                self.logger.info(f"Network performance: {json.dumps(results)}")
                time.sleep(interval)
        
        except KeyboardInterrupt:
            self.logger.info("Monitoring stopped by user")
        except Exception as e:
            self.logger.error(f"Monitoring error: {e}")

def main():
    # Configure logging
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )
    
    # Run network benchmark
    benchmark = NetworkBenchmark(server='storage-server')
    print("Running network benchmark...")
    results = benchmark.run_benchmark()
    print(f"Results: {json.dumps(results, indent=2)}")

if __name__ == "__main__":
    main()
