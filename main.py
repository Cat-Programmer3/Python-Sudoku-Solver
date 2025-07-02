from ultralytics import YOLO ## Ultralytics module for YOLO
from ultralytics.utils.plotting import Annotator 

from sudoku.Inference import * ## Import the Functions for the Inference Module
from sudoku.Solver import *    ## Import the Functions for the Solver

def main():
    grid = [[ 0, 0, 0, 0, 0, 0, 0, 0, 0], ## Start with a grid of the correct size
        [ 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [ 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [ 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [ 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [ 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [ 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [ 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [ 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    
    model = YOLO("Pretrained-M.pt") ## Medium size module for inference on the board Image
    board = load_puzzle() ## Load the puzzle image
    board_numbers = run_inference(model, board) ## Run the detection module for the image to read the current numbers
    grid = create_board(board_numbers, grid, model) ## Convert the inference image to an array
    print_sol(grid) ## Print_sol runs the solver module and outputs in text

if __name__ == "__main__":
    main()
