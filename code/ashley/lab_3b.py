nums = [5, 0, 8, 3, 4, 1, 6]

running_sum = 0
for num in nums:
    running_sum = running_sum + num

average = running_sum / len(nums)


print(average)