nums_2 = []

sum_3 = 0.0

done = str('done')
# -------------------PART TWO--------------------------PART TWO---------------------------PART TWO
while True:
    user_input = input(f"\nenter a number or enter 'done': ")        # user input

    user_input = float(user_input)                                   # user input converted to float

    nums_2.append(user_input)                                        # user input added to nums_2 list

    for num_2 in nums_2:                                             # for every number in list, add sum plus number
        sum_3 += num_2

    average_3 = sum_3 / len(nums_2)

    print(f"\n length: {len(nums_2)}")
    print(f"\n numbers: {nums_2}")
    print(f"\n Average: {average_3}")
    print(f"\n sum: {sum_3}")