board = []

for row in range(0, 3):
    board.append([])
    for col in range(0, 3):
        board[row].append('|_|')

def print_board(board):
    for row in board:
        print("".join(row))

print(board)
print('\n')
print_board(board)

#TODO create a board

#TODO detect a win, based on rows, col, or diag. write a function to check rows, cols, diag

#TODO crate check_win func

#TODO while loop and check game over or still playing







