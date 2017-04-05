import random

def show_board(board):
     print()
     print('   |   |')
     print(' ' + board[0] + ' | ' + board[1] + ' | ' + board[2])
     print('   |   |')
     print('-----------')
     print('   |   |')
     print(' ' + board[3] + ' | ' + board[4] + ' | ' + board[5])
     print('   |   |')
     print('-----------')
     print('   |   |')
     print(' ' + board[6] + ' | ' + board[7] + ' | ' + board[8])
     print('   |   |')

def show_example_board():
    print("this is the example board. please use the numbers below to make your move.")
    example_board = ["0","1","2","3","4","5","6","7","8","9"]
    show_board(example_board)
    print()

def get_player_move(board):
    #get the player's move
    print('It is the player\'s turn. What is your move?')
    print('pick between 0 and 8')
    location = input()
    example_board = ["0","1","2","3","4","5","6","7","8","9"]

    while location not in example_board or not has_empty_space(board,int(location)):
        print("that is an invalid move.")
        print('please pick between 0 and 8 that is open')
        location = input()
    return int(location)

def get_computer_move(board):
    print('It is the computer\'s turn.')
    example_board = ["0","1","2","3","4","5","6","7","8","9"]
    location = random.choice(example_board)

    while not has_empty_space(board,int(location)):
        location = random.choice(example_board)
    print("the computer has chosen location {}".format(location))
    return int(location)

def update_board(board, location, move):
    board[location] = move
    return board


def won_the_game(l, move):
    #top row
    if ((l[0] == move and l[1] == move and l[2] == move) or 
    #middle row
    (l[3] == move and l[4] == move and l[5] == move) or 
    #buttom row
    (l[6] == move and l[7] == move and l[8] == move) or
    #first column
    (l[0] == move and l[3] == move and l[6] == move) or
    #second column
    (l[1] == move and l[4] == move and l[7] == move) or
    #third column
    (l[2] == move and l[5] == move and l[8] == move) or
    #left top to right buttom diagonal
    (l[0] == move and l[4] == move and l[8] == move) or
    #right top to left buttom diagonal
    (l[2] == move and l[4] == move and l[6] == move)):
        return True


#check if the board (the list) has any empty space on it
def has_any_empty_space(l):
    for move_on_board in l:
        if move_on_board == " ":
            return True
    return False

#check if the board (the list) has any empty space on the location
def has_empty_space(l,location):
    try:
        l[location]== " "
    except: 
        return False
    else:
        if l[location]== " ":
            return True
        else:
            return False

def show_winning_animation():
    print(" #      #  #  #    #  #    #  #  #    #   ####  ")
    print(" #      #  #  ##   #  ##   #  #  ##   #  #    # ")
    print(" #   #  #  #  # #  #  # #  #  #  # #  #  #      ")
    print(" # #  # #  #  #  # #  #  # #  #  #  # #  #  ### ")
    print(" #      #  #  #    #  #    #  #  #    #   ####  ")

def show_losing_animation():
    print(":( :( :( :(:( :(:( :(:( :(:( :(:( :(:( :(:( :(:( :(")


def introduce_to_game():
    print()
    print("*********************************************")
    print("***********Let's play Tic Tac Toe************")
    print("*********************************************")
    print()
    show_example_board()

def main():
    #start the game
    introduce_to_game()

    #the player goes first
    curr_player = "player"
    move = "X"
    #new board
    board = [" "," "," "," "," "," "," "," "," "]
    print("{}, your move on the board will look like this {}".format(curr_player, move))

    #gameplay
    while True:
        #Player's turn
            # TODO: Show the board
            print()
            print("before {} makes the move, the board looks like this: ".format(curr_player))
            show_board(board)
            

            # TODO: Get Player's move
            print("remember, your move is {}".format(move))
            location = get_player_move(board)
            board = update_board(board, location, move)

            # TODO: Check if Player won
            if won_the_game(board, move):
                show_winning_animation()
                show_board(board)
                print("{} won the game!".format(curr_player))
                show_winning_animation()
                break

            # TODO: Check if the board is full
            if not has_any_empty_space(board):
                print("The game has no space left. The game is over")
                break

            #prepare for the handoff
            curr_player = "computer"
            move = "O"

        #Computer's turn
            # Don't show the board for computer, because it gets crowded.
            print() 
            # print("before {} makes the move, the board looks like this:".format(curr_player))
            # show_board(board)

            # TODO: Get Computer's move
            location = get_computer_move(board)
            board = update_board(board, location, move)

            # TODO: Check if computer won
            if won_the_game(board, move):
                show_losing_animation()
                show_board(board)
                print("I'm sorry, but {} won the game!".format(curr_player))
                show_losing_animation()
                break

            # TODO: Check if the board is full
            if not has_any_empty_space(board):
                print("The game has no space left. The game is over")
                break

            #prepare for the handoff
            curr_player = "player"
            move = "X"


if __name__ == "__main__":
    main()