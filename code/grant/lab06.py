





def valid_card(card_number):

    card_number = ""

    card_number = input("\nEnter your 16 digit card number: \n")

    card_number_list = [int(number) for number in card_number]

    # print(card_number_list)

    check_digit = card_number_list.pop(15)

    reversed_card_number = card_number_list[::-1]

    total = 0
    
    for index, number in enumerate(reversed_card_number):

        if index % 2 == 0:

            reversed_card_number[index] = reversed_card_number[index] + reversed_card_number[index]

    for index, number_2 in enumerate(reversed_card_number):

        if reversed_card_number[index] > 9:

            reversed_card_number[index] = reversed_card_number[index] - 9

    for number_3 in reversed_card_number:

        total += number_3

    new_total = str(total)  
    
    new_total = [int(x) for x in new_total]   

    check_digit_2 = new_total.pop()

    if check_digit_2 == check_digit:    

        print(f"\nValid!\n") 

    else:

        print(f"\nInvalid!\n")

    # print(total)

    # print(new_total)

    # print(check_digit_2)
    
valid_card(card_number=0)