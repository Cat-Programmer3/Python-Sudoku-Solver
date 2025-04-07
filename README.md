# Python Sudoku Solver
Python Sudoku Solver using [Yolo](https://docs.ultralytics.com/quickstart/) v8 Object Detection, it uses Ultralytics object detection for number recognition then brute forces the puzzle to print a result.
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
You will want to follow the instructions on the website: [pytorch.org](https://pytorch.org/get-started/locally/) for installation.
## Usage
Download the repository and extract into your directory. Run solver.py in terminal or IDE. Input file path of the (Cropped) image of the Sudoku puzzle; Ex. Examples/Hard-Puzzle-1.jpg
## Pretrained Models
There are different sizes of pretrained models from s to x. The Smallest one is nano (n) and the largest is xl. The pretrained model load currently is medium. (Pretrained-M.pt)
