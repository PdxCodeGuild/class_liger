
numbers = []

while True: 
    numbers_wanted = input("\nEnter a number or type 'done' to quit: ")
    
    if numbers_wanted == 'done':
        averaged_numbers =  sum(numbers)/len(numbers)
        print(f"\nThe average is {averaged_numbers}")
        break
    else: 
        numbers.append(int(numbers_wanted))