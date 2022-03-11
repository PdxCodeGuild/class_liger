
card_number = list(input("Please enter your credit card number:\n").strip())

check_digit = card_number.pop()

card_number.reverse()
doubled_digits = []

for index in range(len(card_number)):
    credits = card_number[index]
    if index % 2 == 0:
        doubled_check = int(credits) * 2
        if doubled_check > 9:
            doubled_check = doubled_check - 9

        doubled_digits.append(doubled_check)

    else:
        doubled_digits.append(int(credits))

second_digit_total = sum(doubled_digits)
total_1 = second_digit_total % 10

if total_1 == int(check_digit):
    print("Yous credit card number is valid")

else:
    print("Sorry your credit card number is invalid")
