# Interview Q&A on GANs

1. **Q:** What are GANs?  
   **A:** Two networks — Generator and Discriminator — trained adversarially.

2. **Q:** Why are they adversarial?  
   **A:** Because the generator tries to fool the discriminator.

3. **Q:** Dataset used?  
   **A:** MNIST handwritten digits.

4. **Q:** Loss function?  
   **A:** Binary cross‑entropy.

5. **Q:** Optimizer?  
   **A:** Adam with lr=1e‑4.

6. **Q:** Why normalize data between −1 and 1?  
   **A:** Matches `tanh` output range.

7. **Q:** Why slower on CPU?  
   **A:** No GPU acceleration.

8. **Q:** Sign of balanced training?  
   **A:** Both losses near 1.0.

9. **Q:** What happens if one dominates?  
   **A:** Mode collapse or overfitting.

10. **Q:** Real‑world use cases?  
    **A:** Image generation, art, and data augmentation.
