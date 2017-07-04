while(True):
    try:
        number = int(input("Hello! Please give your number.\n"))
        break
    except ValueError:
        print("Please type a NUMBER!")

if number%4 == 0:
    print("This number can be divided by 4.")
elif number%2 == 0:
    print("Number is even.")
else:
    print("Number is odd.")