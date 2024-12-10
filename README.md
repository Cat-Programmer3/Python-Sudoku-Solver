# Python-Soduku-Solver
Python Soduku Solver using [Ultralytics or Yolo](https://docs.ultralytics.com/quickstart/) v8 Object Detection, it uses Ultralytics object detection for number recognition then brute forces the puzzle to print a result.


## Packages
Uses Ultralytics & Pytorch

### Ultralytics Installation:

Via pip: 
```bash
pip install ultralytics
```

Via Conda: 
```bash
conda install -c conda-forge ultralytics
```
### Pytorch Installation:
You will want to follow the instructions on the [Pytorch Website](https://pytorch.org/get-started/locally/) for installation.

## Usage
Download Zip & Extract

Run Solver-1.py with set pre-trained yolov8 model for number detection

Enter the file path of the puzzle (Image must be cropped)

Ex. Examples/Test-Puzzle-1.jpg

## Pretrained Models
There are different sizes of pre-trained models from s to x. The Smallest one is nano (n) and the largest is xl.
