import array

a=array.array('i',[1,2,3])



print(a)



for i in a:
    print(i,end=' ')
print()



for i in range(len(a)):
    print(a[i],end=' ')
print()


