import random
import string

str1= string.ascii_letters + string.digits
str2=""


s=int(input("Enter the no. of char for creating a password:"))
if s>9:
    print("please give no. below 9 ")
else:
    for i in range(0,s):
      str2= str2 + random.choice(str1)

print(str2)








