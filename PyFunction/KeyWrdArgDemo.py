# Introduction to Keyword Argument and Keyword only Argument Demonstration in Python

#Keyword Argument
print("------Keyword Argument------")
def method1(num1,num2=100,num3=200):
    print("a is %d - b is %d - c is %d"%(num1,num2,num3))

method1(111)
method1(111,222)
method1(111, 222, 333)
method1(5555, num3=7777)
method1(num3=3333,num1=1111,num2=2222)

# method1(111, num2=222, num3) # This method calling is not valid
# No non default value can follow the default value

print("------Keyword Only Argument------")
def method2(numk,*,num1=0,num2=0,num3=0): #After * all the next arguments are treated as the default argument
    print("numk is %d - a is %d - b is %d - c is %d"%(numk,num1,num2,num3))

method2(200, num1=111, num2=222, num3=333)
#method2(200,111, num2=222, num3=333) # Throws error

'''
Created on 21-May-2018

@author: RAJESH
'''