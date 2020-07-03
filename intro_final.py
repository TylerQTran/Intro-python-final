import csv
dataX = open('C:/Users/tyler/OneDrive/Documents/python/Intro-python-final/dataX.csv')
dataY = open('C:/Users/tyler/OneDrive/Documents/python/Intro-python-final/dataY.csv')
dataX = csv.reader(dataX)
dataY = csv.reader(dataY)
X = []
for rows in dataX:
     X.append(len(rows[0])>0)
for rows in dataY:
     X.append(len(rows[0])>0)
print(X)

the.plot (dataX) 