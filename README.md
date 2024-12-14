# Python-Sudoku-Solver
Python Sudoku Solver using [Ultralytics or Yolo](https://docs.ultralytics.com/quickstart/) v8 Object Detection, it uses Ultralytics object detection for number recognition then brute forces the puzzle to print a result.
## Packages
---
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
You will want to follow the instructions on the [Pytorch Website](https://pytorch.org/get-started/locally/) for installation and your specific system (Windows, Mac, Linux).
## Usage
Download this repository and extract. Run Solver.py in the terminal / or your editor of choice. Input the file path for the image within the working directory. For one of the hard example images: Examples/Hard-Puzzle-1.jpg
## Pretrained Models
There are different sizes of pretrained models from s to x. The Smallest one is nano (n) and the largest is xl. This current pretrained model is M. (Pretrained-M.pt)
