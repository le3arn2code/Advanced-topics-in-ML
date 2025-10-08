Q1: What caused the Minikube process to be killed?
A1: The system ran out of memory (OOM), so Linux terminated the largest process — Minikube.

Q2: How can you verify an OOM kill?
A2: Check kernel logs using `sudo dmesg | tail -20`.

Q3: How does the safe two-step load prevent this?
A3: It first exports the image to disk as a tar file, reducing memory pressure during the transfer.

Q4: Why does TensorFlow-based Docker image consume so much memory?
A4: TensorFlow images are large (~3–4 GB) and decompression temporarily doubles RAM use.

Q5: What are the benefits of using `minikube start --memory=2500mb`?
A5: It reserves only 2.5 GB for the cluster, leaving RAM for the host OS.

Q6: What happens if both host and Minikube compete for RAM?
A6: The kernel invokes OOM-killer, freezing or killing random processes.

Q7: Can you use this method for other large images?
A7: Yes, just replace the `IMAGE_NAME` variable in the script.

Q8: Why is `minikube image load` used instead of `docker push`?
A8: It directly injects the image into Minikube’s internal Docker daemon — faster and local.

Q9: What happens after the image is loaded?
A9: You can deploy it via Kubernetes manifests (e.g., deployment.yaml, service.yaml).

Q10: How would you automate this in CI/CD?
A10: Integrate the script in Jenkins or GitHub Actions pipeline before running Kubernetes deployments.
