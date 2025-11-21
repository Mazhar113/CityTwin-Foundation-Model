GPU & Distributed Quickstart

- Use docker/Dockerfile.gpu and docker/requirements-gpu.txt to build a GPU image on a GPU host.
- For distributed training use torchrun or DeepSpeed via scripts/torchrun_launch.sh or distributed/launch_deepspeed.sh
- Use Terraform to provision EKS and ephemeral GPU builders for CodeBuild orchestrator.
