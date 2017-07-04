while(True):
    try:
        number = int(input("Please give an integer"))
        break
    except ValueError:
        print("Please give a valid INTEGER.\n")

divisors = []

for i in range(1, number+1):
    if number%i == 0:
        divisors.append(i)

print("Divisors of ", str(number), " are ", divisors)