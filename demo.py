board = []

for row in range(0, 3):
    board.append([])
    if row < 2:
        for col in range(0, 3):
            board[row].append('[ ]')
    if row == 2:
        for col in range(0, 3):
            board[row].append('[ ]')


def print_board(board):
    for row in board:
        print("|".join(row))


top_left = board[0][0]
top_middle = board[0][1]
top_right = board[0][2]
middle_left = board[1][0]
middle = board[1][1]
middle_right = board[1][2]
bottom_left = board[2][0]
bottom_middle = board[2][1]
bottom_middle = board[2][2]


print(top_left)
print(board)
print('\n')
print_board(board)


#TODO create a board

#TODO detect a win, based on rows, col, or diag. write a function to check rows, cols, diag

#TODO crate check_win func

#TODO while loop and check game over or still playing







