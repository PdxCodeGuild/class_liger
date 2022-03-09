# Lab 03b Average Number


# function to calculate average
nums1 = [5, 0, 8, 3, 4, 1, 6]


def avg_num_v1(nums: list) -> float:
    running_total = 0
    for num in nums:
        running_total += num
        the_average = running_total / len(nums)
        the_average = round(the_average, 2)
    return the_average


avg_num_v1(nums1)

# Ask the user to enter the numbers one at a time, putting them into a list. If the user enters 'done', then calculate and display the average.


def avg_num_v2(nums: list) -> float:

    nums = []
    num_entered = []

    while num_entered != "done":
        num_entered = input("> enter a number, or 'done': ")
        if num_entered == "done":
            answer = avg_num_v1(nums)
        else:
            num_entered = int(num_entered)
            nums.append(num_entered)

    print(
        f"""
    You entered: {nums}
    Average: {answer}
    """
    )


avg_num_v2(nums1)
