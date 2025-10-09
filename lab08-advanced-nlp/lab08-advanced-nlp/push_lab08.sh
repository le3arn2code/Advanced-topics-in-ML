#!/bin/bash
cd /d/AIOPS\ -\ drive/AIOPS\ Additional\ Labs/Advanced\ topic\ in\ ML\ II/Advanced-topics-in-ML
unzip ../lab08-advanced-nlp.zip -d lab08-advanced-nlp
cd lab08-advanced-nlp
git add .
git commit -m "Add Lab 08 – Advanced NLP with DistilBERT and Flask API"
git tag lab08
git push origin main --tags
