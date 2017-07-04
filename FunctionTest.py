def girls_range(age):
    max_age = age/2 + 7
    return max_age

for i in range(1,51):
    print("You are ", i, ".\n","You can date girls at the age of ", girls_range(i), " or older. ;)")