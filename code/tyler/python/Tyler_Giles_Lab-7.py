data = [1,2,3,4,5,6,7,6,5,4,5,6,7,8,9,8,7,6,7,8,9]              # example data 1,2,3,4,5,6,7,6,5,4,5,6,7,8,9,8,7,6,7,8,9       # file name Tyler_Giles_Lab-7
data_check = 1
peak_data = []
valley_data = []
peaks_and_valleys = []

for i in range(1, len(data) - 1):
    if data[i-1] < data[i] > data[i+1]:
        peak_data.append(i)
        peaks_and_valleys.append(i)

for i in range(1, len(data) - 1):
    if data[i-1] > data[i] < data[i+1]:
        valley_data.append(i)
        peaks_and_valleys.append(i)




print(f"\nThe indices of the peaks are {peak_data}.")
print(f"\nThe indices of the valleys are {valley_data}.")
print(f"\nThe indices of the peaks and the valleys are {peaks_and_valleys}.")
