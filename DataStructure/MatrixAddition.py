row=int(input("Enter the row number: "))
col=int(input("Enter the column number: "))

mat1=[]

print("Enter Matrix:\n")
for i in range(0,col):
    mat1.append([int(x) for x in input().split()])

print("The Entered Matrix is: \n")
for index1 in mat1:
    for index2 in index1:
        print("%5d"%index2,end=' ')
    print(" ")


'''
Created on 15-May-2018

@author: RAJESH
'''
