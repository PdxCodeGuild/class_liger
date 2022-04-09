

def card_number_is_valid(cc_number):
    '''Return a boolean indicating if the given card number is valid or not'''

    # remove leading/trailing whitespace
    cc_number = cc_number.strip()
    # print(cc_number)

    # replace all blank spaces with blank strings
    cc_number = cc_number.replace(' ', '')
    # print(cc_number) # 4556737586899855

    # Convert the input string into a list of ints
    cc_number = list(cc_number)
    # print(cc_number) # ['4', '5', '5', '6', '7', '3', '7', '5', '8', '6', '8', '9', '9', '8', '5', '5']

    # ------------------------------------------------------------- #

    # loop through the indices of the list
    for index in range(len(cc_number)):
    #     # convert the character at the index to an integer
        cc_number[index] = int(cc_number[index])

    # print(cc_number) # [4, 5, 5, 6, 7, 3, 7, 5, 8, 6, 8, 9, 9, 8, 5, 5]

    cc_number = [int(x) for x in cc_number]

    # ------------------------------------------------------------- #
    # Slice off the last digit. That is the check digit.

    check_digit_1 = cc_number.pop()

    # print(check_digit_1) # 5
    # print(cc_number) # [4, 5, 5, 6, 7, 3, 7, 5, 8, 6, 8, 9, 9, 8, 5]

    # ------------------------------------------------------------- #
    # Reverse the digits.

    cc_number = cc_number[::-1]
    # print(cc_number) # [5, 8, 9, 9, 8, 6, 8, 5, 7, 3, 7, 6, 5, 5, 4]

    # # the "long way" to reverse with looping backwards through the indices
    # reversed_cc_number = []
    # for index in range(len(cc_number)-1, -1, -1):
    #     reversed_cc_number.append(cc_number[index])

    # print(reversed_cc_number)

    # ------------------------------------------------------------- #
    # Double every other element in the reversed list.
    # &
    # Subtract nine from numbers over nine.

    # loop through the indices
    for index in range(len(cc_number)):
        # at even indices
        if index % 2 == 0:
            # multiply the value at the index by 2
            cc_number[index] *= 2

        # if the value at the index is greater than 9, 
        if cc_number[index] > 9:
            # subtract 9
            cc_number[index] -= 9

    # list comprehension
    # cc_number = [cc_number[i]*2 if i % 2 == 0 else cc_number[i] for i in range(len(cc_number))]
    # cc_number = [cc_number[i]-9 if cc_number[i] > 9 else cc_number[i] for i in range(len(cc_number))]

    # print(cc_number) # [1, 8, 9, 9, 7, 6, 7, 5, 5, 3, 5, 6, 1, 5, 8]
    # ------------------------------------------------------------- #
    # Sum all values.
    total = sum(cc_number)

    # ------------------------------------------------------------- #
    # Take the second digit of that sum.
    check_digit_2 = total % 10

    # if converting to string:
    # total = str(total)[1]
    # print(type(total))

    # ------------------------------------------------------------- #
    
    # If the check digits match, the whole card number is valid.
    # return True or False
    return check_digit_1 == check_digit_2



cc_numbers = {
    'valid': "      \n   4 5 5 6 7 3 7 5 8 6 8 9 9 8 5 5     \n",
    'invalid': "      \n   4554 7375 8689 3855     \n"
}

for key in cc_numbers.keys():
    card_number = cc_numbers[key]
    is_valid = card_number_is_valid(card_number)
    print(is_valid)
