# Introduction to Python Classes and OOP concepts
"""
class MyFirstClass:
    nnm1=100
    num2=200
    

p=MyFirstClass()

print(p)
print(dir(p))

"""
#Introduction to Python __init__ method
class Student:
    """
    This class returs a Student object with the given name,branch and year
    """
    def __init__(self,name,branch,year):
        self.name=name
        self.branch=branch
        self.year=year
        print("A student object is created")
    
    def print_details(self):
        """
        Prints the details of the students
        """
        print("Name: ",self.name,end=' # ')
        print("Branch: ",self.branch,end=' # ')
        print("Year: ",self.year,end=' # ')
            
    
stdobj1=Student("Rajesh","Information Technology","2016")

stdobj1.print_details()

'''
Created on 23-May-2018

@author: RAJESH
'''
