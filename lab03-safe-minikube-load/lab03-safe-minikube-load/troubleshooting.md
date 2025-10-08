🧩 Problem:
Minikube crashed with "Killed" message while loading mnist_model (3.9 GB).

📋 Root Cause:
Kernel OOM killer terminated the process due to memory exhaustion.

🛠️ Resolution:
Used disk-based safe method:
  sudo docker save mnist_model:latest -o mnist_model.tar
  minikube image load mnist_model.tar

🎯 Result:
Successfully imported the image into Minikube.
No system freeze or kernel kill event afterward.
