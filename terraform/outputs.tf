output "ecr_repo_url" { value = aws_ecr_repository.citytwin.repository_url }
output "s3_bucket" { value = aws_s3_bucket.citytwin_data.bucket }
