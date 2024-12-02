from numpy import *

rows=int(input("Enter number of rows: "))
cols=int(input("Enter number of coloumns: "))

m1=zeros((rows,cols))

for i in range(rows):
    for j in range(cols):
        m1[i][j]=int(input("Enter element: "))

print(m1)

