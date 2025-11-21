#!/usr/bin/env bash
# DeepSpeed launch example (ensure deepspeed installed)
deepspeed --num_gpus 4 train_prototype.py --deepspeed_config distributed/deepspeed_config.json
