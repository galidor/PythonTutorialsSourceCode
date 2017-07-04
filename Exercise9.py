import random

print("Guessing Number Game")

number = random.randrange(1, 10)

while True:

    while True:
        try:
            guess = int(input("Please give a number between 1 and 9: "))
            if guess in range(1, 10):
                break
            else:
                print("Give a proper number. You need to type an integer between 1 and 9.")
        except ValueError:
            print("Give a proper number. You need to type an integer between 1 and 9.")

    if guess == number:
        print("Congratulations! You have guessed the correct number which was ", str(number), "!")
        break
    elif guess < number:
        print("Your number is less than target number. Try once again.")
    elif guess > number:
        print("Your number is greater than target number. Try once again.")
    else:
        print("An error occured. Try once again.")