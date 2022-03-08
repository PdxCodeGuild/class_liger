

import numbers


def num_Avg(nums):
    total = 0
    for num_1 in nums:
        total += num_1

        average = total / len(nums)
    return average


nums = []


while True:
    user_choice = input("Enter a number or 'done' to quit:\n")
    if user_choice == "done":
        break

    nums.append(int(user_choice))

num_2 = num_Avg(nums)


print(f"You entered {nums}")
print(f"The average of the numbers entered is {num_2}")
