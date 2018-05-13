#Introduction to Python List with application of Loop
"""
list1=["Rajesh","IT1217",1193923,"TCS","Kolkata"]
print(list1)
print(list1[1])
print(list1[-1])
print(list1[0:5])
print(list1[0:-1])

print("Kolkata" in list1)

print("CTS" in list1)

print(len(list1))

if list1:
    print("List is not Empty")
else:
    print("List is Empty")

for index in list1:
    print(index,end=' ')

list2=[1,2,3,4,5,6,7,8,9,10]

for x in list2[::4]:
    print(x)

print(list(range(1,15)))
print(list(range(1,15,2)))
print(list(range(15)))

"""
"""
#Else in Loop structure in Python
num=int(input("Enter a Range: "))
for index in range(1,num):
    print(index)
else:
    print("Bye Bye")
"""
"""
while True:
    n=int(input("Enter a Positive NonZero Number: "))
    if(n<0):
        continue
    elif(n==0):
        break
    print("The Square Value is: ",(n**2))
print("Good Bye")
"""






'''
Created on 10-May-2018

@author: RAJESH
'''
