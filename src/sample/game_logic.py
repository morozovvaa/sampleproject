import random

def generate_random_number(min_value, max_value):
    return random.randint(min_value, max_value)

def check_guess(guess, secret_number):
    if guess < secret_number:
        return "Слишком мало!"
    elif guess > secret_number:
        return "Слишком много!"
    else:
        return "Поздравляю, вы угадали!"
