# 🧯 Troubleshooting

### 1. Lock Error (/var/lib/dpkg/lock)
**Fix:**
```bash
sudo systemctl stop unattended-upgrades
sudo killall -9 apt apt-get dpkg 2>/dev/null || true
sudo rm -f /var/lib/dpkg/lock-frontend /var/cache/apt/archives/lock
sudo dpkg --configure -a
```

### 2. Horovod build error (CMake < 3.13)
**Fix:**
```bash
sudo apt-get install -y cmake
```

### 3. Compiler `<string>` / `<stdexcept>` errors
**Fix:** Use Horovod 0.28.1 with CMake 3.13+ (auto handled in this lab).

### 4. Out-of-memory during build
Reduce parallel jobs:
```bash
export MAKEFLAGS='-j1'
```

### 5. TensorFlow not using CPU threads
Use:
```bash
import tensorflow as tf
tf.config.threading.set_intra_op_parallelism_threads(2)
```
