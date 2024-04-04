# RAIN-GS with Python3.8, Cuda11.8

## About RAIN-GS
<a href="https://arxiv.org/abs/2403.09413"><img src="https://img.shields.io/badge/arXiv-2403.09413-%23B31B1B"></a>
<a href="https://ku-cvlab.github.io/RAIN-GS/ "><img src="https://img.shields.io/badge/Project%20Page-online-brightgreen"></a>

## Introduction
This project provides RAIN-GS with python3.8, cuda11.8. 
There are several changes in onriginal installation since the installation was not successful on my environment :<

## Installation
For environmental setup, please follow the original requirements of [3DGS](https://github.com/graphdeco-inria/gaussian-splatting). 
I installed following tools and set environment variable.

- Cuda 11.8 [from here](https://developer.nvidia.com/cuda-toolkit-archive)
- Visual Studio 2019 [from here](https://visualstudio.microsoft.com/ja/vs/older-downloads/)
  - You can use the "where cl" command in the "Developer Command Prompt for VS2019" to get the path of cl.exe. 
- Anaconda3 [from here](https://www.anaconda.com)
- ffmpeg [from here](https://ffmpeg.org/)
- COLMAP [from here](https://colmap.github.io/)
- ImageMagick [from here](https://imagemagick.org/index.php)
    - I took "ImageMagick-7.1.1-15-Q16-HDRI-x64-dll.exe"
- viewer (This project has viewer. You can install viewer by setting environment variable for viewers/bin.)

## Training

To train 3D Gaussian Splatting with RAIN-GS, you can set --ours option:

```bash
python train.py --source_path {dataset_path} --exp_name {exp_name} --eval --ours
```

For dense-small-variance (DSV) random initialization (used in the original 3D Gaussian Splatting), you can set --DSV option:
```bash
python train.py --source_path {dataset_path} --exp_name {exp_name} --eval --DSV
```

If exp_name is spacified, the output will be as follows: output/{exp_name} .


## Acknowledgement

I would like to acknowledge the contributions of [3D Gaussian Splatting](https://github.com/graphdeco-inria/gaussian-splatting) and [RAIN-GS](https://github.com/KU-CVLAB/RAIN-GS) for open-sourcing the official codes for 3DGS! 
