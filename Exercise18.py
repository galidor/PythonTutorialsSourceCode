if __name__ == "__main__":
    import random

    number = random.randint(1000, 9999)
    number_list = list(str(number))

    def check(guess):
        cow = 0
        bull = 0
        guess_list = list(str(guess))
        for i in range(len(guess_list)):
            if number_list[i] == guess_list[i]:
                cow += 1
            elif guess_list[i] in number_list:
                bull += 1
        return [cow, bull]

    def game_start():
        guess = 0
        while guess is not number:
            while True:
                try:
                    guess = input("Give me a number, please: ")
                    if guess == "help":
                        break
                    else:
                        guess = int(guess)
                    if guess > 999 and guess < 10000:
                        break
                    else:
                        print("Number is incorrect, try again.")
                except ValueError:
                    print("Number is incorrect, try again.")
            cows_bulls = check(guess)
            if guess == number:
                print("Congratulations, you win!")
                break
            elif guess == "help":
                print("You asked for help, number you are trying to guess is", number)
            else:
                print("You have ", cows_bulls[0], " cows and ", cows_bulls[1], " bulls. Try again!")

    game_start()