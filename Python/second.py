'''
# Arithmetic Operator 
a = 10
b = 20
print("a + b = ", a + b)
print("a - b = ", a - b)
print("a * b = ", a * b)
print("a / b = ", a / b)
print("a % b = ", a % b)
print("a // b = ", a // b)
print("a ** b = ", a ** b)
a = 34

b = 2

# Conditional Operators 
print(a>4)
print(a<4)
print(a<=4)
print(a>=4)
print(a==4) # Is a equal to 4?
print(a==34) # Is a equal to 34?
print(a!=34) # Is a not equal to 34?

c = True 
d = False

# Logical Operators
print(True and True)
print(True and False)
print(False and True)
print(False and False)

print("For Or Operator...")
print(True or True)
print(True or False)
print(False or True)
print(False or False)

print("Not Operator")
print(not(True) ) 
print(not(False) ) 

a = 32
print(a)
a*=3 #a=  a * 3
print(a)

print("-------------------------------------------------")
print("Hello, world! welcome to python")
print("Twinkel, twinkel, lettle start,\nHow I wonder what you are!")
name = "sayed"
age = 25
height = 1.70
is_student = True

print("my name is"+name+"i am"+str(age)+"with height of"+str(height)+"and am istudent?"+ str(is_student) )

num = "45"
num = int(num)+10

print(num)

food = input("Enter you favorite food ")
print("wow! I also like "+food)
'''

# num_1 = int(input("Enter num 1 "))
# num_2 = int(input("Enter num 2 "))
# print("sum ", num_1 + num_2)
# print("difference ", num_1 - num_2)
# print("product ", num_1 * num_2)
# print("quotient ", num_1 / num_2)

# print("Harry said, \"Python is awesome!\"\n this is a new line. \n this is a tab ->\t <- here")


# num_1 = int(input("Enter num 1 "))
# num_2 = int(input("Enter num 2 "))
# print("square", num_1**2)
# print("cube", num_1**3)



# age = int(input("enter your age"))

# if (age > 18):
#     print("you can drive")
# else:
#     print("you cannot drive")

# print("end of program")




# age = int(input("enter your age"))

# if (age > 18):
#     print("you can drive")
# elif(age == 18):
#     print("you are 18 years old wait one more year")
# else:
#     print("you cannot drive")

# print("end of program")

# num = int(input("enter a number between 10 and 0"))

# match num:
#     case 3:
#         print("you won a car")
#     case 5:
#         print("you won a house")
#     case _:
#         print("go out")

#for loop

# for i in range(1,10):
#     print(i, end="")

# j = int(input("enter a number which you want to see the times table of it"))
# for i in range(1,11):
#     print(i, "X",j, "=", j*i )

# while loop

# i = 1
# while i<=10:
#     print("*")
#     i +=1

# for i in range(1,21):
#     if i%2 != 0:
#         print(i)
#         # continue
# for i in range(1,21):
#     print(i)
#     if i == 10:
#         break
# for i in range(1,21):
#     if i == 10:
#         continue
#     print(i)


# for i in range(1,20):
#     pass

 
# num = int(input("enter a number to check it \n"))

# if num >0:
#     print(num,"is positive")
# elif num < 0:
#     print(num, "is negative")
# else:
#     print(num, "is zero")




# age = int(input("enter you age"))

# if age >18:
#     print("you can vote")
# else:
#     print("you can not vote")




# num = int(input("enter a number to check it is even or odd"))

# if num%2==0:
#     print(num, "is even")
# else:
#     print(num, "is odd")

# week_day = int(input("enter an number to show the day of the week"))

# match week_day:
#     case 1:
#         print("today is saturday")
    
#     case 2:
#         print("today is sunday")
    
#     case 3:
#         print("today is monday")
    
#     case 4:
#         print("today is thuseday")
    
#     case 5:
#         print("today is wendsday")
    
#     case 6:
#         print("today is thrusday")
    
#     case 7:
#         print("today is friday")
    

# num_1 = int(input("enter num 1"))
# num_2 = int(input("enter num 2"))
# opt = input("enter the opteation you want to preform")
# match opt:

#     case "+":
#         print("sum", num_2+num_2)
#     case "-":
#         print("sub", num_2-num_2)
#     case "+":
#         print("mul", num_2*num_2)
#     case "+":
#         print("div", num_2/num_2)

# for i in range(1,11):
#     print(i)

# num = int(input("enter a number to see the times table for it"))

# for i in range(1,11):
#     print(i,"X", num , " = ", i*num)

# sum_i = 0

# for i in range(1,101):
#     sum_i +=i
    

# print(sum_i)    

# for i in range(1,5):
#     print("*"*i)

