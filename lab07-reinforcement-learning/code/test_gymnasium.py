import gymnasium as gym

def main():
    env = gym.make("CartPole-v1")
    obs, info = env.reset()
    print("✅ Environment loaded successfully!")
    print(env)
    env.close()

if __name__ == "__main__":
    main()
