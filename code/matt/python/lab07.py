"""
Lab 07
Peaks and Valleys

Define the following functions:

peaks(data) - Returns the indices of peaks. A peak has a lower number on both the left and the right.

valleys(data) - Returns the indices of 'valleys'. A valley is a number with a higher number on both the left and the right.

peaks_and_valleys(data) - uses the above two functions to compile a single list of the peaks and valleys in order of appearance in the original data.

                                                  X                 X
                                               X  X  X           X  X
                          X                 X  X  X  X  X     X  X  X
                       X  X  X           X  X  X  X  X  X  X  X  X  X
                    X  X  X  X  X     X  X  X  X  X  X  X  X  X  X  X
                 X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X
              X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X
           X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X
        X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X
# index 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20
data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]
peaks(data) # [6, 14]
valleys(data) # [9, 17]
peaks_and_valleys(data) # [6, 9, 14, 17]
"""

data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]


def peaks(nums: list) -> list:
    peaks = []
    for i in range(0, len(nums) - 2):
        left = nums[i]
        center = nums[i + 1]
        right = nums[i + 2]
        # print(i, nums[i])
        if left < center and left == right:
            # print(i + 1)
            peaks.append(i + 1)
            # print(peaks)
    return peaks


def valleys(nums: list) -> list:
    valleys = []
    for i in range(0, len(nums) - 2):
        left = nums[i]
        center = nums[i + 1]
        right = nums[i + 2]
        # print(i, nums[i])
        if left > center and left == right:
            # print(i + 1)
            valleys.append(i + 1)
            # print(valleys)
    return valleys


def peaks_and_valleys(nums: list) -> list:
    peaks_and_valleys = []
    for i in range(0, len(nums) - 2):
        left = nums[i]
        center = nums[i + 1]
        right = nums[i + 2]
        # print(i, nums[i])
        if (left < center and left == right) or (left > center and left == right):
            # print(i + 1)
            peaks_and_valleys.append(i + 1)
            # print(peaks)
    return peaks_and_valleys


print(peaks(data))
print(valleys(data))
print(peaks_and_valleys(data))
