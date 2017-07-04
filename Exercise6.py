schrodinger_palindrome = str(input("Please type a word and I'll check whether it is a palindrome or not.\n"))

if len(schrodinger_palindrome)%2:
    counter = int(len(schrodinger_palindrome)/2)
else:
    counter = int((len(schrodinger_palindrome)-1)/2)

palindrome = True

for i in range(counter):
    if not schrodinger_palindrome.lower()[i] == schrodinger_palindrome.lower()[len(schrodinger_palindrome)-i-1]:
        palindrome = False
        break

if palindrome:
    print(schrodinger_palindrome, " is a palindrome.")
else:
    print(schrodinger_palindrome, " is not a palindrome.")