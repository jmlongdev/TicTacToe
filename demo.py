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

player_x = input('Select which box to place your x. ')
player_y = input('Select which box to place your y. ')

if player_x == 'top left':
    board[0][0] = "[X]"
if player_y == 'top left':
    board[0][0] = "[Y]"
if player_x == 'top middle':
    board[0][1] = "[X]"
if player_y == 'top middle':
    board[0][1] = "[Y]"
if player_x == 'top right':
    board[0][2] = "[X]"
if player_y == 'top right':
    board[0][2] = "[Y]"

if player_x == 'middle left':
    board[1][0] = "[X]"
if player_y == 'middle left':
    board[1][0] = "[Y]"
if player_x == 'middle':
    board[1][1] = "[X]"
if player_y == 'middle':
    board[1][1] = "[Y]"
if player_x == 'middle right':
    board[1][2] = "[X]"
if player_y == 'middle right':
    board[1][2] = "[Y]"

if player_x == 'bottom left':
    board[2][0] = "[X]"
if player_y == 'bottom left':
    board[2][0] = "[Y]"
if player_x == 'bottom middle':
    board[2][1] = "[X]"
if player_y == 'bottom middle':
    board[2][1] = "[Y]"
if player_x == 'bottom right':
    board[2][2] = "[X]"
if player_y == 'bottom right':
    board[2][2] = "[Y]"


print(board)
print('\n')
print_board(board)



#TODO create a board

#TODO detect a win, based on rows, col, or diag. write a function to check rows, cols, diag

#TODO crate check_win func

#TODO while loop and check game over or still playing







