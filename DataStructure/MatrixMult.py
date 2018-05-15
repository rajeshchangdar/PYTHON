# Takeing Matrix input and Manipulation
order=int(input("Enter the Order of the Square Matrix: "))
mat1=[]
for i in range(0,order):
    mat1.append([int(index) for index in input("").split(" ")])


print("The Entered Matrix is: \n")
print("-"*15)
for i in mat1:
    for j in i:
        print("%d"%j, end=' ')
    print(" ")


'''
Created on 15-May-2018

@author: RAJESH
'''
