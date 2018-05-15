#Introduction to different Python String Methods
"""
str1="raJeSh ChAngdar"
print(str1.title())  # To Print  the title cased version of the string
print(str1.upper())  # To print the Uppercase version of the String
print(str1.lower())

print(str1.swapcase())# to swap the letters in the String

str2="Rajesh1193923Changdar"
print(str2.isalnum())
print(str2.isalpha())

str3="1234"
print(str3.isdigit())
str4="Rajesh Changdar"
print(str4.islower())
print(str4.isupper())
print(str4.istitle())
"""
#split() method to split the string
str5="he is a good boy"
print(str5.split(" "))
str6="He:Is:Not:a:Bad:Girl"
print(str6.split(":"))

#join() is used to join the sub parts of the String
str7="Rajesh works in TCS Kolkata"
print(".".join(str7.split(" ")))

#String Stripping in Python
str8="This is in TCS\n"
print(str8.strip())

str9="www.tcs.com"
print(str9.lstrip("wtcs."))
print(str9.rstrip("comts."))

#Text Finding in python String
str10="Partho Pan works in TCS R&D Lab in Chennai"

if(str10.find("TCS")>-1):
    print("Found at Position: ",str10.find("TCS"))
else:
    print("Sorry!!! Not Found")


print(str10.startswith("Pa"))
print(str10.endswith("Ai"))














'''
Created on 15-May-2018

@author: RAJESH
'''
