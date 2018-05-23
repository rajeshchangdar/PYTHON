#Here are some features of class
"""
#Example of deleting an object
class Calc:
    def __init__(self):
        
        print("One Claculator object is created")
    
    def add(self,num1,num2):
        return(num1+num2)


calcobj=Calc()

print(calcobj.add(12, 18))

del(calcobj)

print(calcobj)

"""
#Getters and Setters in Python
class Student(object):
    def __init__(self,name):
        self.name=name

stdobje=Student("Rajesh Changdar")

print(stdobje.name)

stdobje.name="Tamal Khamrui"

print(stdobje.name)




'''
Created on 23-May-2018

@author: RAJESH
'''
