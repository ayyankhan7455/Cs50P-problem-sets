import random

def get_positive_integer(prompt):
    while True:
        try:
            user_input = input(prompt).strip()
            if not user_input:
                continue
            value = int(user_input)
            if value > 0:
                return value
        except ValueError:
            pass

def main():
    n = get_positive_integer("Level: ")
    target = random.randint(1, n)

    while True:
        guess = get_positive_integer("Guess: ")

        if guess < target:
            print("Too small!")
        elif guess > target:
            print("Too large!")
        else:
            print("Just right!")
            break

if __name__ == "__main__":
    main()
