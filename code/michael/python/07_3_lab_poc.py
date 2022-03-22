# Peaks and Valleys Lab

data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]

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
    line_string = '       '
    char_val = ''
    for h in range(0, pic_height):
        for i in range(len(data)):
            if data[i] >= (pic_height - h):
                char_val = "X  "
            else:
                char_val = "   "
            line_string += char_val
        # line_string += ' '
        line_strings_list.append(line_string)
        line_string = '       '
    # line_strings_list.reverse()

    #####################################################################

    # adding some code for version 3
    concave_list = []
    for i in range(len(line_strings_list)): # this iterates through the horizontal layers of the picture 
        concave = {}
        # concave_list = []
        for r in range((len(line_strings_list[i]) - 3)): # this iterates through the vertical slices of each horizontal layer
            # concave = {}
            if line_strings_list[i][r] == 'X' and line_strings_list[i][r + 3] == ' ': # this identifies the left wall of a cup
                # print(i)
                # print(r)
                beg = r
                # if line_strings_list[i][r + 2] == ' ':
                # beg = r
                for c in range(r + 3, (len(line_strings_list[i]))): # this iterates through the vertical slices, starting at where the previous iteration left off # this identifies the right wall of the cup
                    # beg = r
                    if line_strings_list[i][c] == 'X' and line_strings_list[i][c - 3] == ' ':
                    # if r != beg:  
                        # beg = r  
                        end = c
                        # elif line_strings_list[i][r - 2] == ' ':
                        #     end = r 
                        #     concave[beg]=end
                        concave[beg]=end
                        # print(concave)
                        break
                    
                # break    
        # print(concave)   
        # if concave != {}:
        concave_copy = concave.copy()
        concave_list.append(concave_copy)
        # print(concave_list)
        

        concave = {}
    print(concave_list)
    line_strings_list_concave = []#line_strings_list.copy()
    line_string_concave = ''
    for i in range(len(line_strings_list)): # changing the data to include O's
        
        line_string_concave = line_strings_list[i]
        dict_to_list = sorted(list(concave_list[i].items()))
        # print(dict_to_list[0][0])
        for d in range(len(dict_to_list)):
            beg = dict_to_list[d][0] + 1
            end = dict_to_list[d][1] - 1
            line_string_concave = line_string_concave[0:beg] + ('  O' * int(((end) - (beg) + 1)/3)) + '  ' + line_string_concave[end + 1:]
            # print(line_string_concave)
        # print(line_string_concave)
        line_strings_list_concave.append(line_string_concave)
        # line_string_concave = line_string_concave[]



    # adding the index of the data at the bottom
    ind = ''
    for i in range(len(data)):
        if i / 10 <= 1:
            ind += ' '
        ind += (str(i))
        ind += ' '

    for i in range(len(line_strings_list)):
        print(line_strings_list[i])
    print('\n')
    for i in range(len(line_strings_list_concave)):
        print(line_strings_list_concave[i])
    
    print(f'index {ind}')
    print(f'data  {data}')




# print(draw_pic(data))
draw_pic(data)
