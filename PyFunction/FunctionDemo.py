#Introduction To Python Functions/Methods
"""

#Palindrom Checking and other functions demo

def addition(num1,num2):
    return(num1+num2)

def subtraction(num1,num2):
    return(num1-num2)

def palindrom(str1):
    return(str1==str1[::-1])

if __name__ == '__main__':
    str2=input("Enter a Striing:  ")
    if(palindrom(str2)):
        print("Yes!! Palindrom")
    else:
        print("NO!! Not a Palindrom")

else:
    print(subtraction(18, 12))


print("Addition of two values is: %d"%addition(12, 15))

"""
#Checking Local and Global variables in python
"""
def modify(k):
    val=10
    print("This is inside Function: %d"%val)


val=1000
print("Before function call val=%d"%val)
modify(val)
print("After function call val=%d"%val)

"""
"""
def modify(k):
    global val
    val=10
    print("This is inside Function: %d"%val)


val=1000
print("Before function call val=%d"%val)
modify(val)
print("After function call val=%d"%val)

"""
"""
#Checking the Default Argument value in Python

def defargval(num1,num2=100):
    if(num1>num2):
        return(True)
    else:
        return(False)

print(defargval(111))
print(defargval(2000, 3000))

"""
#Default Argument value makes a difference for
#a mutable object like List 

def method(val,arr=[]):
    arr.append(val)
    return(arr)

print(method(100))
print(method(200))
print(method(300))

#To resolve the mutable object issue in default argument 
#method,have to use in the below way

def method1(val,arr=None):
    if(arr is None):
        arr=[]
        arr.append(val)
        return(arr)
    

print(method1(200))
print(method1(300))
print(method1(400))





'''
Created on 13-May-2018

@author: RAJESH
'''
