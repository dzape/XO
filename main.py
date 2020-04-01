# --------------- Global Var -------

# Game board
board = ["-","-","-",
         "-","-","-",
         "-","-","-"]

# If game isstill going
game_still_going = True

# Who won / Tie
Winner = None

# Whos turn is it
curent_player = "X"

def display_board():
        print(board[0] + " | " + board[1] + " | " +  board[2])
        print(board[3] + " | " + board[4] + " | " +  board[5])
        print(board[6] + " | " + board[7] + " | " +  board[8])

def play_game():

    display_board()

    while game_still_going:

        handle_turn(curent_player)

        check_if_game_over()

        flip_player()

#--------- Game ended ---------------

    if winner == "X" or winner == "O":
        print(winner + " won.")

    elif winner == None:
        print(" Tie.")


def handle_turn(player):

    print(player + " 's turn. ")

    position = input(" Chose position from 1 - 9 :")

    valid = False

    while not valid:

        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            position = input("Invalid input. Chose position from 1-9 : ")

        position = int(position) - 1

        if board[position] == "-":
            valid = True
        else:
            print(" You cant go there. Go again :")

        board[position] = player

        display_board()


def check_if_game_over():
    check_for_winner()
    check_if_tie()

def check_for_winner():

    # Set global winner
    global winner

    #check row
    row_winner = check_rows()

    #check columns
    column_winner = check_columns()

    #check diagonals
    diagonals_winner = check_diagonals()

    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonals_winner:
        winner = diagonals_winner
    else:
        winner = None
    return

# ------------- Check For Winner --------------------

def check_rows():

    global game_still_going

    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"

    if row_1 or row_2 or row_3:
        game_still_going = False

    if row_1:
       return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]

    return

def check_columns():

    global game_still_going

    column_1 = board[0] == board[3] == board[6] != "-"
    column_2 = board[1] == board[4] == board[7] != "-"
    column_3 = board[2] == board[5] == board[8] != "-"

    if column_1 or column_2 or column_3:
        game_still_going = False

    if column_1:
       return board[0]
    elif column_2:
        return board[1]
    elif column_3:
        return board[2]

    return

def check_diagonals():

    global game_still_going

    diagonal_1 = board[0] == board[4] == board[8] != "-"
    diagonal_2 = board[2] == board[4] == board[6] != "-"

    if diagonal_1 or diagonal_2:
        game_still_going = False

    if diagonal_1:
       return board[0]
    elif diagonal_2:
        return board[2]

    return

# ------------- Check For Winner --------------------

def check_if_tie():

    global game_still_going

    if "-" not in board:
        game_still_going = False

    return

def flip_player():

    global curent_player

    if curent_player == "X":
        curent_player = "O"

    elif curent_player == "O":
        curent_player = "X"

    return

play_game()