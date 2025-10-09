#!/bin/bash
# Lab 09 - Distributed Machine Learning with Horovod (CPU-only)
# Tested on Ubuntu 24.04, Python 3.12, t3.medium (4GB RAM)

# 1️⃣ Update and install system deps (no upgrade)
sudo apt-get update -y
sudo apt-get install -y cmake gfortran openmpi-bin libopenmpi-dev

# 2️⃣ Install Python packages
pip install tensorflow==2.16.1 --break-system-packages
HOROVOD_WITH_TENSORFLOW=1 HOROVOD_CPU_OPERATIONS=GLOO HOROVOD_CMAKE=$(which cmake) pip install horovod==0.28.1 --break-system-packages --no-cache-dir

# 3️⃣ Verify installation
python3 -c "import horovod.tensorflow as hvd; print('Horovod version:', hvd.__version__)"

# 4️⃣ Run MPI test
mpirun --oversubscribe -np 2 python3 code/test_mpi_rank.py

# 5️⃣ Run training
mpirun --oversubscribe -np 2 python3 code/train_horovod_tf.py
