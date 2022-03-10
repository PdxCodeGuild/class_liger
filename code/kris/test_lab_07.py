
data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]
peaksList = []
valleyList = []
indexList = []

for number in range(len(data)):
    dataIndex = data[number]
    indexList.append(number)
# print(data)
# print(indexList)



for x in range(1, len(data) -1): 
    if x > data[x]-1 and x > data[x]+1: 
        print(x)
        peaksList.append(x)

# print(peaksList)``