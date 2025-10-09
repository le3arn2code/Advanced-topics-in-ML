# Lab 09 – Distributed Machine Learning with Horovod (CPU-only)

## 🎯 Objective
Implement distributed training on TensorFlow using **Horovod (CPU-only)**.  
This lab demonstrates multi-process training using MPI on a t3.medium instance.

## ⚙️ Environment
- **OS:** Ubuntu 24.04 LTS
- **Instance Type:** t3.medium (2 vCPU, 4GB RAM)
- **Python:** 3.12.x
- **TensorFlow:** 2.16.1 (CPU-only)
- **Horovod:** 0.28.1 (built with Gloo backend)

---

## 🧩 Steps Overview
1. Install prerequisites and dependencies.
2. Install TensorFlow CPU.
3. Build Horovod with TensorFlow ops (CPU backend).
4. Verify MPI communication.
5. Run distributed training with Horovod.

---

## 🧱 Setup Commands
See `commands.sh` for the full reproducible command list.

---

## 🧪 Verification
```bash
mpirun --oversubscribe -np 2 python3 code/test_mpi_rank.py
```
Expected output:
```
Rank 0 OK
Rank 1 OK
```

Run training:
```bash
mpirun --oversubscribe -np 2 python3 code/train_horovod_tf.py
```

---

## 🧠 Deliverables
- `README.md` – overview & objectives  
- `commands.sh` – setup & run steps  
- `troubleshooting.md` – errors & fixes  
- `interview_qna.md` – 10 real Q&A  
- `layman_explanation.md` – simplified summary  
- `code/` – Python scripts  
- `screenshots/` – training output images  

---

✅ **This lab completes the Horovod CPU Distributed ML pipeline as per the course document.**
