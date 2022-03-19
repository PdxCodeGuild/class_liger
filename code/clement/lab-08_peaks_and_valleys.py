data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]

"""
first and last elements are not part of peak/valley values
peak = prev_num < curr_num > next_num
list()
while loop
"""


def peak_element(data: list[int]) -> list[int]:
    index = 0
    final_list = []


    while index < len(data):
        if index == 0 or index == (len(data) - 1):
            index += 1
            continue


        if data[index - 1] < data[index] and data[index] > data[index + 1]:
            final_list.append(index)
        index += 1
    return final_list

    
all_peaks = peak_element(data)
print(all_peaks)

# valley = prev_num > curr_num < next_num


def valley_values(data: list[int]) -> list[int]:
    index = 0
    final_valeus = []


    while index < len(data):
        if index == 0 or index == (len(data) - 1):
            index += 1
            continue

        if data[index - 1] > data[index] and data[index] < data[index + 1]:
            final_valeus.append(index)
        index += 1
    return final_valeus


valley_elements = valley_values(data)
print(valley_elements)

# peak + valley into one list
# how do l know the length of the finale list
# algorithm to use
# data structure ->list()
# looping index > next


def peak_valley(data: list[int]) -> list[int]:
    final_values = []
    final_values += peak_element(data)  
    final_values += valley_values(data) 


    final_values.sort()
    return final_values


total_final_result = peak_valley(data)
print(total_final_result)




