# 💼 Interview Q&A – Lab 09 (Horovod Distributed ML)

1. **Q:** What is Horovod?
   **A:** Horovod is an open-source library for distributed deep learning training, initially developed by Uber.

2. **Q:** How does Horovod communicate between processes?
   **A:** It uses MPI, Gloo, or NCCL for collective communication like allreduce.

3. **Q:** What is the role of MPI here?
   **A:** MPI launches multiple parallel processes and allows them to share gradients efficiently.

4. **Q:** What is the main advantage of Horovod?
   **A:** Simplified scaling across CPUs/GPUs without modifying model code extensively.

5. **Q:** What does `HOROVOD_CPU_OPERATIONS=GLOO` mean?
   **A:** It tells Horovod to use the Gloo backend optimized for CPU operations.

6. **Q:** How do we verify Horovod installation?
   **A:** By running a simple MPI test (`test_mpi_rank.py`) to confirm process communication.

7. **Q:** Can Horovod run without GPUs?
   **A:** Yes. Gloo backend enables pure CPU execution.

8. **Q:** What TensorFlow version is compatible with Horovod 0.28.1?
   **A:** TensorFlow 2.15–2.16.1.

9. **Q:** What are common build issues on Ubuntu 24.04?
   **A:** Missing CMake, missing `<string>` headers, or GCC incompatibility.

10. **Q:** Why is distributed training important?
    **A:** It enables faster training across multiple devices or nodes for large models.
