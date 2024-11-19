from ultralytics import YOLO
from ultralytics.utils.plotting import Annotator  # ultralytics.yolo.utils.plotting is deprecated

# Load a model
model = YOLO("run-2.pt")  # pretrained YOLOv8n model, Name of the model

board = input("Insert File Name Here:")

# Run batched inference on a list of images
results = model(board)  # return a generator of Results objects


grid = [[ 0, 2, 0, 0, 0, 0, 0, 9, 0], #Predefined Grid (Will be replaced by number finding)
        [ 0, 7, 1, 0, 0, 0, 0, 0, 4],
        [ 0, 8, 0, 0, 0, 0, 0, 0, 1],
        [ 0, 0, 0, 0, 0, 8, 2, 0, 0],
        [ 0, 5, 0, 0, 0, 3, 6, 0, 7],
        [ 2, 0, 0, 7, 0, 9, 0, 0, 0],
        [ 0, 0, 0, 6, 0, 0, 3, 0, 0],
        [ 0, 0, 0, 0, 4, 0, 0, 0, 2],
        [ 5, 0, 4, 1, 0, 0, 0, 0, 0]]

breaker = False

for r in results:
    for z in range(0,81): #Scroll Through all the Numbers on the board
        for a in range(9,-1,-1): 
            for b in range(9,-1,-1): #Boards
                
                x = r.boxes.xyxyn[z,0] # X of the Detection
                y = r.boxes.xyxyn[z,1] # Y of the Detection
                
                ca = a/9 # Estimation Based on the Image bounds (Why the image has to be cropped to the board)
                cb = b/9
                cha = False
                chb = False
                if ca - .05 < x:
                    cha = True
                if cb - .05 < y:
                    chb = True
                if cha == True and chb == True:
                    grid[b][a] = int(model.names[int(r.boxes.cls[z])])
                    breaker = True
                    break
            if breaker == True:
                breaker = False
                break


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


if solve(grid, 0, 0):
    for i in range(9):
            for j in range(9):
                print(grid[i][j], end=" ")
            print()
else:
    print("No Solution")
                
            
                
                
            
