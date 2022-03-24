
# initialize global variables
TTT_board = [['_']*3, ['_']*3, ['_']*3]
# TTT_board = []
XO = 'x'
winner = None
draw = False
count = 0
# Another way to create a tictactoe game board
# for row in range(0, 3):
#     TTT_board.append([])
#     for col in range(0, 3):
#         TTT_board[row].append("_")


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

    # if all([row for row in TTT_board[0]]) and winner is None:
    #     draw = True
    #     print("Draw!")
    if winner is None:
        count += 1
        print(count)
        if count >= 9:
            draw = True
            print('Draw!')
    return count

def player_choice(player_selection, shape):
    global TTT_board
    if player_selection == 'top left':
        TTT_board[0][0] = shape.upper()
    if player_selection == 'top middle':
        TTT_board[0][1] = shape.upper()
    if player_selection == 'top right':
        TTT_board[0][2] = shape.upper()

    if player_selection == 'middle left':
        TTT_board[1][0] = shape.upper()
    if player_selection == 'middle':
        TTT_board[1][1] = shape.upper()
    if player_selection == 'middle right':
        TTT_board[1][2] = shape.upper()

    if player_selection == 'bottom left':
        TTT_board[2][0] = shape.upper()
    if player_selection == 'bottom middle':
        TTT_board[2][1] = shape.upper()
    if player_selection == 'bottom right':
        TTT_board[2][2] = shape.upper()
    check_win()


# def check_tie():
#     global draw, game
#     for list in range(len(TTT_board)):
#         for innerlist in range(len(TTT_board[list])):
#            if "_" not in TTT_board[list][innerlist] and winner is False:
#                 draw = True
#                 print('Draw!')
#                 game = False
#             elif winner:
#                 game = False
#             else:
#                 game = True


game = True
while game:
    player_position = input('Select your position. ')
    shape = input('Place your shape. ')
    player_choice(player_position, shape)
    print_board(TTT_board)
    # check_tie()
    if draw or winner:
        game = False


