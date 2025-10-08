#!/bin/bash
# Step 1: Train models of different sizes
python3 train_small.py
python3 train_medium.py
python3 train_large.py

# Step 2: Verify generated models and screenshots
ls -lh screenshots/
