# Pattern Rendering using Python Loops
#Pattern Type-1
num=int(input("Enter the No of Rows: "))
index=num
while(index>=1):
    i=1
    while(i<=index):
        print("*",end=' ')
        i+=1
    print("\n")
    index-=1

#Pattern Type-2 
#This is the bad approach..should use single loop for this pattern printing
num=int(input("Enter the No of Rows: "))
index=1
while(index<=num):
    i=1
    while(i<=index):
        print("*",end=' ')
        i+=1
    print("\n")
    index+=1

#Pattern Type-3
num=int(input("Enter the No of Rows: "))
index=num
while(index>=1):
    x="*"*index
    y=" "*(num-index)
    print(y+x)
    index-=1

'''
Created on 09-May-2018

@author: RAJESH
'''
