# Troubleshooting (Final)
- `jupyter: command not found` → install in venv, use `python -m notebook`.
- `python: can't open file '~/code/test_env.py'` → create the file first.
- PyTorch CPU wheels → `python -m pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu`.
- OpenCV GUI deps → use `opencv-python-headless` on servers.
- Not reachable → set `c.ServerApp.ip='0.0.0.0'`, allow `ufw 8888/tcp`, check cloud SGs.
