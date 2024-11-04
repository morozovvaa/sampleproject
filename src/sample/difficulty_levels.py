def get_difficulty_level():
  while True:
    print("Выберите уровень сложности:")
    print("1. Легкий")
    print("2. Средний")
    print("3. Сложный")
    choice = input("Введите номер уровня: ")
    if choice in ["1", "2", "3"]:
      return choice
    else:
      print("Неверный выбор.")

def get_number_range(difficulty_level):
  if difficulty_level == "1":
    return 1, 10
  elif difficulty_level == "2":
    return 1, 50
  elif difficulty_level == "3":
    return 1, 100
