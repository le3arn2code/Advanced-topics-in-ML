# Layman Explanation

Think of RL like teaching a kid to balance a stick on a moving cart. The **agent** is the kid, the **environment** is the cart-and-stick world, and the **reward** is the score for keeping it upright.  

- **PPO**: gently nudges the kid’s behavior in small, safe steps so they don’t over-correct.  
- **DQN**: keeps a scoreboard of “if I do X now, how good will it be?” and picks the best move.  
- **Gymnasium**: the safe playground where the kid practices.  

We trained both strategies, logged the progress with TensorBoard, saved the model, and proved we can load it back.
