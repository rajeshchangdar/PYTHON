#Introduction to Map Function
"""
# Map takes one function and one iterator as input and operates on the iterator
print(":::::::MAP():::::::")
def findpower(num):
    return(num**2)

if(__name__=='__main__'):
    lst=[1,2,3,4]
    print(list(map(findpower,lst)))
   
"""
from _ctypes_test import func
"""
#Introduction to Closure
def outer_func(num):
    
    def inner_func(number):
        return(num+number)
    
    return(inner_func)
     
val=outer_func(1000)
print(val)
print(val(1))
print(val(2))

"""
#Introduction to Decorators
#Decorator Example-1
def my_redec_func(f2):
    
    def wrap_func(*args,**kwargs):
        res=f2(*args,**kwargs)
        print(" works as a Systems Engineer at TCS-Kolkata",end=' ')
        return(res)
        
    return(wrap_func)


def my_decorator_func(f1):
    
    def wrap_func(args):
        print("Mr.",end=' ')
        res=f1(args)
        return(res)
    return(wrap_func)    

@my_redec_func
@my_decorator_func
def my_func(fname):
    print(fname,end=' ')


if(__name__=='__main__'):
    nm=input("Enter the Name: ")
    my_func(nm) #Currently Using the function call

'''
Created on 21-May-2018

@author: RAJESH
'''
