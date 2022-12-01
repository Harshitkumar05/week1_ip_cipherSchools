# chapter 1 Escape sequence
#Escape sequence(\)is used for write comma
'''print("hello \"world\" world")'''
#escape sequence(\n) is used for new line
'''print("line A\nline B")'''
#escape(\t) is used for given space
'''print("name\tHarshit")'''
# for print backlash given that double (\\)
'''print("this is backslash \\")'''
# exrecise 1
'''print("this is \\\\ double backslash")'''
'''print("this is /\\/\\/\\/\\ moutain")'''
'''print("he is \t awesome")'''
# raw string in python
'''print(r"this is \\ double backslash")'''
# if a function reapeat with n time
'''first_name= "harshit"
print(first_name*3)'''
# chapter 2 take input a user
 #user input 
'''name=input("what is your name")
age= input("what is your age")
print(name+age)'''
#input is in string
# int function 
'''number_one = int(input("enter a number"))
number_two = int(input("enter a second number"))
total =number_one+number_two
print("total is"+str(total))'''
# int change a number in integer
#str chane in string
#float is change in decimal
# exercise 2 by formating
'''num1 = input("enter 1st number")
num2= input("enter a second number")
num3= input("enter a third number")
print(f"Average of three number{(int(num1)+int(num2)+int(num3)/3)}")
'''
#exercise2 by string slicing
'''name=input("What is your name")
rev=name[-1::-1]
print(rev)'''
#center method
name = "Harshit"
#to print **Harshit**
'''print(name.center(11,"*"))'''
'''name=input("enter your name :")
print(name.center(len(name)+8, "*"))'''
#Exercisen  if else and or
'''name=input("what is your name")
age= int(input("what is your age"))
if age >= 10 and (name[0]=='a'or name[0]=='A'):
    print("you can watch the movie")
else:
    print("you cannot watch coco")'''
#While loop is used
'''i=1
while i<=10:
    print("hello world")
    i=i+1'''
# the sum of 1 to 10 number using while loop
'''total=0
i=1
while i<=10:
    total+=i
    i +=1
print(total)'''
# to take input sum of n number
'''n = input("enter a number:")
n = int(n)
total = 0
i=1
while i<=n:
    total+=i
    i+=1
print(total)'''
#ques for while loop1+2+3+4 input give by user
'''number = input("enter a number")
int(number[i])
total =0
i=0
while i < len(number):
    total += int(number[i])
    i += 1
print(total)'''
#for loop practise
'''for i in range(10):
    print("hello world")'''





