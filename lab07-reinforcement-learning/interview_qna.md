# Interview Q&A (10)

1. **What problem does reinforcement learning solve?**  
   RL optimizes sequential decision-making by learning a policy that maximizes expected cumulative reward through interaction with an environment.

2. **Contrast PPO and DQN.**  
   PPO is a policy-gradient method using a clipped surrogate objective—stable and effective for continuous or discrete actions.  
   DQN is a value-based method estimating Q-values with a replay buffer and target network—primarily for discrete action spaces.

3. **Why is the clipped objective important in PPO?**  
   It prevents overly large policy updates that can collapse performance, improving stability without heavy hyperparameter tuning.

4. **What are ‘done’ vs ‘truncated’ in Gymnasium?**  
   `done` indicates terminal failure/success; `truncated` indicates termination due to a time limit or external constraint.

5. **How does experience replay help DQN?**  
   It decorrelates samples, improves data efficiency, and stabilizes training by sampling mini-batches from a buffer of past transitions.

6. **When would you shape the reward and what risks exist?**  
   Shape rewards to guide learning (e.g., small survival bonus). Risks include unintended incentives (specification gaming) and slower convergence if mis-specified.

7. **How do you monitor RL training?**  
   Use TensorBoard for metrics (loss, episode length, reward), evaluation episodes with plots, and periodic checkpoints.

8. **What is the role of the discount factor γ?**  
   It trades off immediate vs. future rewards. Low γ emphasizes short-term gains; high γ values favor long-term planning.

9. **Why use Gymnasium instead of Gym today?**  
   Gymnasium is actively maintained and compatible with NumPy 2.x, while Gym is deprecated and may break on modern stacks.

10. **How would you verify a saved model works?**  
    Reload it with the same library (e.g., `PPO.load(path)`), run evaluation episodes, and compare behavior/metrics to training logs.
