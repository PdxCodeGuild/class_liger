# Peaks and Valleys Lab

data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]
# peaks_var = []
# valleys_var = []
# peaks_and_valleys_var = []

def peaks(data):
    peaks_var = []
    for i in range(len(data) - 1):
        if i != 0 and (data[i] > (data[i - 1]) and data[i] > (data[i + 1])):
            peaks_var.append(i)
    return peaks_var

def valleys(data):
    valleys_var = []
    for i in range(len(data) - 1):
        if i != 0 and (data[i] < (data[i - 1]) and data[i] < (data[i + 1])):
            valleys_var.append(i)
    return valleys_var

def peaks_and_valleys(data):
    # peaks(data)
    # for i in range(len(peaks(data))):
    #     peaks_and_valleys_var.append(peaks_var[i])
    # # valleys(data)
    # for i in range(len(valleys(data))):
    #     peaks_and_valleys_var.append(valleys_var[i])
    
    peaks_and_valleys_var = []
    # peaks(data)
    # valleys(data)

    peaks_and_valleys_var.extend(peaks(data))
    peaks_and_valleys_var.extend(valleys(data))

    # peaks_and_valleys_var.append(peaks(data))
    # peaks_and_valleys_var.append(valleys(data))
    peaks_and_valleys_var.sort()
    return peaks_and_valleys_var




# print(peaks(data))
# print(valleys(data))
print(peaks_and_valleys(data))







#######################################################################

# Version 2



def draw_pic(data):
    pic_height = max(data)
    line_strings_list = []
    line_string = ''
    char_val = ''
    for h in range(0, pic_height):
        for i in range(len(data)):
            if data[i] >= (pic_height - h):
                char_val = "X "
            else:
                char_val = "  "
            line_string += char_val
        line_strings_list.append(line_string)
        line_string = ''
    # line_strings_list.reverse()
    for i in range(len(line_strings_list)):
        print(line_strings_list[i])
    # return line_strings_list

# print(draw_pic(data))
draw_pic(data)
             


