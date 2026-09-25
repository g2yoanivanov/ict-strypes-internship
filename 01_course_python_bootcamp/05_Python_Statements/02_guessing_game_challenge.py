from random import randint


target = randint(1, 100)

print('RULES:')
print('Guess the random number between 1 and 100.')

player_guess = int(input('Guess the number:'))
if player_guess < 1 or player_guess > 100:
        print('OUT OF BOUNDS')

elif player_guess == target:
        print('YOU WON')
        print('TOOK YOU 1 GUESSES')

else:
    if abs(player_guess - target) <= 10:
        print('WARM!')
    else:
         print('COLD!')

last_guess = player_guess
guesses_count = 1

while True:
    player_guess = int(input('Guess the number:'))

    guesses_count += 1

    if player_guess < 1 or player_guess > 100:
        print('OUT OF BOUNDS')

    elif player_guess == target:
        print('YOU WON')
        print(f'TOOK YOU {guesses_count} GUESSES')
        break

    else:
        if abs(player_guess - target) < abs(last_guess - target):
             print('WARMER!')
        else:
            print('COLDER!')

    last_guess = player_guess