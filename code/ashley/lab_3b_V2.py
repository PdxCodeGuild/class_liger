nums = []

while True:
    user_input = input("Enter a number or 'done:' ")    
    
    if user_input == 'done':
        break
    else:
        user_input = int(user_input)
        nums.append(user_input+0)
        continue

running_sum = 0
for num in nums:
    running_sum = running_sum + num

average = running_sum / len(nums)

output = f'average: {average}'

print(output)