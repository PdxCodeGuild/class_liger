# Peaks and Valleys Lab

data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]
peaks_var = []
valleys_var = []
peaks_and_valleys_var = []

def peaks(data):
    for i in range(len(data) - 1):
        if i != 0 and (data[i] > (data[i - 1]) and data[i] > (data[i + 1])):
            peaks_var.append(i)
    return peaks_var

def valleys(data):
    for i in range(len(data) - 1):
        if i != 0 and (data[i] < (data[i - 1]) and data[i] < (data[i + 1])):
            valleys_var.append(i)
    return valleys_var

def peaks_and_valleys(data):
    # peaks(data)
    for i in range(len(peaks(data))):
        peaks_and_valleys_var.append(peaks_var[i])
    # valleys(data)
    for i in range(len(valleys(data))):
        peaks_and_valleys_var.append(valleys_var[i])

    # peaks_and_valleys_var.append(peaks(data))
    # peaks_and_valleys_var.append(valleys(data))
    peaks_and_valleys_var.sort()
    return peaks_and_valleys_var




# print(peaks(data))
# print(valleys(data))
print(peaks_and_valleys(data))