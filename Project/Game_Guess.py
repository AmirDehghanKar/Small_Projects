#EN
#A guessing game: human vs bot. The human guesses the computer’s random number (1-99) with ↑/↓ hints.
#Then the user types a secret number and the bot finds it using random guesses within a shrinking range. Fewer guesses wins.

import random
import getpass

LOW, HIGH = 1, 99


def read_int(prompt, low=LOW, high=HIGH):
    while True:
        try:
            value = int(prompt and input(prompt))
            if low <= value <= high:
                return value
        except ValueError:
            pass
        print(f'Please enter a whole number between {low} and {high}.')


def human_turn():
    print('Turn HUMAN')
    secret = random.randint(LOW, HIGH)
    tries = 0
    print('-' * 28)

    while True:
        guess = read_int('Enter your guess: ')
        tries += 1
        if guess == secret:
            print(' !!! You Win !!! ')
            break
        print('↓↓↓↓↓↓' if guess > secret else '↑↑↑↑↑↑')

    print('Number of human guesses:', tries)
    return tries


def bot_turn():
    print('\nTurn BOT')
    secret = read_int(f'Enter your secret number ({LOW}-{HIGH}): ')
    low, high = LOW, HIGH
    tries = 0
    print('-' * 28)

    while True:
        guess = (low + high) // 2        # binary search
        tries += 1
        print('Guess:', guess)
        if guess == secret:
            print('The bot wins this round!')
            break
        if guess > secret:
            high = guess - 1
        else:
            low = guess + 1

    print('Number of bot guesses:', tries)
    return tries


def game_guess():
    human = human_turn()
    bot = bot_turn()

    print(f'\nHuman: {human} guesses | Bot: {bot} guesses\n')
    if human < bot:
        print('!!!! Human wins !!!!')
    elif human > bot:
        print('#### Bot wins ####')
    else:
        print('It\'s a tie!')


game_guess()