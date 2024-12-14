from ultralytics import YOLO
from ultralytics.utils.plotting import Annotator 
import numpy as np


# Solving Algrothim

def IVM(grid, row, col, number):

    for x in range(9):
        if grid[row][x] == number:
            return False

    for x in range(9):
        if grid[x][col] == number:
            return False

    corner_row = row - row % 3
    corner_col = col - col % 3
    for x in range(3):
        for y in range(3):
            if grid[corner_row + x][corner_col + y] == number:
                return False

    return True



def solve(grid, row, col): # Start Solving the puzzle

    if col == 9:
        if row == 8:
            return True
        row += 1
        col = 0

    if grid[row][col] > 0:
        return solve(grid, row, col + 1)

    for num in range(1,10):

        if IVM(grid, row, col, num):

            grid[row][col] = num

            if solve(grid, row, col + 1):
                return True

        grid[row][col] = 0

    return False


def load_puzzle():
    # Load the puzzle from a file
    return input("Enter the puzzle: ") # User Input Puzzle

def run_inference(model_file, board_file):
    # Load the model and board from files
    board_inference = model_file(board_file, verbose=False)
    return board_inference

def create_board(bn, orginal_board, model_file):
    for nums in range(0,81):
        x = bn[0].boxes.xyxyn[nums,0]
        y = bn[0].boxes.xyxyn[nums,1]

        do_break = False

        for test_x in range(0,9):
            for test_y in range(0,9):
                test_nx = test_x/9
                test_ny = test_y/9

                if test_nx == 1:
                    test_nx -= 1/18
                if test_ny == 1:
                    test_ny -= 1/18
                
                if test_nx == 0:
                    test_nx += 1/18
                if test_ny == 0:
                    test_ny += 1/18
                
                if x > test_nx - 1/18 and x < test_nx + 1/18:
                    if y > test_ny - 1/18 and y < test_ny + 1/18:
                        orginal_board[test_x][test_y] = int(model_file.names[int(bn[0].boxes.cls[nums])])
                        do_break = True
                        break                
            if do_break:
                break
    return orginal_board            

def main():
    grid = [[ 0, 0, 0, 0, 0, 0, 0, 0, 0], #Predefined Zeroed Grid 
        [ 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [ 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [ 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [ 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [ 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [ 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [ 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [ 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    
    model = YOLO("Pretrained-M.pt")
    board = load_puzzle()
    board_numbers = run_inference(model, board)
    grid = create_board(board_numbers, grid, model)

    if solve(grid, 0, 0):
        for i in range(9):
                for j in range(9):
                    print(grid[i][j], end=" ")
                print()
    else:
        print("No Solution")

    
if __name__ == "__main__":
    main()
