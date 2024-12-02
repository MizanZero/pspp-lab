from array import *

a=array('i',[])
n=int(input("How many elements?: "))

for i in range(n):
    x=int(input("Enter element"))
    a.append(x)

print(a)
