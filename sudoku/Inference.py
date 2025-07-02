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