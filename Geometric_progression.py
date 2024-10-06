import random

def generate_progression(length):
    start = random.randint(1, 10)  # Начальное значение
    ratio = random.randint(2, 5)    # Общий множитель
    progression = [start * (ratio ** i) for i in range(length)]
    return progression

def hide_element(progression):
    hidden_index = random.randint(0, len(progression) - 1)
    hidden_value = progression[hidden_index]
    progression[hidden_index] = '..'  # Заменяем элемент на '..'
    return hidden_value, progression

def geometric_progression(name):
    while True:
        length = random.randint(5, 10)  # Длина прогрессии от 5 до 10
        progression = generate_progression(length)
        hidden_value, displayed_progression = hide_element(progression)

        print("Question:", ' '.join(map(str, displayed_progression)))
        answer = input("Your answer: ")

        if answer.isdigit() and int(answer) == hidden_value:
            print("Correct!")
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{hidden_value}'.")
            print(f"Let's try again, {name}!")
            break
