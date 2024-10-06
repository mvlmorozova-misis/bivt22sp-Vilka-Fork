import random
import math
from functools import reduce

def lcm(a, b):
    return abs(a * b) // math.gcd(a, b)

def lcm_multiple(numbers):
    return reduce(lcm, numbers)

def nok(name):
    rounds = 3
    for _ in range(rounds):
        numbers = [random.randint(1, 100) for _ in range(3)]
        correct_answer = lcm_multiple(numbers)

        print(f"Question: {' '.join(map(str, numbers))}")
        user_answer = int(input("Your answer: "))

        if user_answer == correct_answer:
            print("Correct!")
        else:
            print(f"'{user_answer}' is wrong answer; Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return