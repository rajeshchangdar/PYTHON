#Introduction to Python Loop Structure
"""
#Print N numbers
num=int(input("Enter the Number: "))
ind=1
while(ind<num+1):
    print(ind,end=' ')
    ind+=1

#Fibonacci Series
num=int(input("\nEnter the Series Range: "))
a,b=0,1
while(b<num):
    print(b,end=' ')
    a,b=b,a+b

#Fibonacci Series with no of Terms
num=int(input("\nEnter the No of Terms: "))
a,b=0,1
index=0
while(index<=num):
    print(b,end=' ')
    a,b=b,a+b
    index+=1
"""
"""
#Power Series calculation  e**x where 0<x<1
x=float(input("Enter the value of x: "))
n=term=1
summ=1.0
while(n<=100):
    term=term*(x/n)
    summ+=term
    n+=1
    if(term<0.0001):
        break
print("The No of Times: %d and the Sum: %f"%(n,summ))

"""
"""
#Multiplication Table Calculation
print(15*"-"+"MULTIPLICATION TABLE"+(15*"-"))
print("-"*50)
index1=1
while(index1<=10):
    res=index1
    index2=1
    while(index2<=10):
        res=index2*index1
        print("%4d"%res,end=' ')
        index2+=1
    print("\n")
    index1+=1
print("-"*50)

"""
'''
Created on 09-May-2018

@author: RAJESH
'''
