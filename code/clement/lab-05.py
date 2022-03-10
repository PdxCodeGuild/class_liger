

check_p = input("Please enter a wold: ")


def palindromes(check_p):
    choices = list(check_p)
    palindromes = True

    for choice in choices:
        if choice == choices[-1]:
            choices.pop()

        else:
            palindromes = False
            break
    return palindromes


if palindromes(check_p) == True:

    print(f"{check_p} is a palindrome")

else:
    print(f"{check_p} is not a palindrome")
