import warnings
warnings.filterwarnings("ignore", category=UserWarning)

import gymnasium as gym
from stable_baselines3 import PPO
from stable_baselines3.common.callbacks import BaseCallback

class TensorBoardCallback(BaseCallback):
    def _on_step(self):
        return True

def main():
    env = gym.make("CartPole-v1")
    model = PPO("MlpPolicy", env, verbose=1, tensorboard_log="./logs/")
    model.learn(total_timesteps=10000, callback=TensorBoardCallback())
    env.close()
    print("✅ PPO training with TensorBoard complete. Logs in ./logs/")

if __name__ == "__main__":
    main()
