
# initialize global variables
TTT_board = [['_']*3, ['_']*3, ['_']*3]
# TTT_board = []
XO = 'x'
winner = None
draw = False
count = 0


def print_board(TTT_board):
    for row in TTT_board:
        print("|".join(row))

def check_win():
    global TTT_board, winner, draw, count
    # Check for winning rows
    for row in range(0, 3):
        if TTT_board[row][0] == TTT_board[row][1] == TTT_board[row][2] and TTT_board[row][0] != "_":
            # this row won
            winner = TTT_board[row][0]
            print(f"{winner} won!")
            break
    # Check for winning columns
    for col in range(0, 3):
        if TTT_board[0][col] == TTT_board[1][col] == TTT_board[2][col] and TTT_board[0][col] != "_":
            # this col won
            winner = True
            winner = TTT_board[0][col]
            print(f"{winner} won!")
            break

    # Check for diagonal winners
    if TTT_board[0][0] == TTT_board[1][1] == TTT_board[2][2] and TTT_board[0][0] != "_":
        # game won diagonally left to right
        winner = TTT_board[0][0]
        print(f"{winner} won!")

    if TTT_board[0][2] == TTT_board[1][1] == TTT_board[2][0] and TTT_board[0][2] != "_":
        # game won diagonally right to left
        winner = TTT_board[0][2]
        print(f"{winner} won!")

    if winner is None:
        count += 1
        # print(count)
        if count >= 9:
            draw = True
            print('Draw!')
    return count


def player_choice(player_selection, shape):
    global TTT_board
    if player_selection == '1':
        TTT_board[0][0] = shape.upper()
    if player_selection == '2':
        TTT_board[0][1] = shape.upper()
    if player_selection == '3':
        TTT_board[0][2] = shape.upper()

    if player_selection == '4':
        TTT_board[1][0] = shape.upper()
    if player_selection == '5':
        TTT_board[1][1] = shape.upper()
    if player_selection == '6':
        TTT_board[1][2] = shape.upper()

    if player_selection == '7':
        TTT_board[2][0] = shape.upper()
    if player_selection == '8':
        TTT_board[2][1] = shape.upper()
    if player_selection == '9':
        TTT_board[2][2] = shape.upper()
    check_win()

game = True
while game:
    player_position = input('Select your position. ')
    shape = input('Place your shape. ')
    player_choice(player_position, shape)
    print_board(TTT_board)
    # check_tie()
    if draw or winner:
        game = False


