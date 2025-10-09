import warnings
warnings.filterwarnings("ignore", category=UserWarning)

import gymnasium as gym
from stable_baselines3 import PPO

def main():
    env = gym.make("CartPole-v1")
    model = PPO("MlpPolicy", env, verbose=1)
    model.learn(total_timesteps=10000)
    model.save("ppo_cartpole_model")
    env.close()
    print("✅ PPO training complete and model saved.")

if __name__ == "__main__":
    main()
