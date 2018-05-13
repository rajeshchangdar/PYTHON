#Introduction to Tuple using Python
tuple1='Atos','TCS','CTS','Infosys','IBM','Accenture','MuSigma'

print(tuple1)
for index in tuple1:
    print(index,end=' ')

print("\n",divmod(5,2))
x,y=divmod(5, 2)
print(y)

print("-------Tuples are Immutable-------")
tuple2=(1,2,3,4,5,6)
print(tuple2)
#del tuple2[1]

test1=(233)
print(type(test1))
test2=(233,344)     # Always need to check the trailing comma in the tuple
print(type(test2))
print(type(len))

'''
Created on 11-May-2018

@author: RAJESH
'''
