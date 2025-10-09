#!/usr/bin/env bash
set -e

# Lab 07 – Reinforcement Learning with Gymnasium (nano-friendly commands)
# NOTE: No apt update/upgrade. Use --break-system-packages as requested.

# 1) Prepare workspace
mkdir -p ~/lab07-reinforcement-learning/{code,screenshots}
cd ~/lab07-reinforcement-learning

# 2) Virtual environment
python3 -m venv rl_env
source rl_env/bin/activate

# 3) Install deps
pip install gymnasium[classic_control] stable-baselines3 matplotlib numpy tensorboard --break-system-packages
sudo apt install -y xvfb

# 4) Run tests/train
python3 code/test_gymnasium.py
python3 code/train_ppo.py | tee screenshots/ppo_training_output.txt
xvfb-run -s "-screen 0 640x480x24" python3 code/evaluate_agent.py
python3 code/train_tensorboard.py | tee screenshots/tensorboard_output.txt
python3 code/train_dqn.py | tee screenshots/dqn_training_output.txt
python3 code/custom_env.py
python3 code/save_load_test.py

# 5) (Optional) Pack for GitHub
zip -r lab07-reinforcement-learning.zip .
