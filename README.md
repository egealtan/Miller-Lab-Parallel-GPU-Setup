This is a dummy repo for moving development code to the remote machines in Miller Limb Lab.

"runArgs": ["--runtime=nvidia", "-e", "NVIDIA_VISIBLE_DEVICES=0,1"] in devcontainer.json is key to access the GPUs.

Make sure to check the nvidia driver version. Then modify the nvidia image with appropriate CUDA and CUDNN versions.
For shrek (as of 2021-12-23), CUDA 11.3 is appropriate