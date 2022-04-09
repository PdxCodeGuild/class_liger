# credit card validation

from tabnanny import check

user_input = input('Enter a 16 digit number: ')


numbers = list(user_input)
numbers = [int(i) for i in numbers]

check_digit = str(numbers[-1])

sliced = numbers[:-1:]

reversed_list = sliced[::-1]

reversed_list[::2] = [num*2 for num in reversed_list[::2]]

list = []
for num in reversed_list:
    if num > 9:
        list.append(num - 9)
    else:
        list.append(num)

sum = str(sum(list))

if sum[1] == check_digit:
    print("The card is valid!")
else:
    print("The card is invalid...")
