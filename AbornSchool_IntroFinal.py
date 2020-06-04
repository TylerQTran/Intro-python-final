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

data = open('C:/Users/balto/OneDrive/Desktop/AbornSchool/data.csv','w')
data2 = csv.writer(data)
data2.writerow(x_csv)
data2.writerow(y_csv)

plt.scatter(x, y)
plt.show()