def find_avg(nums):
    total = 0
    for num in nums: 
        total += num
    # print(total)
    avg = total / len(nums)
    # print(avg)
    return avg

response = None
nums = []

while response != 'done':
    response = input('\nPlease input a number to be averaged, input "done" when you are done: ')
    if response == 'done':
        break
    else:
        nums.append(int(response))
# print(nums)
print(find_avg(nums))