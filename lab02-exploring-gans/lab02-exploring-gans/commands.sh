#!/bin/bash
mkdir ~/lab02-exploring-gans && cd ~/lab02-exploring-gans
python3 -m venv gan-env
source gan-env/bin/activate
pip install tensorflow matplotlib numpy
python3 gan_lab.py
