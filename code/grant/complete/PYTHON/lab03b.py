





# # -------------------PART ONE--------------------------PART ONE---------------------------PART ONE
def average_lab01():

    p1 = float(input("\nPlease enter a number: "))            # user input for self test   
    p2 = float(input("\nPlease enter another number: "))      # user input for self test       
    p3 = float(input("\nPlease enter another number: "))      # user input for self test      
    p4 = float(input("\nPlease enter another number: "))      # user input for self test         
    p5 = float(input("\nPlease enter another number: "))      # user input for self test      
    p6 = float(input("\nPlease enter another number: "))      # user input for self test       
    p7 = float(input("\nPlease enter another number: "))      # user input for self test        

    number_list = [p1, p2, p3, p4, p5, p6, p7]     # test list for self study

    nums = [5.0, 0.0, 8.0, 3.0, 4.0, 1.0, 6.0]   # given number list

    sum = 0

    sum_2 = 0

    for digits in number_list:
        sum_2 += digits

    for num in nums:
        sum += num

    average = sum / len(nums)

    average_2 = sum_2 / len(number_list)

    print(f"\nThe sum of this list is {sum}, and the average of this list is {average}.")

    print(f"\nThe sum of the entered number is {sum_2}, and the average is {average_2}.")


# # -------------------PART TWO--------------------------PART TWO---------------------------PART TWO
def average_lab02():

    nums_2 = []

    sum_3 = 0.0

    done = str('done')

    while True:
        user_input = input(f"\nenter a number or enter 'done': ")        # user input

        if user_input == done:
            print(f"\nThe average is {average_3}.")
            break

        user_input = float(user_input)                                   # user input converted to float
    
        nums_2.append(user_input)
                                            
        sum_3 = sum_3 + user_input

        average_3 = sum_3 / len(nums_2)

        print(f"\n length of list: {len(nums_2)}")
        print(f"\n numbers list: {nums_2}")
        print(f"\n Average: {sum_3 / len(nums_2)}")
        print(f"\n sum: {sum_3}")
        
average_lab01()
average_lab02()