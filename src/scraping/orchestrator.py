import csv

i= 0
Flight = []
Departure = []
Arrival = []
DepDate = []
RetDate = []
OWRT = []

with open('D:/Users/fcakin/Desktop/coflight/src/dataset/thy-international-dataset.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        for j in range(0,5):
            Flight.append([])
            Flight[i].append(row[j])
        i += 1
    for j in range(0,i):
        Departure.append(Flight[j][0])
        Arrival.append(Flight[j][1])
        DepDate.append(Flight[j][2])
        RetDate.append(Flight[j][3])
        OWRT.append(Flight[j][4])
    for j in range(0,i):
        print(Departure[j],Arrival[j],DepDate[j],RetDate[j],OWRT[j])