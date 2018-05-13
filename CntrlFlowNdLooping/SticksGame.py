sticks=21

while True:
    print("Stricks Left: ",sticks)
    
    sticks_taken=int(input("Take Sticks(1-4): "))
    if sticks==1:
        print("You took the last stick..you lose")
        break
    if((sticks_taken>=5)or(sticks_taken<=0)):
        print("Wrong Choice!!!..Try Again")
        continue
    print("Computer Took: ",(5-sticks_taken),"\n")
    sticks-=5
    
    
'''
Created on 10-May-2018

@author: RAJESH
'''
