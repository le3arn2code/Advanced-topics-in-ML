from stable_baselines3 import PPO

def main():
    model = PPO.load("ppo_cartpole_model")
    print("✅ PPO model loaded successfully!")

if __name__ == "__main__":
    main()
