# Lab 03 – Safe Minikube Image Load (Low Memory Systems)

This lab demonstrates how to load large Docker images (like TensorFlow-based 3.9 GB containers) into Minikube **safely**, even on low-memory EC2 instances (e.g., t3.medium).

## 🧠 Objective
Prevent system freezes and “Killed” messages caused by OOM (Out-of-Memory) during `minikube image load`.

## 🧩 Steps Performed
1. Verified system memory (`free -m`)
2. Detected insufficient memory (~3.8 GB)
3. Ran `minikube image load mnist_model:latest` → Result: `Killed`
4. Diagnosed with `sudo dmesg | tail -20` → Out of memory logs
5. Applied fix via two-step disk-based load
6. Automated with `safe_minikube_load.sh`

## 🧱 Files
- `safe_minikube_load.sh` – Main script
- `commands.sh` – One-liner execution
- `troubleshooting.md` – Issue + Fix
- `interview_qna.md` – 10 DevOps Q&As
- `layman_explanation.md` – Beginner-friendly view
- `screenshots/` – Contains OOM evidence

## ✅ Output Example
```
mnist_model   latest   43123559786a   3.92GB
```

## 🧰 Environment
Ubuntu 24.04 EC2 (t3.medium), Minikube v1.37.0 (Docker driver)
