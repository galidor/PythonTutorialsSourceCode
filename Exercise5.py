import random

failure_counter = 5

while failure_counter > 0:
    try:
        size1 = int(input("Please give the length of first list: "))
        if size1 > 1:
            break
        else:
            print("Type an integer greater than 1")
    except ValueError:
        failure_counter -= 1
        print("Error, please give a valid integer, ", str(failure_counter), " attempts left.")
        if failure_counter == 0:
            print("Too many failed attempts. Exiting...")
            exit()

failure_counter = 5

while failure_counter > 0:
    try:
        size2 = int(input("Please give the length of first list: "))
        if size2 > 1:
            break
        else:
            print("Type an integer greater than 1")
    except ValueError:
        failure_counter -= 1
        print("Error, please give a valid integer, ", str(failure_counter), " attempts left.")
        if failure_counter == 0:
            print("Too many failed attempts. Exiting...")
            exit()

list1 = []
list2 = []

common_numbers = []

for i in range(size1):
    list1.append(random.randrange(1, 100))

for i in range(size2):
    list2.append(random.randrange(1, 100))

print("Lists created!\nList 1: ", list1, "\nList 2: ", list2)

for i in range(len(list1)):
    for j in range(len(list2)):
        if list1[i] == list2[j] and not list1[i] in common_numbers:
            common_numbers.append(list1[i])

print("Common numbers are: ", common_numbers)