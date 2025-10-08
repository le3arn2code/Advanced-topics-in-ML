### Interview Q&A (10)

1. **Q:** What is model scaling?
   **A:** Increasing layer or neuron count to capture complex patterns.

2. **Q:** Why does a larger model take longer to train?
   **A:** More parameters = more computations per epoch.

3. **Q:** What causes out-of-memory errors?
   **A:** Model size or data batch too large for available RAM.

4. **Q:** How can you speed up training on CPU?
   **A:** Use mixed precision, fewer layers, and efficient data pipelines.

5. **Q:** Why did minikube get killed?
   **A:** OOM killer due to limited 4GB memory on instance.

6. **Q:** How to reduce Docker image size?
   **A:** Use slim base images, clear caches, and avoid unnecessary libraries.

7. **Q:** How to test model locally before Kubernetes deployment?
   **A:** Use Flask + curl prediction endpoint.

8. **Q:** What tool monitors TensorFlow performance?
   **A:** TensorBoard Profiler.

9. **Q:** Why is CPU training slower than GPU?
   **A:** GPU handles matrix multiplications in parallel.

10. **Q:** What’s the trade-off between accuracy and speed?
    **A:** Larger models give better accuracy but require more compute time.
