# Troubleshooting Log (Real Issues)

## Environment
- **Machine:** AWS EC2 t3.medium (2 vCPUs, 4 GB RAM)  
- **OS:** Ubuntu 24.04 LTS  
- **TensorFlow:** 2.20.0 (CPU-only)

### ⚠️ Issue 1: CUDA Drivers Not Found
**Message:**  
`Could not find cuda drivers on your machine, GPU will not be used.`  
**Cause:** No GPU present on EC2 t3.medium.  
**Resolution:** TensorFlow automatically falls back to CPU mode.

### ⚠️ Issue 2: Keras Deprecation Warnings
**Messages:**
- `Do not pass an input_shape/input_dim argument...`
- `Argument 'alpha' is deprecated. Use 'negative_slope' instead.`
**Resolution:** Informational only; no impact on execution.

### ⚠️ Issue 3: Memory Allocation Warnings
**Message:**  
`Allocation of 376320000 exceeds 10% of free system memory.`  
**Cause:** TensorFlow pre‑allocates RAM for matrix operations.  
**Resolution:** Harmless on 4 GB RAM VM. Allowed to proceed without crash.

### ✅ Final Outcome
- Training completed all 5 epochs (~55 min)  
- Generator loss ≈ 0.9–1.3, Discriminator loss ≈ 0.9–1.2  
- Generated MNIST‑like digits successfully saved to `screenshots_generated_epoch_5.png`
