'''CreditCardValidationLab'''

credit_card = "4556 7375 8689 9855"
credit_card = credit_card.replace(" ", "")


credit_card = list(credit_card)
credit_card_numbers = []
for number1 in credit_card:
    number1 = int(number1)
    credit_card_numbers.append(number1)


print(f"\nOrigninal: {credit_card_numbers}")


check_value = credit_card_numbers[-1]
print(f"\nCheck Value: {check_value}")

credit_card2 = credit_card_numbers.copy()
credit_card2 = credit_card2[0:15]
print(f"\nCard no check value: {credit_card2}")

credit_card2.reverse()
print(f"\nReversed: {credit_card2}")

doubled_numbers = []
CardMultiplcation = credit_card2[::2]
for numbers in CardMultiplcation:
    numbers = numbers * 2
    doubled_numbers.append(numbers)

print(doubled_numbers)

del credit_card2[::2]
print(credit_card2)

credit_card3 = credit_card2 + doubled_numbers

print(f"\nCard with every other doubled: {credit_card3}")

subtracted_nine = []
lessThanNine = []

for nonsubtracted in credit_card3:
    
    if nonsubtracted >9:
        nonsubtractedMinusNine = nonsubtracted - 9
        subtracted_nine.append(nonsubtractedMinusNine)

    else:
        lessThanNine.append(nonsubtracted)
        
print(subtracted_nine)
print(lessThanNine)

credit_card4 = subtracted_nine + lessThanNine
print(credit_card4)


placeHolder = 0

for unaddedNumber in credit_card4:
    placeHolder += unaddedNumber

placeHolder = str(placeHolder)

placeHolder = list(placeHolder)

print(placeHolder[1], type(placeHolder[1]))

check_value = str(check_value)

print(check_value, type(check_value))

if placeHolder[1] == check_value:
    print("\nValid!")

else: 
    print('\nNot Valid :(')