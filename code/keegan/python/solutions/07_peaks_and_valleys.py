

def peaks(data):
    peaks = []
    for i in range(1, len(data)-1):

        left = data[i-1]
        center = data[i]
        right = data[i+1]

        # print(left < center and center > right)
        if left < center > right:
            peaks.append(i)

    return peaks


def valleys(data):
    pass


def peaks_and_valleys(data):
    # define dictionary for results
    results = {
        'peaks': [],
        'valleys': []
    }

    for i in range(1, len(data)-1):

        left = data[i-1]
        center = data[i]
        right = data[i+1]

        # print(left < center and center > right)
        if left < center > right:
            results['peaks'].append(i)

        elif left > center < right:
            results['valleys'].append(i)

    return results





data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]




# a peak is defined as being greater than each of its neighbors

# print(peaks(data)) # [6, 14]
# print(peaks_and_valleys(data)) # {'peaks': [6, 14], 'valleys': [9, 17]}