
card_num = list(input("Please enter your credit card number:\n").strip())

check_digit = card_num.pop()

card_num.reverse()
double_digits = []

for num1 in range(len(card_num)):

    if num1 % 2 == 0:
        double_digits.append(int(num1) * 2)

        print(double_digits)

    # else:
    #     if num2 % 2 != 0:
    #     double_digits.append(int(num2))


#     if num_1 % 2 == 0:
#         double_digits.append(int(num_2) * 2)

#     else:
#         double_digits.append(int(num_2))

#     print(double_digits)
# print(check_digit)
