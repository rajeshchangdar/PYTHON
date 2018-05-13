#Introduction to Python List Data Structure
"""
list1=[11,-23,44,67,1123445,-9889,2000,44]
print(list1)
list1.append(3000)
print(list1)
list1.insert(1,2333)
print(list1)
print(list1.count(67))
print(list1.count(44))
list1.remove(-9889)
print(list1)
list1.reverse()
print(list1)

list2=[111,222,333,444,555]
list1.append(list2)
print(list1)
list1.extend(list2)
print(list1)
print(list1[-1])
list1.remove(list2)
list1.sort()
print(list1)
del(list1[-1])
print(list1)

"""
"""
#Stack Implementation using List
list1=[11,22,33,44,55,66]
print(list1)
list1.pop() #STACK POP 
print(list1)
list1.pop()
print(list1)
list1.append(55) #STACK PUSH
print(list1)

"""
"""
#Queue Implementation using List
list1=[11,22,33,44,55,66]
print(list1)
list1.pop(0)
print(list1)
list1.pop(0) 
print(list1)
list1.append(77)
print(list1)
"""
#List Comprehensions

list1=[1,2,3,4,5]
print([index**2 for index in list1])
print([index+1 for index in [index**2 for index in list1]])

'''
Created on 11-May-2018

@author: RAJESH
'''
