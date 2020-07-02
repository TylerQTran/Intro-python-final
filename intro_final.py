import csv
X = []

dx = open('C:/Users/tyler/OneDrive/Documents/python/Intro-python-final/dataX.csv')
dataY = open('C:/Users/tyler/OneDrive/Documents/python/Intro-python-final/dataY.csv')

dataX = csv.reader(dx)
dataY = csv.reader(dataY)

for rows in dx:
    X.append(rows)
print(X)
