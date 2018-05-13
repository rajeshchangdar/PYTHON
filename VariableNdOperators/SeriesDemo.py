x=int(input("Enter the value of X: "))
N=int(input("Enter the no of Terms: "))
val=0.0
for index in range(1,N+1):
    val=val+(1/index)
    print("%2d---%.2f"%(index,val))



'''
Created on 09-May-2018

@author: RAJESH

'''
