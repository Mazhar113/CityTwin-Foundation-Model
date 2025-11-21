provider "aws" { region = var.aws_region }
resource "aws_ecr_repository" "citytwin" { name = var.ecr_repo_name }
resource "aws_s3_bucket" "citytwin_data" { bucket = var.s3_bucket_name }
# Add EKS resources or use module to create cluster
