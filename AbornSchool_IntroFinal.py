import matplotlib.pyplot as plt
import math
import csv

x_csv = []
y_csv = []
x = [] 
y = []

x2_csv = []
y2_csv = []
x2 = []
y2 = []
for i in range(1001):
    x_csv.append(str((2*math.pi*i)/1000))
    y_csv.append(str(math.sin((2*math.pi*i)/1000)))
    x.append(((2*math.pi*i)/1000))
    y.append((math.sin((2*math.pi*i)/1000)))

for i in range(1000):
    x2_csv.append(str((2*math.pi*i)/1000))
    y2_csv.append(str(math.exp((2*math.pi*i)/1000)*math.sin((2*math.pi*i)/1000)))
    x2.append(((2*math.pi*i)/1000))
    y2.append((math.exp((2*math.pi*i)/1000)*math.sin((2*math.pi*i)/1000)))

data_x = open('C:/Users/balto/OneDrive/Desktop/AbornSchool/dataX.csv','w')
data_y = open('C:/Users/balto/OneDrive/Desktop/AbornSchool/dataY.csv','w')

data_x2 = open('C:/Users/balto/OneDrive/Desktop/AbornSchool/dataX2.csv','w')
data_y2 = open('C:/Users/balto/OneDrive/Desktop/AbornSchool/dataY2.csv','w')

data2 = csv.writer(data_x)
data2.writerow({'X values of sin'})
for i in range(len(x_csv)):
    data2.writerow({x_csv[i]})

data3 = csv.writer(data_y)
data3.writerow({'Y values of sin'})
for i in range(len(y_csv)):
    data3.writerow({y_csv[i]})
    #data2.writerow(y_csv[i])

#print(x2_csv)
data4 = csv.writer(data_x2)
data4.writerow({'X values of sin'})
for i in range(len(x2_csv)):
    data4.writerow({x2_csv[i]})

data5 = csv.writer(data_y2)
data5.writerow({'Y values of sin'})
for i in range(len(y2_csv)):
    data5.writerow({y2_csv[i]})
    #data2.writerow(y_csv[i])

plt.scatter(x2, y2)
plt.show()