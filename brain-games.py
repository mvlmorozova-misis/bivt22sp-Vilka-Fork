import sys

sys.path.append("C:/Users/Виолетта/Documents/Мисис/МОИ РАБОТЫ/Методологии разработки ПО/Задание 1/src")

from NOK import nok
from Geometric_progression import geometric_progression
from cli import welcome, choose_game


if __name__ == "__main__":
    name = welcome()

    while True:
        game_choice = choose_game()
        if game_choice == '1':
            nok(name)
        elif game_choice == '2':
            geometric_progression(name)
        elif game_choice == '3':
            print("See you later!")
            break
        else:
            print("Invalid choice. Please select either 1, 2 or 3.")
