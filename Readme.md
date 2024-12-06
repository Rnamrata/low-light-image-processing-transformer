# Low Light Image Processing Transformer
 
## Overview
This project focuses on the Low-Light Image Processing Transformer, a neural network architecture designed to enhance images captured in low-light conditions. The study focuses on fine-tuning the hyperparameters of an existing model (HVI-CIDNet) designed to improve perceptual metrics. This is accomplished by using a stable diffusion approach to adjust the lighting of a source image instead of adding noise. This innovative model processes brightness and color features separately using a dual-path architecture. The project also introduces Fréchet Inception Distance (FID) as a new evaluation metric for image quality, alongside conventional metrics such as Peak Signal-to-Noise Ratio (PSNR) and Structural Similarity Index Measurement (SSIM).

## Key Features
1. Dual-Path Architecture:

    * Separates processing of brightness and color features.
    * Employs the Horizontal/Vertical-Intensity (HVI) transformation for efficient color space conversion.

2. CIDNet:

    * A UNet-based architecture featuring two branches for brightness and color processing.
    * Uses the Lightweight Cross-Attention (LCA) module for information exchange and noise suppression.

3. Evaluation Metrics:

    * FID to assess generated image similarity to real images.
    * PSNR and SSIM for traditional quality assessment.

4. Dataset:

    * A curated dataset from Kaggle consisting of 500 paired low-light and normal-light images.

## Dataset
    Source: Kaggle [https://www.kaggle.com/datasets/soumikrakshit/lol-dataset]
    Content: 500 paired images (low-light and normal-light), predominantly indoor scenes with a resolution of 400×600.
    Division: 485 training pairs, 15 testing pairs.

## Architecture

    1. Horizontal/Vertical-Intensity (HVI) Transformation
        * Intensity Map: Derives the maximum value from RGB channels.
        * HV Color Map: Measures color reflectance with adjustable density.
        * Trainable HVI Map: Combines intensity and HV color maps for reversible transformation.
    
    2. Color and Intensity Decoupling Network (CIDNet)
        * HV-way: Focuses on color information processing.
        * Intensity-way: Handles brightness adjustments for varied lighting scenarios.
        * LCA Module:
            * Includes Cross-Attention Block (CAB), Intensity Enhance Layer (IEL), and Color Denoise Layer (CDL).

    3. Fréchet Inception Distance (FID)
        * Compares feature distributions of generated and real images.
        * Lower FID indicates higher quality.

## Results
    Three model variants were evaluated.
    Model 3 performed best with optimal metrics:
        PSNR: 24.54 dB
        SSIM: 0.8633
        FID: 31.07

## Conclusion
The Low-Light Image Processing Transformer demonstrates significant improvement in image enhancement tasks under low-light conditions. While small adjustments can be time-consuming, increasing model complexity improves performance. Future goals include integrating differentiable FID in the loss function and leveraging advanced techniques like LiDAR for improved accuracy and precision.

## References
1. Dataset: Kaggle LOL Dataset [https://www.kaggle.com/datasets/soumikrakshit/lol-dataset]
2. HVI-CIDNet: You Only Need One Color Space: An Efficient Network for Low-light Image Enhancement [https://github.com/Fediory/HVI-CIDNet]
3. pytorch-frechet-inception-distance: Fréchet Inception Distance (FID) for Pytorch [https://github.com/hukkelas/pytorch-frechet-inception-distance]