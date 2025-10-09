import gymnasium as gym
from gymnasium.envs.classic_control.cartpole import CartPoleEnv

class CustomCartPole(CartPoleEnv):
    def step(self, action):
        state, reward, done, truncated, info = super().step(action)
        reward += 1  # Bonus reward for each step survived
        return state, reward, done, truncated, info

if __name__ == "__main__":
    env = CustomCartPole()
    obs, info = env.reset()
    print("✅ Custom environment created successfully.")
