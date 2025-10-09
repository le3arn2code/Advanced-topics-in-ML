# Troubleshooting (Real Issues Encountered)

## 1) `pygame` / SDL2 build error during `gym[all]` or `gym[classic_control]`
**Symptom:** messages like `sdl2-config: not found` or build failures.  
**Cause:** Headless VM lacks GUI/SDL2.  
**Fix:** Use **Gymnasium** and *do not* install `gym[all]`. We used:
```
pip install gymnasium[classic_control] --break-system-packages
```

## 2) Gym deprecation warning
**Symptom:** `Gym has been unmaintained since 2022...` shows in logs.  
**Cause:** Older libraries import `gym`.  
**Fix:** We switched our code to `import gymnasium as gym`. Training scripts also suppress these warnings for cleaner logs.

## 3) No display / `$DISPLAY` missing
**Symptom:** render errors like `No display name and no $DISPLAY`.  
**Fix:** Use headless rendering with `xvfb-run` when running plotting/evaluation:
```
sudo apt install -y xvfb
xvfb-run -s "-screen 0 640x480x24" python3 code/evaluate_agent.py
```

## 4) Verifications
- PPO training logs saved to `screenshots/ppo_training_output.txt`
- DQN training logs saved to `screenshots/dqn_training_output.txt`
- TensorBoard logs in `./logs`, with terminal output saved to `screenshots/tensorboard_output.txt`
- Reward curve saved as `screenshots/ppo_rewards.png`
