import csv
dataX = open('C:/Users/tyler/OneDrive/Documents/python/Intro-python-final/dataX.csv')
dataY = open('C:/Users/tyler/OneDrive/Documents/python/Intro-python-final/dataY.csv')
dataX = csv.reader(dataX)
dataY = csv.reader(dataY)
X = []
for rows in dataX:
    if len(float(rows[0])>0):
         X.append(float(rows[0]))
print(X)