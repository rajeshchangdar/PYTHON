#Gross Salary Calculations
basic_sal=1500
bonus_amount=200
comm_rate=0.02

nos=int(input("Enter the No of Cameras: "))
price=float(input("Enter the total Price: "))

bonus=(nos*bonus_amount)
commision=(comm_rate*nos*price)

gross=basic_sal+bonus+commision

print("Monthly Gross Salary: ",gross)

'''
Created on 09-May-2018

@author: RAJESH
'''
