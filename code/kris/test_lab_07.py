
data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]
peaksList = []
valleyList = []
indexList = []

for number in range(len(data)):
    dataIndex = data[number]
    indexList.append(number)
# print(data)
# print(indexList)


# for place in indexList:
#     print(place)
 
for index in range(1, len(data) -1): 
    right_one = data[index + 1]   
    left_one = data[index - 1]
    one = data[index]

    if  left_one < one > right_one:
        # print(index)
        peaksList.append(index)

    if data[index] < data[index - 1] and data[index] < data[index + 1]:
        # print(index)
        valleyList.append(index)

print(f'''\nPeaks: {peaksList}
Valleys: {valleyList} ''')