from functools import reduce
l1=[1,2,3,4,5,6]
num=reduce(lambda x,y:x*y,l1)
print(num)