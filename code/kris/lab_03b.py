
numbers = [5, 1, 8, 3, 4, 1, 6]
added_number = 0
averaged_number = []
for number in numbers:
    added_number += number
    averaged_number.append(added_number)
    
    # print(added_number)
    print(averaged_number)


for i in range(len(numbers)):
    print(added_number)
    


# # while True: 
# #     numbers_wanted = input("\nEnter a number or type 'done' to quit: ")
    
# #     if numbers_wanted == 'done':
# #         averaged_numbers =  sum(numbers)/len(numbers)
# #         print(f"\nThe average is {averaged_numbers}")
# #         break
# #     else:
# #         numbers.append(int(numbers_wanted))