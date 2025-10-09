#!/bin/bash
python3 -m venv nlp_env
source nlp_env/bin/activate
pip install torch transformers datasets flask
python3 code/train_bert_imdb.py | tee screenshots/train_output.txt
python3 code/save_trained_model.py
python3 code/app.py
