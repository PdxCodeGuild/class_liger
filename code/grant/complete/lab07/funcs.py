





def valleys(data):

    valleys_list = []

    for i in range(1, len(data) - 1):

        if data[i] < data[i - 1] and data[i] < data[i + 1]:
           
           valleys_list.append(i)
            
    print(f"{valleys_list}\n")

def peaks(data):

    peaks_list = []

    for i in range(1, len(data) - 1):

        if data[i] > data[i - 1] and data[i] > data[i + 1]:

            peaks_list.append(i)

    print(f"\n{peaks_list}\n")

def peaks_and_valleys(data):

    peaks_and_valleys_list = []

    for i in range(1, len(data) - 1):

        if data[i] > data[i - 1] and data[i] > data[i + 1]:

            peaks_and_valleys_list.append(i)

        elif data[i] < data[i - 1] and data[i] < data[i + 1]:

            peaks_and_valleys_list.append(i)

    print(f"\n{peaks_and_valleys_list}")