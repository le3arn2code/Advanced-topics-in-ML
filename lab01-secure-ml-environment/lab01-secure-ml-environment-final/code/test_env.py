#!/usr/bin/env python3
def main():
    import sys
    print("Python:", sys.version)
    try:
        import numpy as np; print("NumPy:", np.__version__)
        import pandas as pd; print("Pandas:", pd.__version__)
        import matplotlib; print("Matplotlib:", matplotlib.__version__)
        import seaborn as sns; print("Seaborn:", sns.__version__)
        import sklearn; print("scikit-learn:", sklearn.__version__)
    except Exception as e:
        print("Core libs import error:", e)
    try:
        import tensorflow as tf
        print("TensorFlow:", tf.__version__)
        print("TF GPUs:", tf.config.list_physical_devices('GPU'))
    except Exception as e:
        print("TensorFlow import error:", e)
    try:
        import torch
        print("PyTorch:", torch.__version__)
        print("Torch CUDA available:", torch.cuda.is_available())
    except Exception as e:
        print("PyTorch import error:", e)
if __name__ == "__main__":
    main()
