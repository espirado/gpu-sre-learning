from typing import Dict, List
import subprocess
import json
import os

class SlurmGPUManager:
    def __init__(self):
        self.config = self._load_config()
    
    def _load_config(self) -> Dict:
        '''Load Slurm configuration for GPUs'''
        try:
            cmd = "scontrol show config"
            result = subprocess.run(cmd.split(), capture_output=True, text=True)
            return self._parse_config(result.stdout)
        except Exception as e:
            print(f"Error loading Slurm config: {e}")
            return {}
    
    def _parse_config(self, config_str: str) -> Dict:
        '''Parse Slurm configuration'''
        config = {}
        for line in config_str.splitlines():
            if "GresTypes" in line or "GPU" in line:
                key, value = line.strip().split("=")
                config[key.strip()] = value.strip()
        return config
    
    def get_gpu_nodes(self) -> List[Dict]:
        '''Get information about GPU nodes'''
        try:
            cmd = "sinfo -N --Format=nodelist,gres:30,cpus,memory,statecompact"
            result = subprocess.run(cmd.split(), capture_output=True, text=True)
            return self._parse_nodes(result.stdout)
        except Exception as e:
            print(f"Error getting GPU nodes: {e}")
            return []
    
    def submit_gpu_job(self, script_path: str, num_gpus: int = 1) -> str:
        '''Submit a GPU job to Slurm'''
        try:
            cmd = f"sbatch --gres=gpu:{num_gpus} {script_path}"
            result = subprocess.run(cmd.split(), capture_output=True, text=True)
            return result.stdout.strip()
        except Exception as e:
            print(f"Error submitting GPU job: {e}")
            return ""
    
    def monitor_gpu_jobs(self) -> List[Dict]:
        '''Monitor running GPU jobs'''
        try:
            cmd = "squeue --Format=jobid,name,username,timeused,numgpus,state -h"
            result = subprocess.run(cmd.split(), capture_output=True, text=True)
            return self._parse_jobs(result.stdout)
        except Exception as e:
            print(f"Error monitoring GPU jobs: {e}")
            return []

class BrightClusterManager:
    def __init__(self):
        self.monitoring_data = {}
    
    def get_gpu_nodes(self) -> List[Dict]:
        '''Get information about GPU nodes from Bright'''
        try:
            # Simulated for example - replace with actual BCM API calls
            return [
                {
                    'name': f'gpu-node-{i}',
                    'gpus': 4,
                    'gpu_type': 'A100',
                    'status': 'UP'
                } for i in range(4)
            ]
        except Exception as e:
            print(f"Error getting GPU nodes from BCM: {e}")
            return []
    
    def monitor_health(self) -> Dict:
        '''Monitor cluster health'''
        try:
            nodes = self.get_gpu_nodes()
            health_data = {}
            for node in nodes:
                # Simulate health checks
                health_data[node['name']] = {
                    'temperature': self._check_temperature(node['name']),
                    'utilization': self._check_utilization(node['name']),
                    'memory': self._check_memory(node['name'])
                }
            return health_data
        except Exception as e:
            print(f"Error monitoring cluster health: {e}")
            return {}

def create_example_job():
    '''Create example GPU job script'''
    job_script = '''#!/bin/bash
#SBATCH --job-name=gpu_test
#SBATCH --output=gpu_test_%j.out
#SBATCH --error=gpu_test_%j.err
#SBATCH --time=01:00:00
#SBATCH --gres=gpu:1
#SBATCH --cpus-per-task=4
#SBATCH --mem=16G

module load cuda/11.0
python /path/to/your/gpu_script.py
'''
    with open('gpu_job.sh', 'w') as f:
        f.write(job_script)

if __name__ == "__main__":
    # Test Slurm GPU management
    slurm_manager = SlurmGPUManager()
    print("GPU Nodes:", slurm_manager.get_gpu_nodes())
    
    # Test BCM integration
    bcm_manager = BrightClusterManager()
    print("Cluster Health:", bcm_manager.monitor_health())
