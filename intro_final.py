import csv
X = []

dataX = open('C:/Users/tyler/OneDrive/Documents/python/Intro-python-final/dataX.csv')
dataY = open('C:/Users/tyler/OneDrive/Documents/python/Intro-python-final/dataY.csv')

dataX = csv.reader(dataX)
dataY = csv.reader(dataY)

print(dataX)
print(dataY)

for rows in dataX:
    print(rows)
