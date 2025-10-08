### Troubleshooting Notes

**Issue:** Out-of-memory (OOM) during model training  
**Fix:** Reduce batch size, disable GPU acceleration, or switch to t3.medium.

**Issue:** Minikube OOM during image load  
**Fix:** Save model to .tar and load safely after restarting minikube.

**Issue:** TensorFlow CPU warnings  
**Fix:** Ignore GPU warnings; TensorFlow auto-falls back to CPU execution.
