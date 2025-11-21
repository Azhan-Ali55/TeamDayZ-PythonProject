import random

gameRunning: bool = True
firstRun = True
while gameRunning:
    if not firstRun:
        print("\n")

    random_number: int = random.randint(1, 50)
    tries: int = 0

    while True:
        user_input: int = int(input("Enter a number: "))
        difference: int = user_input - random_number
        end_str: str = "low" if difference < 0 else "high"
        tries += 1

        if difference == 0:
            print("> You guessed correctly!")
            print(f"> It took you {tries} tries.")
            break
        elif abs(difference) > 10:
            print(f"You guessed too {end_str}")
        else:
            print(f"You guessed {end_str}")

    gameRunning = (
        True if input("Play again (y: continue, otherwise quit): ") == "y" else False
    )
    firstRun = False


print("\n\nQuitting...")
