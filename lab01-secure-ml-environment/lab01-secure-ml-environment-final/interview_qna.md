# Interview Q&A — Secure ML Environment (10 with answers)
1) Virtual env purpose → Isolation and reproducibility.
2) Secure Jupyter on cloud → Password, HTTPS, firewall, allowlist, optional SSH tunnel.
3) `python -m notebook` vs `jupyter notebook` → Ensures correct venv binary.
4) CPU-only PyTorch install → torch/vision/audio via official CPU index URL.
5) Verify GPU visibility → TF list_physical_devices, Torch cuda.is_available.
6) UFW best practice → allow OpenSSH before enable.
7) Why headless OpenCV → avoid libGL issues on servers.
8) Persist Jupyter → systemd service using venv and config.
9) Common paste pitfalls → PageUp/Down keycodes `[200~`, inline comments.
10) requirements.txt content → pin core libs, add note for torch CPU index.
