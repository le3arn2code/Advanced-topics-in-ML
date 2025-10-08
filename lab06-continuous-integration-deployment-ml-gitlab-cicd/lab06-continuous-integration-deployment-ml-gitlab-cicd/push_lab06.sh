#!/bin/bash
cd ~/my_ml_project
git add .
git commit -m "Add Lab 06 – Continuous Integration and Deployment for ML"
git tag lab06
git push origin main --tags
