# Dice simulator using random module
import random

while True:
    command = input("Press Enter to roll the dice, or type q to quit: ").strip().lower()
    if command == "q":
        print("Thanks for playing!")
        break

    result = random.randint(1, 6)
    print("You rolled:", result)
