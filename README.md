CityTwin — Production-ready starter repository

This repository contains a production-ready starter for the CityTwin multi-modal
foundation model and data-fusion system. It includes:

- Multimodal model implementations (small & large GPU-ready)
- Training scripts: quick, prototype, distributed (DeepSpeed / torchrun)
- FastAPI serving with model endpoints
- Dockerfiles: cpu (local) and gpu (production)
- Terraform skeleton: ECR, S3, EKS, IAM, ASG for GPU builders
- Helm chart and k8s manifests for deployment
- GitHub Actions workflows (CI, CD, CodeBuild orchestrator via OIDC)
- NeRF integration guide & server stub
- ViT + transformer text encoder integration
- Runbook, cost estimates, and security guidance

See docs/quickstart.md for immediate steps.
