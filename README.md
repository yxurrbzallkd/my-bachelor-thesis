# Repository for the Bachelor Thesis of Diana Kypybida
[APPS UCU](https://apps.ucu.edu.ua/en/) 2024

## Project Description
A repository with the basic code needed to replicate the experiments in my bachelor thesis

Structure:
1. [Missing Pixel Restoration with Singular Value Thresholding](#svt)
2. [Noisy Transmission Model](#noisy-transmission-model)
3. [SISR with RealESRGAN](#sisr)
4. [Illustrations](#illustrations)

## Requirements

See `requirements.txt`.
Also, `ffmpeg` is required for the noisy transmission model.

## SVT

Notebook `SVT.ipynb` contains a demo of missing pixel restoration with a uniform noise mask

Folder `artifacts` contains examples of artifact masks inspired by artifacts from real video frames, that can be found in the `affected` folder. All frames are from videos from `https://t.me/ssternenko` and `https://t.me/escadrone`.

Folder `svt-benchmark` contains 3 frames from two datasets used in the thesis: [kaggle dataset](https://www.kaggle.com/datasets/kmader/drone-videos) and [UCU ML lab drone objecte detection dataset](https://apps.ucu.edu.ua/en/projects/stvorennya-naboru-danyh-dlya-prototypuvannya-idey-shhodo-vyyavlennya-ob-yektiv/).

## Noisy Transmission Model

Notebook `noisy-transmission.ipynb` contains a demo of our noisy transmission channel model. The video examples used is `test-video.MP4`. Credit for the video goes to `https://t.me/ssternenko`. It is a publicly available video from a Ukrainian UAV on the frontlines. 

## SISR

To upscale your images with [RealESRGAN](https://github.com/styler00dollar/Colab-Real-ESRGAN?tab=readme-ov-file) use their [demo Colab Notebook](https://colab.research.google.com/drive/1k2Zod6kSHEvraybHl50Lys0LerhyTMCo?usp=sharing)

## Illustrations

Folder `imgs` contains some illustrations from the bachelor thesis.

Notebook `measures.ipynb` contains an example of use of [image-similarity-measures](https://pypi.org/project/image-similarity-measures/) package on images from the `flower` folder.
