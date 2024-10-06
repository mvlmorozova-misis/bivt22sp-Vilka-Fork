def welcome():
    print("Welcome to the Brain Games!")
    name = input("May I have your name? ")
    print(f"Hello, {name}!")

    return name

def choose_game():
    print("Choose the game:")
    print("1. NOK")
    print("2. Geometric progression")
    print("3. Exit")
    
    num_game = input("Selected game: ")
    
    return num_game