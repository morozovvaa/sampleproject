from utils import clear_screen

def welcome_message():
  clear_screen()
  print("Добро пожаловать в игру 'Угадай число'!")
  print("Я загадал число, а вы должны его угадать.")

def get_user_guess():
  while True:
    try:
      guess = int(input("Введите ваше число: "))
      return guess
    except ValueError:
      print("Введите целое число!")

def show_result(message):
  print(message)

def game_over():
  print("Игра окончена! Спасибо за игру!")
