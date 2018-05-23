# Introduction to Python Inheritance
class Person(object):
    """
    This class returns a Person object with the given name
    
    """
    def __init__(self,name):
        self.name=name
        
    def get_details(self):
        """
        This function returns a string containing the name of the person
        """    
        return(self.name)
        
class Student(Person):
    """
    This class returns a Student object taking 3 aruments name,branch,year
    """
    def __init__(self,name,branch,year):
        Person.__init__(self, name)
        self.branch=branch
        self.year=year
    
    def get_details(self):
        
        return("%s studies %s of year %s"%(self.name,self.branch,self.year))
    
    
class Teacher(Person):    
    """
    This class returns a Teacher object and takes a list of subjects as the arguments
    """
    def __init__(self,name,papers):
        Person.__init__(self, name)
        self.papers=papers
    
    def get_details(self):
        return("%s teaches %s"%(self.name,','.join(self.papers)))
    

# This is the function calling Part
p1=Person("Tamal")
print(p1.get_details())    

s1=Student("Rajesh"," IT ","2016")    
print(s1.get_details())
    
t1=Teacher("Koushik",['SE','CD','CG'])

print(t1.get_details())



'''
Created on 23-May-2018

@author: RAJESH
'''
