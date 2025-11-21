#!/usr/bin/env bash
# torchrun single-node multi-gpu example
NUM_GPUS=${1:-4}
python -m torch.distributed.run --nproc_per_node=${NUM_GPUS} train_prototype.py
