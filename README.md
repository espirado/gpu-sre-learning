# GPU SRE Learning Environment Setup

## Prerequisites
- Python 3.8+
- NVIDIA GPU (local) or cloud access
- Docker with NVIDIA Container Runtime
- Basic understanding of Python, Linux systems, and containers

## Project Structure

The project is structured as follows:

```
setup_learning_env.py           # Main setup script
├── day1/                       # Day 1: GPU Basics
│   ├── exercises/
│   │   ├── system_metrics/
│   │   ├── process_management/
│   │   └── cloud_gpu/
│   └── solutions/
├── day2/                       # Day 2: Kubernetes
│   ├── exercises/
│   │   ├── config_management/
│   │   └── deployment/
│   └── solutions/
├── day3/                       # Day 3: Cluster Management
│   ├── exercises/
│   │   ├── cluster_management/
│   │   └── performance/
│   └── solutions/
├── day4/                       # Day 4: Networking & Storage
│   ├── exercises/
│   │   ├── networking/
│   │   └── storage/
│   └── solutions/
├── day5/                       # Day 5: Monitoring
│   ├── exercises/
│   │   ├── monitoring/
│   │   └── testing/
│   └── solutions/
├── weekend_project/
│   ├── gpu_monitor/
│   ├── cluster_manager/
│   └── tests/
└── docs/
    ├── cloud_setup/
    └── cluster_setup/
```

## Getting Started

1. Clone the repository:
```bash
git clone <your-repo-url>
cd gpu-sre-learning
```

2. Create and activate virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
.\venv\Scripts\activate   # Windows
```

3. Install requirements:
```bash
pip install -r requirements.txt
```

## Daily Exercises

### Day 1: GPU Basics and System Programming
- System metrics collection
- GPU resource monitoring
- Process management
- Performance benchmarking

### Day 2: Kubernetes with GPUs
- GPU operator deployment
- Resource management and quotas
- Pod scheduling strategies
- Monitoring integration

### Day 3: Cluster Management
- Slurm configuration
- Bright Cluster Manager integration
- Resource optimization
- Performance profiling

### Day 4: Networking and Storage
- Container networking architectures
- High-performance storage solutions
- Network optimization
- Distributed storage patterns

### Day 5: Monitoring System
- Metrics collection
- Prometheus integration
- Alert management
- Dashboard creation

## Cloud GPU Options

### Google Colab
- Free GPU access (Tesla K80, P100)
- Setup guide: `docs/cloud_setup/colab_setup.md`
- Perfect for learning exercises

### Kaggle Kernels
- Free GPU access (Tesla P100)
- Setup guide: `docs/cloud_setup/kaggle_setup.md`
- Great for development

## Core Skills Covered

### 1. GPU Cluster Management
- Slurm administration
- BCM operations
- Resource optimization
- Performance tuning

### 2. Container Technologies
- Docker with GPU support
- Kubernetes orchestration
- Networking configurations
- Storage optimization

### 3. Monitoring and Operations
- Metrics collection
- Alert management
- Performance monitoring
- Capacity planning

## Assessment Criteria
- Code quality and style
- Error handling
- Documentation standards
- Test coverage
- Performance optimization
- Resource management

## Advanced Topics
- Large-scale Slurm deployments
- BCM cluster management
- Container networking architectures
- High-performance storage solutions
- Distributed system monitoring

## Resources
- [NVIDIA Documentation](https://docs.nvidia.com/cuda/)
- [Slurm Documentation](https://slurm.schedmd.com/)
- [Kubernetes Documentation](https://kubernetes.io/docs/)
- [BCM Documentation](https://brightcomputing.com/documentation/)

## Contributing
Please read CONTRIBUTING.md for details on our code of conduct and the process for submitting pull requests.

## License

This project is licensed under the MIT License - see the LICENSE file for details.


