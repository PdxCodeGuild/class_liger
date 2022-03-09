# Lab 03b Average Number


# function to calculate average
nums1 = [5, 0, 8, 3, 4, 1, 6]


def avg_num_v1(nums: list) -> float:
    pass
    running_total = 0
    for num in nums:
        running_total += num
        the_average = running_total / len(nums)
        the_average = round(the_average, 2)
    return the_average


print(avg_num_v1(nums1))


def avg_num_v2():
    pass
