# Introduction to Python Exception

#print(num) #Raises the NameError as the variable is not declared yet 

#print("Rajesh"+1193923) #Raises the TypeError as the operation is with different datatypes

#print(12/0) # Raises ZeroDivisionError as we can't devide the number y zero

#list1=[1,2,3,4]
#print(list1[4]) #Raises IndexError as the wrong index of the list is accessed

#num=int(input("Enter Number: ")) #Raises ValueError if enter non numeric number instead of numeric

"""
#Exception Handling Demo
def get_number():
    num=float(input("Enter a Float Value: "))
    return(num)

if(__name__=='__main__'):
    while(True):
        try:
            print("You Entered: ",get_number())
        
        except ValueError:
            print(" ValueEoor Exception Here")
            

"""    
#Raise Exception example in exception handling in Python
try:
    raise ValueError("A value error happened")

except:
    print("A Value Error in Our Code")

#Use of finally in the exception handling
try:
    fobj=open("hello.txt","w")
    res=12/5
except ZeroDivisionError:
    print("We have an error in division")
finally:
    fobj.close()
    print("closing the file object..")
    








'''
Created on 22-May-2018

@author: RAJESH
'''
