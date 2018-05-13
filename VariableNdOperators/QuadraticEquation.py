# Calculation of the equation: a*x*x+b*x+x=0
import math
a=int(input("Enter the value of a: "))
b=int(input("Enter the value of b: "))
c=int(input("Enter the value of c: "))
d=(b*b)-(4*a*c)
if(d<0):
    print("Roots are Imaginary")
else:
    root1=((-b)+math.sqrt(d))/(2.0*a)
    root2=((-b)-math.sqrt(d))/(2.0*a)
    print("Root1: ",root1)
    print("Root2: ",root2)


'''
Created on 09-May-2018

@author: RAJESH
'''
