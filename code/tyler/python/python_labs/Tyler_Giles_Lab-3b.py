# create a user inputted list of numbers and average them

nums = []
total = 0




while True:
    user_num = input("Enter a number or 'done': ")
    if user_num == 'done':
        print("\nOkey dokey, one moment...")
        break
    else:
        user_num = int(user_num)
        nums.append(user_num)
    
    
print(nums)
for num in nums:
    total += num


total = total / len(nums)

print(f"\nThe average of your numbers is {total}. ")

