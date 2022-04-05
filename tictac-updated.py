#TICTACTOE funcs
    #blank board
def display_board(board):
    print('\n'*3)
    print('1   |2   |3')
    print(' ' + board[1] + '  | ' + board[2] + '  | ' + board[3])
    print('    |    |')
    print('---------------')
    print('4   |5   |6')
    print(' ' + board[4] + '  | ' + board[5] + '  | ' + board[6])
    print('    |    |')
    print('---------------')
    print('7   |8   |9')
    print(' ' + board[7] + '  | ' + board[8] + '  | ' + board[9])
    print('    |    |')

    #player 1 choice of marker
def player_input():
    marker = ''
    while not (marker == 'X' or marker == 'O'):
        marker = input("Player 1: Do you want to use X or O? ").upper()
    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')

    #placing marker onto board using index position
def place_marker(board,marker,position):
    board[position] = marker

    #randomly choose which player goes first
import random
def choose_first():
    if random.randint(0, 1) == 0:
        return 'Player 2'
    else:
        return 'Player 1'

    #make sure the request space is empty
def space_check(board,position):
    return board[position] == ' '

    #make sure the board has an empty space
def full_board_check(board):
    for i in range(1,10):
        if space_check(board, i):
            return False
    return True

    #asking the player to choose a digit between 1 and 9 and space is not taken already
def player_choice(board):
    position = 0
    while position not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not space_check(board,position):
        position = int(input('Please choose a position: (1-9) '))
    return position

    #checking if any player has won
def win_check(board, marker):
    return ((board[1] == marker and board[2] == marker and board[3] == marker) or  # across the top
            # across the middle
            (board[4] == marker and board[5] == marker and board[6] == marker) or
            # across the bottom
            (board[7] == marker and board[8] == marker and board[9] == marker) or
            # down the left
            (board[1] == marker and board[4] == marker and board[7] == marker) or
            # down the middle
            (board[2] == marker and board[5] == marker and board[8] == marker) or
            # down the right
            (board[3] == marker and board[6] == marker and board[9] == marker) or
            # diagonal
            (board[1] == marker and board[5] == marker and board[9] == marker) or
            # diagonal
            (board[7] == marker and board[5] == marker and board[3] == marker))

    #ask if players would like to continue playing
def replay():
    choice = "default"
    while choice not in ['Y', 'N']:
          choice = input("Keep playing? (Y or N): ").upper()
          if choice not in ['Y', 'N']:
               print("Sorry, invalid choice. Please type Y or N: ")
    if choice == 'Y':
          return True
    else:
          return False

# GET THA GAME GOIN
print('Welcome to Tic Tac Toe!')
while True:
    ## set up everything ( board, first player, choose markers)
    the_board = [' ']*10
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(turn + ' will go first')
    play_game = input('Ready to play? Y or N ').upper()
    if play_game == 'Y':
        game_on = True
    else:
        game_on = False
    ### gameplay
    while game_on:
    #### player 1 turn
        if turn == 'Player 1':
            #show board
            display_board(the_board)
            #choose position
            position = player_choice(the_board)
            #place a marker on chosen position
            place_marker(the_board,player1_marker,position)
            #check if they won
            if win_check(the_board,player1_marker):
                display_board(the_board)
                print('Player 1 is the winner!')
                game_on = False
            #checking if board is full with no winners
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('The game is a Tie')
                    game_on = False
                #passing turn to player 2 if neither of the above are true
                else:
                    turn = 'Player 2'
        else:
    #### player 2 turn (duplicate of player 1)
            display_board(the_board)
            position = player_choice(the_board)
            place_marker(the_board, player2_marker, position)
            if win_check(the_board, player2_marker):
                display_board(the_board)
                print('Player 2 is the winner!')
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('The game is a Tie')
                    game_on = False
                else:
                    turn = 'Player 1'
    #break out if no replay
    if not replay():
        break