#!/bin/bash
# Push Lab 10 to GitHub (helper)
ZIP=lab10-shap-fairness.zip
cd "$(dirname "$0")"
cd ..
zip -r "$ZIP" lab10-shap-fairness
echo "Created $ZIP"
