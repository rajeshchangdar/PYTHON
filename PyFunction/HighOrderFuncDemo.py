"""

#Introduction to Doc String in Python
import math

def longest_side(num1,num2):
    
    Function to find the length of the longest side of the right triangle
    :arg num1: side a of the triangle
    :arg num2: side b of the triangle
    :return: Length of the longest side num3 as the Floot
    
    
    num3=math.sqrt(num1*num1 + num2*num2)
    return(num3)

if(__name__=='__main__'):
    num1=int(input("Enter First Side: "))
    num2=int(input("Enter Second Side:"))
    print(int(longest_side(num1, num2)))
    
 
"""
#Function as an Argument in Python
def addlist(numlst): #normal function
    return(sum(numlst))

def main(f,*args):#function as an argument
    res=f( *args )
    print(res)

if(__name__=='__main__'):
    main(addlist,[1,2,3,4,5])


#Introduction to Higher Order Function in Python
def twoadd(x,y):
    return(x+y)
 
def threeadd(x,y,z):
    return(x+y+z)
 
def addfunc(nums):
    if(nums==3):
        return(threeadd)
    else:
        return(twoadd)
    


if(__name__=='__main__'):
    args=[1,2,3]
    resfunc=addfunc(len(args))
    print(resfunc)
    print(resfunc(*args)) #Unpacking the arguments

    list1=[7,5]
    resfunc=addfunc(len(list1))
    print(resfunc(*list1))
    


'''
Created on 21-May-2018

@author: RAJESH
'''
