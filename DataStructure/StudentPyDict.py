num=int(input("Enter the Number of Students: "))
subject=['Mathematics','Statistics','Computer Science']
dict1={}

for i in range(0,num):
    name=(input("Enter the name of the Student %d: "%(i+1)))
    marks=[]
    for i in subject:
        marks.append(int(input("Enter marks for subject [ %s ]: "%(i))))
    dict1[name]=marks

for x,y in dict1.items():
    total=sum(y)
    print("Total sum for %s is %d "%(x,total))
    if(total>120):
        print("%s has passed the Exam"%x)
    else:
        print("%s has failed the Exam"%x)   
    
    


'''
Created on 14-May-2018

@author: RAJESH
'''
