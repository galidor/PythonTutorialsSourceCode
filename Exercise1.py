import datetime

while(True):
    try:
        name = str(input("What is your name buddy?\n"))
        break
    except ValueError:
        print("Seriously, what is your name?\n")

while(True):
    try:
        age = int(input("How old are you?\n"))
        break
    except ValueError:
        print("That is not the valid age, input numeric value.\n")

now = datetime.datetime.now()

current_year = now.year

year_to_turn_hundred = current_year + (100 - age)

print("Hello ", name, ", nice to meet you! You will be 100 years old in ", str(year_to_turn_hundred))
