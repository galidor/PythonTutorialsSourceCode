import random

word_list = ['relinquish', 'productive', 'attractive', 'definition', 'conclusion', 'provincial', 'memorandum']
random_password = word_list[random.randint(0, 6)]
random_password = list(random_password)
for i in range(3):
    counter = random.randint(0, 9)
    random_password[counter] = random_password[counter].upper()
    random_password.append(str(random.randint(0, 9)))
random_password = "".join(random_password)
print(random_password)
