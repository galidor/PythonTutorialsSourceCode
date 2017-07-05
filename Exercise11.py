def get_number():
    while True:
        try:
            number = int(input("Please give me a number: "))
            if number > 0:
                return number
        except ValueError:
            print("Given number is invalid. Please type an integer.")


def is_prime(number):
    counter = 0
    for i in range(1, (number+1)):
        if number%i == 0:
            counter += 1
    if counter > 2:
        return False
    else:
        return True


x = get_number()
if is_prime(x):
    print("Number ", str(x), " is prime.")
else:
    print("Number ", str(x), " is not prime.")