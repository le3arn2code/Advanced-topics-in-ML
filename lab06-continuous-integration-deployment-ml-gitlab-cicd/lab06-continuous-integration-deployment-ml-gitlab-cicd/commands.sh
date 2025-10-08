#!/bin/bash
sudo apt update -y
sudo apt install gitlab-runner -y
gitlab-runner register
git add .
git commit -m "Add Flask API and deploy stage"
git push origin main
nohup python3 app.py > api.log 2>&1 &
