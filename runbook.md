Runbook: CityTwin production rollout

1. Set up AWS infra via Terraform (ECR, S3, EKS)
2. Build and push GPU Docker image using CodeBuild orchestrator -> ECR
3. Deploy to EKS via Helm
4. Configure monitoring (CloudWatch, Prometheus) and logging

Cost estimates: small dev (~$100/month), medium training cluster ($2k+), full pretraining ($50k+/month)
