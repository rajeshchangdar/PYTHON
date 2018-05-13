#Introduction to Variables
import sys
print("Hello!! Introduction to  Python Programming World")
print(sys.version_info)

#simple interest calculations
amount=float(input("Enter Amount: "))
intrate=float(input("Enter Interest rate: "))
period=int(input("Enter Time Period: "))

value=0
yr=1
while(yr<=period):
    value=amount+(amount*intrate)
    print("Year=%d and Amount=%f" %(yr,value))
    amount=value
    yr=yr+1

#Average of N numbers Problem
N=10;
summ=0
count=0
while(count<N):
    num=float(input(" "))
    summ=summ+num
    count+=1
print("Count=%d and Average=%f"%(count,(summ/10)))

#Fehrenheit to Celcius Temperature Conversion
fer=0.0
print("Ferenhite-----Celcius")
while(fer<250):
    cel=(fer-32.0)/1.8
    print("%.1f  %.2f"%(fer,cel))
    fer=fer+25

#Multiple Assignments in Python
a,b=12,14
print("a=%d and b=%d"%(a,b))
c,d=a,b
print("c=%d and d=%d"%(c,d))


'''
Created on 07-May-2018

@author: RAJESH
'''
