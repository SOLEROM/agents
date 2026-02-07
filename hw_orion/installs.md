# installs for full GPU LLM performance

before:
```
jetson_release
Software part of jetson-stats 4.3.2 - (c) 2024, Raffaello Bonghi
Jetpack missing!
 - Model: NVIDIA Jetson Orin NX Engineering Reference Developer Kit
 - L4T: 36.4.4
NV Power Mode[2]: 15W
Serial Number: [XXX Show with: jetson_release -s XXX]
Hardware:
 - P-Number: p3767-0000
 - Module: NVIDIA Jetson Orin NX (16GB ram)
Platform:
 - Distribution: Ubuntu 22.04 Jammy Jellyfish
 - Release: 5.15.148-tegra
jtop:
 - Version: 4.3.2
 - Service: Active
Libraries:
 - CUDA: Not installed
 - cuDNN: 9.3.0.75
 - TensorRT: Not installed
 - VPI: 3.2.4
 - Vulkan: 1.3.204
 - OpenCV: 4.5.4 - with CUDA: NO

```

## installs

```
sudo apt update
sudo apt install -y nvidia-jetpack
sudo apt install -y nvidia-container-toolkit
sudo ln -s /usr/src/tensorrt/bin/trtexec  /usr/local/bin/trtexec
sudo reboot



```

## power mode

```
# show current mode
sudo nvpmodel -q

# set max power mode (varies by Orin SKU; often 0 is max)
sudo nvpmodel -m 0

# lock clocks to max
sudo jetson_clocks
```

## verify

```
# CUDA compiler/toolkit presence
nvcc --version || true
ls -l /usr/local/cuda || true

# TensorRT tools (commonly present when installed)
which trtexec && trtexec --version

```