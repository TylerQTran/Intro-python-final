import csv
X = []

dataX = open('C:/Users/tyler/OneDrive/Documents/python/Intro-python-final/dataX.csv')
dataY = open('C:/Users/tyler/OneDrive/Documents/python/Intro-python-final/dataY.csv')

dataX = csv.reader(dataX)
dataY = csv.reader(dataY)

print(dataX)
print(dataY)

For rows in dataX:
    x.append(rows[0])

print(X)