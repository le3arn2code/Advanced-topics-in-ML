import warnings
warnings.filterwarnings("ignore", category=UserWarning)

import gymnasium as gym
from stable_baselines3 import DQN

def main():
    env = gym.make("CartPole-v1")
    model = DQN("MlpPolicy", env, verbose=1)
    model.learn(total_timesteps=10000)
    model.save("dqn_cartpole_model")
    env.close()
    print("✅ DQN training complete and model saved.")

if __name__ == "__main__":
    main()
