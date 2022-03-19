





import funcs

data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]

# def peaks(data):

#     peaks_list = []

#     for i in range(1, len(data) - 1):

#         if data[i] > data[i - 1] and data[i] > data[i + 1]:

#             peaks_list.append(i)

#     print(f"\n{peaks_list}\n")
            
# def valleys(data):

#     valleys_list = []

#     for i in range(1, len(data) - 1):

#         if data[i] < data[i - 1] and data[i] < data[i + 1]:
           
#            valleys_list.append(i)

#     print(f"\n{valleys_list}\n")
    
# peaks(data)

# valleys(data)

# peaks_and_valleys(data)

funcs.valleys(data)

funcs.peaks(data)

funcs.peaks_and_valleys(data)