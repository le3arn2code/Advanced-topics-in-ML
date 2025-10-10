# Advanced Topics in Machine Learning

This repository contains a collection of advanced, hands-on labs covering modern machine learning (ML) concepts, distributed computing, secure model deployment, and explainable AI. Each lab is designed to be **GitHub-ready**, reproducible, and optimized for **cloud-based environments** (t3.medium/t3.micro instances or equivalent VMs).

---

## 🚀 Repository Overview

**Repository:** [le3arn2code/Advanced-topics-in-ML](https://github.com/le3arn2code/Advanced-topics-in-ML)

This repo continues the structured series from *Python-Programming-for-Machine-Learning-II*, focusing on practical, security-aware, and production-oriented ML workflows.

Each lab includes:
- `README.md`: Theory, objective, and implementation details.
- `commands.sh`: Complete executable commands used during setup and execution.
- `troubleshooting.md`: Real errors encountered and their resolutions.
- `interview_qna.md`: Ten curated interview-style questions with answers.
- `screenshots/`: Real execution screenshots.
- `layman_explanation.md`: Simplified explanation of the lab for conceptual understanding.

---

## 🧠 Labs Summary

### **Lab 01 – Secure ML Environment Setup**
Set up an isolated and hardened ML development environment with restricted privileges, data encryption, and runtime safety for AI experiments.

### **Lab 02 – Exploring Generative Adversarial Networks (GANs)**
Understand the generator-discriminator architecture, train a basic GAN using TensorFlow, and visualize generated outputs.

### **Lab 03 – Safe Minikube Image Load (Low Memory Systems)**
Deploy and load ML containers safely on Minikube within constrained resources, ensuring isolation and resource limits.

### **Lab 04 – Model Training Performance Analysis**
Compare CPU-based training across small, medium, and large datasets using TensorFlow/Keras. Collect performance metrics and visualize resource utilization.

### **Lab 05 – Implementing Zero Trust Authentication with SPIFFE & SPIRE**
Integrate Zero Trust identity using SPIFFE/SPIRE for microservices in ML environments, ensuring secure service-to-service communication.

### **Lab 06 – Continuous Integration & Deployment (CI/CD) for ML with GitLab CI/CD**
Automate ML pipeline stages — data preprocessing, training, model packaging, and deployment — using GitLab CI/CD.

### **Lab 07 – Reinforcement Learning with Gymnasium (PPO & DQN)**
Implement reinforcement learning agents using Proximal Policy Optimization (PPO) and Deep Q-Networks (DQN) to learn game-like environments.

### **Lab 08 – Advanced NLP with DistilBERT and Flask API**
Fine-tune DistilBERT for text classification and expose model inference via a Flask REST API endpoint.

### **Lab 09 – Distributed Machine Learning with Horovod (CPU-only)**
Scale deep learning training using Horovod on multi-core CPU setups, focusing on communication efficiency and parallelism.

### **Lab 10 – Model Fairness & Explainability with SHAP**
Interpret deep learning models using SHAP to assess feature importance, bias, and fairness. Includes ethical evaluation of AI decisions.

---

## 🧩 Repository Structure

```bash
Advanced-topics-in-ML/
├── lab01-secure-ml-environment/
├── lab02-exploring-gans/
├── lab03-safe-minikube-load/
├── lab04-model-training-performance/
├── lab05-zero-trust-spiffe/
├── lab06-continuous-integration-deployment-ml-gitlab-cicd/
├── lab07-reinforcement-learning/
├── lab08-advanced-nlp/
├── lab09-distributed-ml-horovod/
└── lab10-shap-fairness/
```

Each lab directory includes subfolders:
```bash
├── code/
├── scripts/
├── screenshots/
├── README.md
├── commands.sh
├── troubleshooting.md
├── interview_qna.md
└── layman_explanation.md
```

---

## ⚙️ Requirements

- **Environment:** Ubuntu 22.04 / Cloud VM (t3.medium or higher)
- **Python:** ≥ 3.12
- **Frameworks:** TensorFlow, PyTorch, Keras, Horovod, Transformers, Flask
- **Tools:** AWS CLI, Docker, GitLab CI/CD, Minikube, jq, OpenSSL
- **No `apt upgrade` step included** (keeps labs lightweight and safe for cloud environments)

---

## 🧰 Development Workflow

1. **Clone the repo:**
   ```bash
   git clone https://github.com/le3arn2code/Advanced-topics-in-ML.git
   cd Advanced-topics-in-ML
   ```
2. **Navigate to a lab:**
   ```bash
   cd lab09-distributed-ml-horovod
   ```
3. **Execute commands:**
   ```bash
   bash commands.sh
   ```
4. **Review troubleshooting logs:**
   ```bash
   cat troubleshooting.md
   ```

---

## 💬 Learning Philosophy

> *"Real learning happens when theory meets errors and you fix them."*  
Each lab captures both success and failure states, teaching resilience and problem-solving for professional AI/ML engineering.

---

## 📦 Version Control and Contribution

- All labs follow a consistent structure (`labXX-topic` naming convention).
- Tags are used to version milestones, e.g.:
  ```bash
  git add .
  git commit -m "Add Lab 10 – Model Fairness & Explainability with SHAP"
  git tag lab10
  git push origin main --tags
  ```
- Pull requests are welcome for improvements or bug fixes.

---

## 🏁 Author

**Engineer DevOps (Haroon ur Rasheed)**  
🚀 *Building the future of AI/ML through structured, reproducible labs.*  
📂 [GitHub Profile](https://github.com/le3arn2code)

---

## 📘 License

This project is licensed under the **MIT License** – see the [LICENSE](LICENSE) file for details.

---

## 🔗 Related Repositories

- [Python-Programming-for-Machine-Learning-II](https://github.com/le3arn2code/Python-Programming-for-Machine-Learning-II)
- [Vagrant](https://github.com/le3arn2code/vagrant)
- [Docker Deep Dive](https://github.com/le3arn2code/docker_deep_dive)

---

**Last Updated:** October 2025
