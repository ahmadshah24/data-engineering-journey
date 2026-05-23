# modules in python we have built in and extrnal modules we can create our own modules as well


# import mymodule

# mymodule.hello()
# print()

# scop we have local and global scops; with the help of global word we can make global var in local scop as well

# def sum(a,b):
#     c = a +b
#     # print(z) here if we do not have a local one will take the global one
#     # z = 99 # this will creat an local var
#     global z # this will make the z as global one 
#     z = 999

#     print(z)
#     return c

# z = 77 # this is a global
# print(sum(22,33))
# print(z)


#docstring is the very next line after the defination of the function

# def add(a,b):
#     '''this function will add 2 numbers'''
#     return a+b

# print(add.__doc__)
# print(add(44,55))



# def greet():
#     print("Hello, python learner")


# greet()

# def square(num):
#     return num**2

# print(square(4))

# def full_name(first_name,last_name):
#     return first_name+last_name


# print(full_name("sayed ","shah"))


# def calculate_area(lenght, width=10):
#     return lenght*width

# print(calculate_area(11,22))
# print(calculate_area(44))

# add = lambda a,b:a+b

# print(add(44,55))

# list_a = [1,2,3,4,5,6]

# square = lambda x:x*x
# print(list(map(square,list_a)))

# def factorail(n):
#     if n == 1:
#         return 1
#     return n * factorail(n-1)

# print(factorail(4))

# def sum_of_digits(n):
#     if n== 0:
#         return 0
#     return n%10 + sum_of_digits(n//10)

# print(sum_of_digits(33554))

# import math

# print(math.sqrt(144))
# print(math.sin(math.radians(90)))

# import requests

# a = requests.get("https://api.github.com")

# print(a.json())

# def safe_divide(a,b):
#     if b==0:
#         return "cannot divide by zero"
#     return a/b

# print(safe_divide(33,3))
# print(safe_divide(33,0))


# data structures in python we have list, tuples, sets and dicionanries

# lists

marks = [66,77,88,99,44]

mixed = [44,"shah",False, 4.3]

# print(marks[1])
# print(marks[1:5])
# for i in marks:
#     print(i)


# marks.append(656)
# marks.pop()
# marks.insert(3,454)
# # marks.extend(mixed)
# marks.
# print(marks)

# a = 5
# table = []

# for i in range(1,11):
#     table.append(5*i)

# print(table)

# table = [5*i for i in range(1,11)]
# print(table)

# squared = [i**2 for i in range(6)]
# print(squared)

# cube = [i*3 for i in range(5)]
# print(cube)


# tuples in python we cannot change the elements in tuple


# my_tuple = (1,2,3,4,4)# we cannot change the elements
# singal_element_tuple = (5, ) # we have to add commo at the end to make a singal element tuple


# tu = (22,33,44,55)
# a,b,c,d = tu
# print(a,b,c,d)
# print(tu.count(22))
# print(tu.index(22))

# sets in python ; unordered, unique collection of data

# fruits = {"apple","banana","cherry",""}
# print(fruits)
# fruits.add('watermelon')
# print(fruits)
# fruits.remove('apple') #if we want to remove the element which is not in the set will gives us error we have to use discard
# print(fruits)
# fruits.discard('apple')
# print(fruits)


#  set operations

# a = {1,2,4,4,5,6}
# b = {4,5,6,7,8,9}

# c = a.union(b)
# print(c)
# d = a.intersection(b)
# print(d)
# e=a.difference(b)
# print(e)


# dictionaries it key value pais and used for fast lookups

# student = {
#     'name': 'shah',
#     'age': 22,
#     'grade': 'A',
# }
# print(student['name'])
# student['name'] = 'jan shah'
# print(student['name'])

 
# print(student.keys())
# print(student.values())
# print(student.items())
# student.pop('age')

# lista = [i*2 for i in range(6)]
# print(lista)


# squares = {i: i**2 for i in range(10)}

# print(squares)


# keys = squares.keys()

# print(keys)

# fruits = ["apple","banana","cherry","watermelon"]

# fruits[0] = 'orange'
# print(fruits)
# print(fruits.__len__())
# print(len(fruits))

# nums = [1,2,3,4,5,6,7,8,9,10]
# print(nums[0:3])
# print(nums[-3:])

# sorted_nums = nums.sort()
# nums.append(12)
# print(nums)

# nums.remove(2)

# nums.insert(3,44)
# print(nums)


# coordinates = (10,20)
# print(coordinates[0])
# print(coordinates[1])

# lista = list(coordinates)

# lista.append(50)

# mytup = tuple(lista)

# print(mytup)

# my_set = {1,2,3,3,4}
# print(my_set)

# my_set.add(4)
# my_set.remove(2)
# print(my_set)

# set_a = {1,2,3,4}
# set_b = {3,4,5,6,7}

# print(set_a.union(set_b))
# print(set_a.intersection(set_b))
# print(set_a.difference(set_b))


# student = {
#     'name': 'shah',
#     'age': 22,
#     'grade': 'A',
# }

# print(student['name'])
# student['grade'] = 'A+'
# student['city']= 'kabul'

# print(student)


# friends_numbers ={
#     'shah':102020,
#     'jan': 303030,
#     'khan':445555,
# }

# keys =  friends_numbers.keys()
# values = friends_numbers.values()
# times = friends_numbers.items()

# for key,value in friends_numbers.items():
#     print(key,value)

# num_list = [1,2,3,4,5,5,4,3,2,11,22,44]

# num_set = set(num_list)
# print(num_list)
# print(num_set)


# products = {
#     'pen':30,
#     'ball':40,
#     'book':50,
# }
# max_price =None

# for i in products.values():
#     if max_price is None or i > max_price:
#         max_price = i


# print(max_price)


# dict_1 = {
#     'a':1,
#     'b':2,
#     'c':3,
# }
# dict_2 = {
#     'd':4,
#     'e':5,
#     'f':6,
# }

# merged = dict_1 | dict_2

# print(merged)



# Object oriented programming (OOP)





