import gymnasium as gym
from stable_baselines3 import PPO
import matplotlib.pyplot as plt

def main():
    env = gym.make("CartPole-v1")
    model = PPO.load("ppo_cartpole_model")

    rewards = []
    obs, info = env.reset()
    for step in range(1000):
        action, _ = model.predict(obs)
        obs, reward, done, truncated, info = env.step(action)
        rewards.append(reward)
        if done or truncated:
            obs, info = env.reset()
    env.close()

    plt.figure(figsize=(8, 4))
    plt.plot(rewards)
    plt.title("PPO Evaluation Rewards")
    plt.xlabel("Steps")
    plt.ylabel("Reward")
    plt.tight_layout()
    plt.savefig("screenshots/ppo_rewards.png")
    plt.close()
    print("✅ Evaluation complete. Saved plot: screenshots/ppo_rewards.png")

if __name__ == "__main__":
    main()
