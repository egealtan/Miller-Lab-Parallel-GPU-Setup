# Welcome to Ege's dummy repo

## This is a dummy repo for moving development code to the remote machines in Miller Limb Lab.

With Dockerfile and .devcontainer.json inside .devcontainer, you can easily create a remote development environment.

"runArgs": ["--runtime=nvidia", "-e", "NVIDIA_VISIBLE_DEVICES=0,1"] in devcontainer.json is key to access the GPUs.

Make sure to check the nvidia driver version. Then modify the nvidia image with appropriate CUDA and CUDNN versions.
For shrek (as of 2021-12-23), CUDA 11.3 is appropriate
Confirmed both tensorflowgpu (1.15) and pytorch (1.10) work in the container.

With this setup, the user can easily mount and edit datafiles. mount settings are found in .devcontainer.

To switch between views, use Ctrl+Shift+V in the VS Code editor.

