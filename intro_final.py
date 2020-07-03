import matplotlib.pyplt as plt 
import csv
dataX = open('C:/Users/tyler/OneDrive/Documents/python/Intro-python-final/dataX.csv','r')
dataY = open('C:/Users/tyler/OneDrive/Documents/python/Intro-python-final/dataY.csv','r')
dataX = csv.reader(dataX)
dataY = csv.reader(dataY)
X = []
Y = []
for rows in dataX:
    if(len(rows)>0):
        if "X" not in rows[0]:
            X.append(float(rows[0]))
for rows in dataY:
    if(len(rows)>0):
        if "Y" not in rows[0]:
            Y.append(float(rows[0]))
print(X)
print(Y)
sumofarea = 0
for i in range(len(Y)):
    sumofarea+=((X[1] - X[0])*Y[i])
print(sumofarea)