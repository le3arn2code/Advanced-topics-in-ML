#!/bin/bash
# Step 3: Push Lab 09 to GitHub

unzip ../lab09-distributed-ml-horovod.zip -d lab09-distributed-ml-horovod
cd lab09-distributed-ml-horovod
git add .
git commit -m "Add Lab 09 – Distributed ML with Horovod (CPU-only)"
git tag lab09
git push origin main --tags
