#!/usr/bin/env bash
IMAGE=citytwin-gpu:local
docker build -f docker/Dockerfile.gpu -t $IMAGE .
docker save -o citytwin-gpu-image.tar $IMAGE
echo saved
