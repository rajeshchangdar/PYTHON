#Here is the application of Property method of Python
class Account(object):
    def __init__(self,rate):
        self.amt=0
        self.rate=rate

    @property
    def amount(self):
        return(self.amt)
    @property
    def inr(self):
        return(self.amt*self.rate)
    @amount.setter
    def amount(self,value):
        if(value<0):
            print("Enter Positive Number")
            return
        self.amt=value

if(__name__=='__main__'):
    
    acc1=Account(rate=61)
    acc1.amount=20
    
    print("Dollar Amount: ",acc1.amount)
    print("INR Value: ",acc1.inr)
    
    acc1.amount=-100

    print("Daller Amount: ",acc1.amount)

'''
Created on 23-May-2018

@author: RAJESH
'''
