# Interview Q&A – Lab 10 (Fairness + SHAP)

1. Q: What problem does SHAP solve?
   A: It explains the contribution of each feature to a specific prediction and summarizes global importance.

2. Q: Why choose SHAP over simple feature importance?
   A: SHAP provides theoretically grounded additive attributions based on Shapley values.

3. Q: What’s the difference between global and local explanations?
   A: Global shows overall feature importance; local explains a single prediction’s feature contributions.

4. Q: What is Disparate Impact Ratio (DIR)?
   A: Positive prediction rate of group B divided by group A; values far from 1 indicate potential bias.

5. Q: What is Equal Opportunity?
   A: Groups should have similar TPR (recall for the positive class). We measure group TPR differences.

6. Q: How do you pick thresholds for fairness?
   A: Use domain policy (e.g., 80% rule for DIR), validate with stakeholders, and consider trade-offs.

7. Q: Why small SHAP samples?
   A: Kernel/Gradient explanations are expensive; small samples balance insight and runtime on CPU VMs.

8. Q: How do you mitigate bias if found?
   A: Rebalance data, add fairness constraints, change thresholds per group, or retrain with debiasing.

9. Q: Are explanations stable?
   A: Explanations vary with data and model; ensure robust sampling and cross-validation.

10. Q: Can explanations reveal sensitive features indirectly?
    A: Yes, take care with proxies and ensure compliance with privacy and fairness policies.
