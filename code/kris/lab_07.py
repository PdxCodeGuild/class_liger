
data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]

def peaks(x):
    peak_list = []
    for index in range(1, len(data) -1): 
        right_one = data[index + 1]   
        left_one = data[index - 1]
        one = data[index]

        if  left_one < one > right_one:
            peak_list.append(one)
    return peak_list

def valley(x):
    valley_list = []
    for index in range(1, len(data) -1): 
        right_one = data[index + 1]   
        left_one = data[index - 1]
        one = data[index]
        if  left_one > one < right_one:
            valley_list.append(one)
    return valley_list

def peaks_and_valley(x):
    pv_list = []
    for index in range(1, len(data) -1): 
        r_one = data[index + 1]   
        l_one = data[index - 1]
        one = data[index]
        if  l_one < one > r_one or l_one > one < r_one:
            pv_list.append(one)
    return pv_list

p_check = peaks(data)
v_check = valley(data)
pv_check = peaks_and_valley(data)

print(f'''\nPeaks: {p_check}
Valleys: {v_check}
Peaks and Valleys: {pv_check}''')
