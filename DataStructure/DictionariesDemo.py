#Introduction to the Python Dictionary

"""
dict1={'Rajesh':'IT','Gopal':'ME','Samya':'ECE','Soumik':'CSE'}
print(dict1)
print(dict1['Samya'])

dict1['Partho']='EIE'
print(dict1)

del dict1['Gopal']
print(dict1)

print('Repeat' in dict1)
print('Rajesh' in dict1)

"""
#dict() function to create dictionary from tuple of key:value pair

dict2=dict((('India','Delhi'),('Australia','Sydney'),('Russia','Moskow')))
print(dict2)

#items() method used to loop through the dictionary
for x,y in dict2.items():
    print("%s's capital city is: %s "%(x,y))

#setdefault() method is used to add more data to a value in a dictionary 
dict3={}
dict3.setdefault('name', []).append('Java')
dict3.setdefault('name', []).append('Python')
dict3.setdefault('name',[]).append('C')
print(dict3)

#dict.get(key,value) method is used to get the default value when the key doesn't exist before
#print(dict2['invalid'])
print(dict2.get('invalid','Hello'))

#enumarate() used to loop through a list
list1=['BJP','RSS','VHP','Bajrang Dal','Shiv Sena']
for i,j in enumerate(list1):
    print("%d-----%s"%(i,j))

#zip() method used to iterate through two sequence same time
list1=["Rajesh","Santanu","Esha"]
list2=["TCS","Infosys","IBM"]

for x,y in zip(list1,list2):
    print("%s----%s"%(x,y))

'''
Created on 13-May-2018

@author: RAJESH
'''
