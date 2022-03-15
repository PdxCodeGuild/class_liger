"""
    Lab 06b 
    Credit Card Validation

1. Convert the input string into a list of ints
2. Slice off the last digit.  That is the **check digit**.
3. Reverse the digits.
4. Double every other element in the reversed list.
5. Subtract nine from numbers over nine.
6. Sum all values.
7. Take the second digit of that sum.
8. If that matches the check digit, the whole card number is valid.

"""

ex = "4 5 5 6 7 3 7 5 8 6 8 9 9 8 5 5"
items = "' ',"


def list_of_ints(cc_as_str: list) -> list:
    credit_card_integer = []
    for num in range(len(cc_as_str)):
        credit_card_integer.append(int(cc_as_str[num]))
    return credit_card_integer


def sum(nums: list):
    total = 0
    for num in nums:
        total += num
    return total


def transform_to_check(cc_as_integers):
    cc_as_integers = cc_as_integers[::-1]
    print(cc_as_integers)

    for index in range(0, len(cc_as_integers), 2):
        cc_as_integers[index] *= 2
    print(cc_as_integers)

    numbers_to_sum = []
    for num in cc_as_integers:
        if num > 9:
            numbers_to_sum.append(num - 9)
        else:
            numbers_to_sum.append(num)
    print(numbers_to_sum)
    check_total = sum(numbers_to_sum)

    return check_total


credit_card_str = input(">>> enter your credit card number: ")

# removes & replaces items
for item in credit_card_str:
    if item in items:
        credit_card_str = credit_card_str.replace(item, "")

# handles too few or too many numbers
while len(credit_card_str) != 16:
    print(f"There must be 16 digits. You entered {len(credit_card_str)}; please try again")
    credit_card_str = input(">>> enter your credit card number: ")
    for item in credit_card_str:
        if item in items:
            credit_card_str = credit_card_str.replace(item, "")

# transforms cleaned input string to an integer
credit_card_integer = list_of_ints(credit_card_str)
print(credit_card_integer)
# sets aside check_digit
check_digit = credit_card_integer.pop(15)

# sets aside remaining 15 digits
credit_card_integer_15 = credit_card_integer
print(credit_card_integer_15)

check_total = transform_to_check(credit_card_integer_15)

check_digit = str(check_digit)
check_total = str(check_total)
print(check_total)
print(check_digit)


if check_total[1] == check_digit:
    print("Valid!")
else:
    print("Invalid")
