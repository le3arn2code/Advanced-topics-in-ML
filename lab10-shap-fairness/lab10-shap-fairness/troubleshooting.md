# Troubleshooting – Lab 10 (SHAP Fairness)

1) PEP 668 / externally managed environment
   - Use pip flag: `--break-system-packages`

2) Matplotlib backend (no GUI)
   - We force `Agg` backend to save figures: no display needed.

3) TensorFlow install slow on t3.medium
   - This is CPU-only wheel; allow ~2–5 minutes.

4) Memory spikes during SHAP
   - We limit background to 200 rows and test to 50 rows.

5) Network issues fetching Adult dataset
   - Re-run later or mirror the CSV locally and change the URL.
