a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

b = []

while(True):
    try:
        number = int(input("Please type a number: "))
        break
    except ValueError:
        print("You must give a numeric value!")

for i in range(len(a)):
    try:
        if a[i] < number:
            b.append(a[i])
    except ValueError:
        print("Element on the list has not a numeric value. Check and then try once again.")
    finally:
        print("Finished checking ", str(i+1), " of ", str(len(a)), " elements")

print(b)