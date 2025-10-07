#!/usr/bin/env bash
if [ -z "$VIRTUAL_ENV" ]; then
  echo "Activate venv: source ~/ml_env/bin/activate"; exit 1
fi
sudo ufw allow 8888/tcp >/dev/null 2>&1 || true
exec python -m notebook
