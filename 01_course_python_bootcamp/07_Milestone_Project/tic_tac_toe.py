row1 = [' ', '|', ' ', '|', ' ']
row2 = [' ', '|', ' ', '|', ' ']
row3 = [' ', '|', ' ', '|', ' ']
dashes = ['-', '-', '-', '-', '-']

def display_board(rows):
    print()
    for row in rows:
        for cell in row:
            print(cell, end=' ')
        print()
    print()


def team_choice():
    while True:
        player1 = input('Player 1: Select X or O ')

        if player1 in ['X', 'O']:
            break

    if player1 == 'X':
        player2 = 'O'

    else:
        player2 = 'X'

    return player1, player2


def position_available(position):
    if position in [1, 2, 3]:
        index = (position - 1) * 2
        return row1[index] == ' '

    if position in [4, 5, 6]:
        index = (position - 4) * 2
        return row2[index] == ' '

    if position in [7, 8, 9]:
        index = (position - 7) * 2
        return row3[index] == ' ' 


def update_board(position, player):
    global row1
    global row2
    global row3

    if position in [1, 2, 3]:
        index = (position - 1) * 2
        row1[index] = player

    elif position in [4, 5, 6]:
        index = (position - 4) * 2
        row2[index] = player

    elif position in [7, 8, 9]:
        index = (position - 7) * 2
        row3[index] = player


def take_user_input():
    while True:
        position = input('Select a cell (1-9):')

        if position.isdigit():
            position = int(position)

            if position not in range(1, 10):
                print('The selected cell must be between 1 and 9!')

            if position_available(position):
                break

            elif not position_available(position):
                print('Cell already occupied!')


        else:
            print('The selected cell must be a digit (1-9)')

    return position


def check_winner(rows, player):
    # Checking rows
    for row in rows:
        if row[::2] == [player] * 3:
            return True

    # Checking cols
    for i in range(0, 5, 2):
        col = []
        for j in range(0, 5, 2):
            if rows[j][i] == player:
                col.append(player)
        if col == [player] * 3:
            return True

    # Checking main diagonal
    diag = []
    for i in range(0, 5, 2):
        if rows[i][i] == player:
            diag.append(player)

    if diag == [player] * 3:
        return True

    # Checking reverse diagonal
    rev_diag = []
    for i in range(0, 5, 2):
        if rows[i][5 - i - 1] == player:
            rev_diag.append(player)

    if rev_diag == [player] * 3:
        return True

    return False


def swap_turns(turn):
    if turn:
        return False

    return True


def play_game():
    global row1
    global row2
    global row3

    row1 = [' ', '|', ' ', '|', ' ']
    row2 = [' ', '|', ' ', '|', ' ']
    row3 = [' ', '|', ' ', '|', ' ']

    player1, player2 = team_choice()

    player1_turn = True

    while True:
        board_rows = [row1, dashes, row2, dashes, row3]

        display_board(board_rows)

        if player1_turn:
            print("Player 1's turn: ")

        else:
            print("Player 2's turn: ")

        position = take_user_input()

        if position_available(position):
            if player1_turn:
                update_board(position, player1)
            else:
                update_board(position, player2)

        if check_winner(board_rows, player1):
            board_rows = [row1, dashes, row2, dashes, row3]
            display_board(board_rows)
            print('Player 1 WINS!!!')
            print()
            break

        elif check_winner(board_rows, player2):
            board_rows = [row1, dashes, row2, dashes, row3]
            display_board(board_rows)
            print('Player 2 WINS!!!')
            print()
            break

        player1_turn = swap_turns(player1_turn)

def restart_game():
    while True:
        restart = input('Play again? (yes/no): ')
        print()

        restart.lower()

        if restart not in ['yes', 'no']:
            continue

        elif restart == 'yes':
            return True

        elif restart == 'no':
            return False

def start_game():
    while True:
        start = input('Start the game? (yes/no): ')

        print()
    
        start.lower()
    
        if start not in ['yes', 'no']:
            continue
    
        elif start == 'yes':
            return True
    
        elif start == 'no':
            return False


def main():
    while True:
        print('OXOXO Tic Tac Toe XOXOX')
        print()

        if start_game():
            play_game()

        else:
            print('Quitting...')
            break

        if not restart_game():
            print('Thank you for playing!')
            print('Quitting...')
            break


main()