# BIANSA (Brain Intensity Abnormality Segmentation Algorithm): A novel tool for automated segmentation of white matter hyperintensities

![CC BY-NC-SA 4.0][cc-by-nc-sa-shield]

[cc-by-nc-sa-shield]: https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey.svg
[![Hits](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2FKevinTsaiCodes%2Fwmansa&count_bg=%2379C83D&title_bg=%23555555&icon=&icon_color=%23E7E7E7&title=hits&edge_flat=false)](https://hits.seeyoufarm.com)


### Dependencies
- Python 3.8
- MATLAB 2017a

#### Install the dependencies of python

    pip install -r requirements.txt

### Preparing Data
1. To build **training** dataset, you'll also need following datasets. All the images need to be converted to **grayscale**.
- [ADNI](https://adni.loni.usc.edu/)

2. To build **validation/testing** dataset, you'll also need following datasets. All the images need to be cropped into a square, and resize into **512*512**.
- [ADNI 2](https://adni.loni.usc.edu/)
- [ADNI 3](https://adni.loni.usc.edu/)


### Getting Started
#### Usage
