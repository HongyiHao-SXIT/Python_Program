import random
difficulty_level = input("Difficulty level: (easy or hard)")
if difficulty_level == "easy":  # Determine selected difficulty
    randon_number = random.randint(1, 100)  # Random number range
    number_times = 0  # Attempts
    while True:
        number = int(input("Please enter a number:"))
        number_times += 1
        if number < randon_number:
            print("Too small")
        elif number > randon_number:
            print("Too big")
        else:
            print("Congratulations, you guessed it! You took {} attempts".format(number_times))
            break
    if number_times > 10:
        print("You need more practice")
elif difficulty_level == "hard":
    randon_number = random.randint(1, 100)  # Random number range
    number_times = 0  # Attempts
    chance = int(input("Please enter your desired number of attempts:"))
    while True:
        number = int(input("Please enter a number:"))
        number_times += 1
        if number > randon_number:
            print("Too big, you still have {} chances".format(chance - number_times))
        elif number < randon_number:
            print("Too small, you still have {} chances".format(chance - number_times))
        else:
            print("Correct, smart guess! You took {} attempts".format(number_times))
            break
        if chance - number_times == 0:
            print("You had your chance but missed it")
