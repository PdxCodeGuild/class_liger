# Credit card Validation

# Define some vars and take an input
int_credit_number = []
double_reverse = []
minus_9 = []
sum = 0

credit_number = input('Please enter a 16 digit credit card number: ')

# step 1 convert to list of ints
list_credit_number = list(credit_number.replace(" ", ""))
for x in list_credit_number:
    int_credit_number.append(int(x))

# step 2 slice and check digit
check_digit = int_credit_number[-1] 
int_credit_number.pop(-1)

# step 3 reverse them
reverse_credit = int_credit_number.copy()
reverse_credit.reverse()

# step 4 double every other
for index, value in enumerate(reverse_credit):
    if index % 2 == 0:
        value *= 2
        double_reverse.append(value)
    else:
        double_reverse.append(value)

# step 5 subtract 9        
for x in double_reverse:
    if x > 9:
        x -= 9
        minus_9.append(x)
    else:
        minus_9.append(x)

# step 6 sum them
for x in minus_9:
    sum += x

# step 7 find second digit
second_digit = sum % 10

# step 8 check if it matches
if second_digit == check_digit:
    print('Valid!')
else:
    print('Invalid!')


# Instructions
# Let's write a function which returns whether a string containing a credit card number is valid as a boolean. The steps are as follows:

# Convert the input string into a list of ints
# Slice off the last digit. That is the check digit.
# Reverse the digits.
# Double every other element in the reversed list.
# Subtract nine from numbers over nine.
# Sum all values.
# Take the second digit of that sum.
# If that matches the check digit, the whole card number is valid.