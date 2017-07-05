def fibonacci(elements_number):

    tab = []

    for i in range(elements_number-1):
        if i == 0:
            tab.append(1)
        elif i == 1:
            tab.append(1)
        else:
            tab.append(tab[i-2]+tab[i-1])

    return tab

while True:
    try:
        elements_number = int(input("How many Fibonacci numbers do you want?\n"))
        if elements_number > 0:
            break
        else:
            print("Invalid number, please give a positive value.")
    except ValueError:
        print("Invalid number.")

print(fibonacci(elements_number))