# Here are some Python String Operations 

"""
#Check the String Operations
str1=input("Enter a String:")
#print(str1[0:3])
print(str1[0:5])
strlst=(str1.split(" "))
print(type(strlst))
strlst.reverse()
print(strlst)

strts="This Is Rajesh Changdar"
print(strts[::-1])

restr=" ".join(strlst)
print(restr)
print(restr[::-1]) # To reverse a String

"""
"""
#Palindrom Number Checking
while(1):
    str1=input("Enter a String: ")
    str2=str1[::-1]

    if(str1==str2):
        print("Yes!! Palindrom")
        break
    else:
        print("No!! Not a Palindrom")

"""
"""
#Count the Number of Words
strchk=input("Enter a String to count Words: ")
chklst=strchk.split(" ")
print("Total No of Words in the String: ",len(chklst))
wrd=input("Enter the word to check no of appearence in String: ")
count=0
for index in chklst:
    if(index==wrd):
        count+=1
    
print("The No of Appearences of %s in String is %d"%(wrd,count))

"""
#Iterating all characters in the String
strck=input("Enter a String: ")
for index in strck:
    print(index, end=' ')


        
'''
Created on 15-May-2018

@author: RAJESH
'''
