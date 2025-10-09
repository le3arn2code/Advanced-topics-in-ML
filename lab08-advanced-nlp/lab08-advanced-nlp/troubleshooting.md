# Troubleshooting

**Problem:** `No module named 'transformers'`
- **Fix:** Ensure the virtual environment is active: `source nlp_env/bin/activate`

**Problem:** Training restarts twice on Alnafi Cloud.
- **Fix:** Interrupt after first `eval_loss` line to prevent re-run.

**Problem:** No results folder.
- **Fix:** Create manually: `mkdir -p results` and rerun `save_trained_model.py`.
