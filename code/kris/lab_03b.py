numbers = [5, 1, 8, 3, 4, 1, 6]
averaged_number = []
added_number = 0

for number in numbers:
        added_number += number
        averaging = added_number / len(numbers)
        averaged_number.append(averaging)

print(f"\nThe average is: {averaged_number[-1]}")
    


