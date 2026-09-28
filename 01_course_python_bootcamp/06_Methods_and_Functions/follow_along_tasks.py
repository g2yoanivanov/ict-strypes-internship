from random import shuffle

# Shuffle cups game

def shuffle_list(my_list):
    shuffle(my_list)

    return my_list


def get_player_guess():
    guess = -1

    while guess not in [0, 1, 2]:
        guess = int(input('Take a guess (0, 1, 2): '))

    return guess

def check_guess(shuffled_list, player_guess):
    if shuffled_list[player_guess] == 'O':
        return True

    return False

def play_game():
    my_list = [0, 'O', 0]

    shuffled = shuffle_list(my_list)

    guess = get_player_guess()

    result = check_guess(shuffled, guess)

    if result:
        print('You won!')

    else:
        print('Wrong guess!')
    
    print(shuffled)

play_game()