# num = 1
# while num <=10:
#     print(num)
#     num+=1


# password = "shah"
# user_password = input("enter your password")

# while user_password != password:
#     user_password=input("wrong password try again")


# print("sucess your login")



# num = 12345

# print(int(str(num)[::-1]))

# for i in range(1,11):
#     print(i)
#     if i ==7:
#         break

# for i in range(1,11):
#     if i == 5:
#         continue
#     print(i)


# for i in range(1,11):
#     print(i)
#     if i ==3:
#         pass


# strings in python


# name1 = "sayed"
# name2 = 'sayed'
# name3 = '''sayed
# is a
# boy'''

# print(name1)
# print(name2)
# print(name3)

# name = "sayed ahmad shah"
# print(name[0])
# print(name[4])
# print(name[:3])
# print(name[::-1]) #this revers the string
# print(name[-1])# this will start form the end 

# print(name[1:10:1])# this will skip one charatar
# print(name[1:10:3])# this will skip 2 charatar

# print(name[:5]) # this is the same as name[0:5]
# print(name[5:]) # this is the same as name[5:end of string]


#strings are immutalbe means not changable so we cannot change the acutle string 


# name = "  sayed  "
# name_len = len(name)
# print(name_len)
# print(name.upper(), name)
# print(name.lower())
# print(name.title())
# print(name.capitalize())


# print(name.strip()) # remove the space for start and end
# print(name.lstrip())
# print(name.rstrip())

# txt = "this is a ball"

# print(txt.find("is"))
# print(txt.find("a"))
# print(txt.replace("is", "are"), txt)


# txt = "apple, banana, orange"

# print(txt)
# fruits = txt.split(",") # will craet a list and will split with ,
# print(fruits)

# new_fruits = " - ".join(fruits)
# print(new_fruits)
# txt = "sayed"
# print(txt.isalpha()) #will check that the text is all alphabit or not
# print(txt.isdigit()) #will check that the text is all digits or not
# print(txt.isalnum()) # this will check is the text is combantion of both
# print(txt.isspace())#will check is there any space in the text


#fstring is using for formating the text in python

# template = "Dear {}, I am cool to have you with {}"

# name_1 = "sayed"
# name_with = "shah"


# new_name = template.format(name_1, name_with) 
# print(new_name)

# user_name = input("enter your user name")
# password = input("enter you password")

# print(f"your name is {user_name} and your password is {password}")


#both of these are using in encoding  and can gives us ASCII vaule 

# print(ord('B')) 
# print(chr(65))


name = "sayed ahmad shah sekandary"

# print(name[0])
# print(name[-1])
# print(len(name))

# hello = "Hello"
# world = "world"

# print(hello + " " + world)



# txt = "Python progtramming"

# print(txt[:6])
# print(txt[-6:])
# print(txt[::2])
# print(txt[::-1])


# txt = " I love python progamming "

# print(txt.strip())
# print(txt.title())
# print(txt.count('o'))
# print(txt.isalnum())


# name = 'sayed'
# age = 22

# print(f"my name is {name} and i am {age} years old")





# sentence = 'coding in python is fun'

# print(sentence.replace("fun","awesom"))


# print(sentence.index('python'))

# print(sentence.upper())


# sentence = 'coding in python is fun'
# vowels = [ 'a','i','o','e','u']
# sum_v = 0
# for i in sentence.lower():
#     if (i in vowels):
#         sum_v+=1


# print(sum_v)


# word = input("enter a word \n")

# word_reverse = word[::-1]
# # print(word)
# # print(word_reverse)

# if word == word_reverse:
#     print(f"{word} is palindrome with {word_reverse}")


# this is without return will not have anything for this function to assign it to any other variables and with gives you none


# def average(a,b,c):
#     avg = (a+b+c)/3
#     print(f"the average of {a}, {b}, {c} is {avg}")

# average(22,33,44)
# first_avg = average(55,66,88)

# print(first_avg)
# #this is with return

# def average_return(a,b,c): # a,b,c are parameters
#     avg = (a+b+c)/3
#     return(f"the average of {a}, {b}, {c} is {avg}")



# print(average_return(55,66,77)) # we have to print the funcation which returns a vaule but we have a vault that fromt he funcation


# second_avg = average_return(66,88,99) # numbers are artribute


# print(second_avg)




#lambda functions these are anonumous inline founctions


# add = lambda a,b:a+b

# print(add(55,4))




# recursion
# it happens when a function call it slefs to solve a problem


# def fib(n):
#     if (n==0 or n==1):
#         return n
#     return fib(n-2)+fib(n-1)


# print(fib(9))


# def factorail (n):
#     if n==1:
#         return 1
    
#     return n*factorail(n-1)

# print(factorail(4))






