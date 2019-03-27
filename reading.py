import csv
import matplotlib.pyplot as plt
x=[]
y=[]
with open('mygraph.csv', 'r') as csvFile:
    reader = csv.reader(csvFile)
    for i in reader:
        x.append(i[0])
        y.append(i[1])
plt.bar(x,y)
plt.show()