import matplotlib.pyplot as plt
import math
import csv

x_csv = []
y_csv = []
x = [] 
y = []

for i in range(1001):
    x_csv.append(str((2*math.pi*i)/1000))
    y_csv.append(str(math.sin((2*math.pi*i)/1000)))
    x.append(((2*math.pi*i)/1000))
    y.append((math.sin((2*math.pi*i)/1000)))

data_x = open('C:/Users/balto/OneDrive/Desktop/AbornSchool/dataX.csv','w')
data_y = open('C:/Users/balto/OneDrive/Desktop/AbornSchool/dataY.csv','w')

data2 = csv.writer(data_x)
data2.writerow({'X values of sin'})
for i in range(len(x_csv)):
    data2.writerow({x_csv[i]})

data3 = csv.writer(data_y)
data3.writerow({'Y values of sin'})
for i in range(len(y_csv)):
    data3.writerow({y_csv[i]})
    #data2.writerow(y_csv[i])

#plt.scatter(x, y)
#plt.show()