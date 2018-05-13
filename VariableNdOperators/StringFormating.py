#Introduction to String Formatting

#Tuple Packing and Unpacking
data=("Rajesh Changdar","1193923","TCS") # Tuple Packing
name,empid,company=data # Tuple Unpacking
print(name,empid,company)

#Python_v<3.6 String Formatting 
name="Rajesh Changdar"
roll="it1217"
college="CEM,Kolaghat"
msg="My name is {0} and my roll no is {1} of college {2}".format(name,roll,college)
print(msg)

#Python_v>3.6 String Formatting
name="Rajesh Changdar"
empid=1193923
company="TCS"
msg=f"This is {name} and empid is {empid} who works for {company}"
print(msg)

'''
Created on 07-May-2018

@author: RAJESH
'''
