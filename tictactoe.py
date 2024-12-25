from random import randrange, randint

board = [['1','2','3'],
         ['4','5','6'],
         ['7','8','9']]

co_ord = {"1": (0,0), "2": (0,1), "3": (0,2), "4": (1,0), "5": (1,1), "6": (1,2), "7": (2,0), "8": (2,1), "9": (2,2)}

occupied_positions = []

def print_board():
    print('+' + '-'*7 + '+' + '-'*7 + '+' + '-'*7 + '+')
    for i in range(3):
        print('|'+' '*7+'|'+' '*7+'|'+' '*7+'|')
        print('|   ' + str(board[i][0]) + ' ' *3 + '|   ' + str(board[i][1]) + ' ' *3 + '|   ' + str(board[i][2]) + ' ' *3 + '|' )
        print('|'+' '*7+'|'+' '*7+'|'+' '*7+'|')
        print('+' + '-'*7 + '+' + '-'*7 + '+' + '-'*7 + '+')

def player_first():
    while len(occupied_positions) < 9:
        user_move = int(input("Enter your move: "))
        occupied_positions.append(user_move)
        for position,indices in co_ord.items():
            if str(user_move) == position:
                board[indices[0]][indices[1]] = "O"
                print_board()
        if board[0][0] + board[0][1] + board[0][2] == 'OOO' or board[1][0] + board[1][1] + board[1][2] == 'OOO' or board[2][0] + board[2][1] + board[2][2] == 'OOO' or board[0][0] + board[1][0] + board[2][0] == 'OOO' or board[0][2] + board[1][2] + board[2][2] == 'OOO' or board[0][1] + board[1][1] + board[2][1] == 'OOO' or board[0][0] + board[1][1] + board[2][2] == 'OOO' or board[0][2] + board[1][1] + board[2][0] == 'OOO':
            print('Player has won the match!')
            break
        elif len(occupied_positions) == 8:
            print('DRAW! - REMATCH')
            break

        print("It is my turn")
        comp_move = randrange(1,9)
        while comp_move in occupied_positions:
            comp_move = randrange(1, 9)
        occupied_positions.append(comp_move)
        for position,indices in co_ord.items():
            if str(comp_move) == position:
                board[indices[0]][indices[1]] = "X"
                print_board()
        if board[1][0] + board[1][1] + board[1][2] == 'XXX' or board[2][0] + board[2][1] + board[2][2] == 'XXX' or board[0][0] + board[1][0] + board[2][0] == 'XXX' or board[0][1] + board[1][1] + board[2][1] == 'XXX' or board[0][2] + board[1][2] + board[2][2] == 'XXX' or board[0][0] + board[1][1] + board[2][2] == 'XXX' or board[0][2] + board[1][1] + board[2][0] == 'XXX' or board[0][0] + board[0][1] + board[0][2] == 'XXX':
            print('Computer has won the match!')
            break
        elif len(occupied_positions) == 8:
            print('DRAW! - REMATCH')
            break


def computer_first():
    while len(occupied_positions) < 9:
        print("It is my turn")
        comp_move = randrange(1, 9)
        while comp_move in occupied_positions:
            comp_move = randrange(1, 9)
        occupied_positions.append(comp_move)
        for position, indices in co_ord.items():
            if str(comp_move) == position:
                board[indices[0]][indices[1]] = "X"
                print_board()
        if board[1][0] + board[1][1] + board[1][2] == 'XXX' or board[2][0] + board[2][1] + board[2][2] == 'XXX' or board[0][0] + board[1][0] + board[2][0] == 'XXX' or board[0][1] + board[1][1] + board[2][1] == 'XXX' or board[0][2] + board[1][2] + board[2][2] == 'XXX' or board[0][0] + board[1][1] + board[2][2] == 'XXX' or board[0][2] + board[1][1] + board[2][0] == 'XXX' or board[0][0] + board[0][1] + board[0][2] == 'XXX':
            print('Computer has won the match!')
            break
        elif len(occupied_positions) == 8:
            print('DRAW! - REMATCH')
            break

        user_move = int(input("Enter your move: "))
        occupied_positions.append(user_move)
        for position, indices in co_ord.items():
            if str(user_move) == position:
                board[indices[0]][indices[1]] = "O"
                print_board()
        if board[0][0] + board[0][1] + board[0][2] == 'OOO' or board[1][0] + board[1][1] + board[1][2] == 'OOO' or board[2][0] + board[2][1] + board[2][2] == 'OOO' or board[0][0] + board[1][0] + board[2][0] == 'OOO' or board[0][2] + board[1][2] + board[2][2] == 'OOO' or board[0][1] + board[1][1] + board[2][1] == 'OOO' or board[0][0] + board[1][1] + board[2][2] == 'OOO' or board[0][2] + board[1][1] + board[2][0] == 'OOO':
            print('Player has won the match!')
            break
        elif len(occupied_positions) == 8:
            print('DRAW! - REMATCH')
            break

print('Welcome to the game of tic tac toe, your symbol would be 0, while mine will be X')
print('Let me a flip a toss to decide who goes first' )
toss_choice = input("Heads or Tails? : ")
flip = randint(1,2)

if flip == 1:
    result = "Heads"
elif flip == 2:
    result = "Tails"

if toss_choice == result:
    print('Congrats! You have won the toss.')
    print_board()
    player_first()
else:
    print('You have lost the toss. The computer will start the match')
    print_board()
    computer_first()