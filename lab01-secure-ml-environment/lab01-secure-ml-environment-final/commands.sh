#!/usr/bin/env bash
set -e

# System prep
sudo apt update && sudo apt upgrade -y
sudo apt install -y build-essential dkms curl git wget software-properties-common ufw fail2ban

# Security
sudo ufw allow OpenSSH
sudo ufw --force enable
sudo systemctl enable --now fail2ban

# Python (optional 3.9 toolchain)
sudo add-apt-repository -y ppa:deadsnakes/ppa || true
sudo apt update || true
sudo apt install -y python3.9 python3.9-venv python3.9-dev python3-pip || true

# Venv
python3 -m venv "$HOME/ml_env"
source "$HOME/ml_env/bin/activate"

# Jupyter + libs
python -m pip install --upgrade pip
python -m pip install jupyter notebook ipykernel
python -m pip install numpy pandas scikit-learn matplotlib seaborn tensorflow
python -m pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu
python -m pip install opencv-python-headless pillow keras

# Verifier
mkdir -p "$HOME/code"
cat > "$HOME/code/test_env.py" <<'PY'
#!/usr/bin/env python3
def main():
    import sys
    print("Python:", sys.version)
    try:
        import numpy as np; print("NumPy:", np.__version__)
        import pandas as pd; print("Pandas:", pd.__version__)
        import matplotlib; print("Matplotlib:", matplotlib.__version__)
        import seaborn as sns; print("Seaborn:", sns.__version__)
        import sklearn; print("scikit-learn:", sklearn.__version__)
    except Exception as e:
        print("Core libs import error:", e)
    try:
        import tensorflow as tf
        print("TensorFlow:", tf.__version__)
        print("TF GPUs:", tf.config.list_physical_devices('GPU'))
    except Exception as e:
        print("TensorFlow import error:", e)
    try:
        import torch
        print("PyTorch:", torch.__version__)
        print("Torch CUDA available:", torch.cuda.is_available())
    except Exception as e:
        print("PyTorch import error:", e)
if __name__ == "__main__":
    main()
PY
chmod +x "$HOME/code/test_env.py"

# Jupyter config + password
python -m notebook --generate-config
python -m notebook password

# HTTPS
mkdir -p "$HOME/jupyter_ssl" && cd "$HOME/jupyter_ssl"
openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout jupyter.key -out jupyter.crt -subj "/CN=localhost"

CONF="$HOME/.jupyter/jupyter_notebook_config.py"
# ServerApp keys
cat >> "$CONF" << 'CFG'
c.ServerApp.certfile = u'/home/REPLACE_USER/jupyter_ssl/jupyter.crt'
c.ServerApp.keyfile  = u'/home/REPLACE_USER/jupyter_ssl/jupyter.key'
c.ServerApp.ip = '0.0.0.0'
c.ServerApp.open_browser = False
c.ServerApp.port = 8888
c.ServerApp.root_dir = u'/home/REPLACE_USER'
CFG
sed -i "s|/home/REPLACE_USER|$HOME|g" "$CONF"

# Firewall + run
sudo ufw allow 8888/tcp
# python -m notebook
