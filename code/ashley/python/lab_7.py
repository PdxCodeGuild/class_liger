"""Lab 7 - Peaks and Valleys"""

# from operator import index


# def peak(list):
#     nums = []
#     for num in nums:
#         if num[-1]:
#             print(num)
        
#     # return index
# # index + 1

# nums = [1,2,3]

# peak(nums)

def p_&_v(data):




def peaks(data):
    peaks = []
    for i in range(1, len(data)-1):
    

        left = data[i-1]

        center = data[i]

        right = data[i+1]

        if left < center > right:
            peaks.append(i)
    return peaks

    


data = [1,2,3,4,5,6,7,6,5,4,5,6,7,8,7,6,7,8,9]

print(peaks(data))