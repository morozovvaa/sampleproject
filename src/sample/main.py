from game_logic import generate_random_number, check_guess
from user_interface import welcome_message, get_user_guess, show_result, game_over
from difficulty_levels import get_difficulty_level, get_number_range


def play_game():
    difficulty_level = get_difficulty_level()
    min_value, max_value = get_number_range(difficulty_level)
    secret_number = generate_random_number(min_value, max_value)

    welcome_message()

    attempts = 0
    while True:
        guess = get_user_guess()
        attempts += 1
        result = check_guess(guess, secret_number)
        show_result(result)
        if result == "Поздравляю, вы угадали!":
            print(f"Вы угадали за {attempts} попыток!")
            break

    game_over()


if __name__ == "__main__":
    play_game()
