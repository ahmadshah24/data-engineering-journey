# from sys import exception


# class Employee:
#     company = "ABC Corporation"  # class attribute

#     def __init__(self, name, age, position):
#         self.name = name
#         self.age = age
#         self.position = position
# #  this is the instance method
#     def display_info(self):
#         print(f"Name: {self.name}, Age: {self.age}, Position: {self.position}")

# if we do not need or want to have self in the method we can use static method 

#     @staticmethod
#     def company_info():
#         print(f"Company: {Employee.company}")

#     @classmethod
#     def change_company(cls, new_company):
#         cls.company = new_company   



# emp_1 = Employee("John Doe", 30, "Software Engineer")
# emp_1.display_info()  # Output: Name: John Doe, Age: 30
# Employee.company_info()  # Output: Company: ABC Corporation
# emp_1.change_company("XYZ Corporation") 
# Employee.company_info()  # Output: Company: XYZ Corporation



#  dunder methods are special methods in python which have double underscores before and after the method name. they are also called magic methods or special methods. they are used to define the behavior of objects for built-in operations. for example, when we use the + operator on two objects, python will call the __add__ method of the first object and pass the second object as an argument. we can override these methods in our classes to customize their behavior.



# class Number:

#     def __init__(self, value):
#         self.value = value

#     def __add__(self, other):
#         return self.value + other.value


# n1 = Number(5)
# n2 = Number(10)

# print(n1 + n2)



# exceptions in python are errors that occur during the execution of a program. they can be handled using try-except blocks. we can also raise exceptions using the raise statement. we can create our own custom exceptions by creating a new class that inherits from the built-in Exception class.
# 
#
#  


# while True:
#     # without try and except block the program will terminate if we enter a string instead of an integer. but with try and except block the program will continue to run and ask for input again.
#     try:
#         num_1 = int(input("Enter a number : "))
#         num_2 = int(input("Enter a number : "))
#         print(f"the sum of {num_1} and {num_2} is {num_1 + num_2}")
#     except ValueError:
#         print("Please enter a valid integer.")
#     except ZeroDivisionError:
#         print("Division by zero is not allowed.")
#     except KeyboardInterrupt:
#         print("\nProgram interrupted by user.")
#         break
#     except Exception as e:
#          print("Please enter a valid integer.", e)
#     # except:
#     #     print("Please enter a valid integer.")


# num_1 = int(input("Enter a number : "))
# num_2 = int(input("Enter a number : "))

# if num_2 == 0:
#     raise ZeroDivisionError("Division by zero is not allowed.") # this is how we can raise an exception in python. we can also create our own custom exceptions by creating a new class that inherits from the built-in Exception class.

# print(f"the sum of {num_1} and {num_2} is {num_1 / num_2}")


# try:
#     # num = 5555/0 # except will be executed
#     num = 5555/55 # else except will be executed
# except ZeroDivisionError as e:
#     print(f"Error: {e}")
# else:
#     print("No error occurred.") # will be executed if no exception occurs in the try block.
# finally:
#     print("This block will always execute.") # will be executed whether an exception occurs or not. it is used to clean up resources or perform any necessary finalization tasks.

# map, filter and reduce.

# map is a built-in function in python that takes a function and an iterable as arguments and returns a map object (an iterator) that applies the function to every item of the iterable. we can convert the map object to a list or tuple using the list() or tuple() functions.
# filter is a built-in function in python that takes a function and an iterable as arguments and returns a filter object (an iterator) that contains only the items of the iterable for which the function returns True. we can convert the filter object to a list or tuple using the list() or tuple() functions.

# reduce is a function in the functools module that takes a function and an iterable as arguments and returns a single value that is the result of applying the function cumulatively to the items of the iterable, from left to right. we can import the reduce function from the functools module using the following statement: from functools import reduce.

# numbers = [1, 2, 3, 4, 5]

# def square(x):
#     return x ** 2

# new_numbers = map(square, numbers) # this will return a map object which is an iterator. we can convert it to a list or tuple using the list() or tuple() functions.

# print(new_numbers) # this will print the map object. we can convert it to a list or tuple using the list() or tuple() functions.
# print(list(new_numbers)) # this will print the list of squared numbers. we can also use the tuple() function to convert it to a tuple.

# def is_even(x):
#     return x % 2 == 0

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# new_numbers = filter(is_even, numbers) # this will return a filter object which is an iterator. we can convert it to a list or tuple using the list() or tuple() functions.

# print(new_numbers) # this will print the filter object. we can convert it to a list or tuple using the list() or tuple() functions.
# print(list(new_numbers)) # this will print the list of even numbers. we can also use the tuple() function to convert it to a tuple.

# from functools import reduce

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# def multiply(x, y):
#     return x * y

# result = reduce(multiply, numbers) # this will return a single value that is the result of applying the function cumulatively to the items of the iterable.
# print(result) # this will print the result.


# walrus operator (:=) is a new operator introduced in python 3.8 that allows us to assign a value to a variable as part of an expression. it is also called the assignment expression operator. it is useful when we want to use a value in an expression and also assign it to a variable at the same time.



# while (data:= input("Enter some data (or 'q' to quit): ")):
#     print(f"You entered: {data}")
#     if data == 'q':
#         break



# args and kargs are used to pass a variable number of arguments to a function. args is used to pass a variable number of non-keyword arguments to a function, while kwargs is used to pass a variable number of keyword arguments to a function. args is represented by an asterisk (*) before the parameter name, while kwargs is represented by two asterisks (**) before the parameter name.
# args will retun tuple

# def sum(*args):
#     total = 0
#     for num in args:
#         total += num
#     return total

# sum(1, 2, 3, 4, 5) # this will return 15. we can pass any number of arguments to the function.
# #  kargs will return dictionary wil key value pairs

# def marks(**kwargs):
#     for item in kwargs:
#         print(f"the marks of {item}: is  {kwargs[item]}")
#         print(item)
#         print(kwargs[item])
#         for i in kwargs.keys():
#             total = 0
#             total += kwargs[i]
# marks(ali=90, ahmed=80, shah=70) # this will return the marks of ali, ahmed and shah. we can pass any number of keyword arguments to the function.)

# def combined_args_kargs(*args, **kwargs):  # args should come before kwargs in the function definition. if we put kwargs before args we will get a syntax error.
#     print("args:", args)
#     print("kwargs:", kwargs)




# def looger_decorator(func):
#     print("Before the function is called.")
#     return func()

# @looger_decorator
# def say_hello():
#     print("Hello, World!")


# # hello = say_hello()

# # print(say_hello)

# from time import time

# def timer_decorator(func):
#     import time
#     def wrapper():
#         start_time = time.time()
#         func()
#         end_time = time.time()
#         print(f"Execution time: {end_time - start_time} seconds")
#     return wrapper


# @timer_decorator
# def long_running_function():
#     sum = 0
#     for i in range(1000000):
#         sum += i



# a = long_running_function()
# # print(a)




# class Employee:
#     @property
#     def salary(self):
#         return self._salary
#     @salary.setter
#     def salary(self, value):
#         if value < 0:
#             raise ValueError("Salary cannot be negative.")
#         self._salary = value

    




# e1 = Employee()
# e1.salary = 50000
# print(e1.salary)


# class MathUtils:
#     @staticmethod
#     def add(a, b):
#         return a + b
#     @classmethod
#     def decripation(cls):
#         return "This class contains utility methods for mathematical operations."
    

# print(MathUtils.add(22,33))
# print(MathUtils.decripation())


# class Book:
#     tile = "Python Programming"  # class attribute
#     author = "John Doe"  # class attribute

#     def __str__(self):
#         print(f"Title: {self.tile}")
#     def __len__(self):
#         print(len(self.tile))    

# b1 = Book()
# b1.__str__()
# b1.__len__()

# class NegativeNumberError(Exception):
#     pass

# num = int(input("Enter a number: "))
# try:
#     print(f"the number is {num}")
# except ValueError:
#     print("Please enter a valid integer.")
# except ZeroDivisionError:
#     print("Division by zero is not allowed.")
# except NegativeNumberError:
#     if num < 0:
#         raise NegativeNumberError("Negative numbers are not allowed.")


# list_1 = [1, 2, 3, 4, 5]
# list_cubes = list(map(lambda x: x**3, list_1))  # using map and lambda function to get the cubes of the numbers in the list
# print(list_cubes)  # Output: [1, 8, 27, 64, 125]

# list_2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# def is_even(x):
#     return x % 2 == 0

# list_even = list(filter(is_even, list_2))  # using filter and function to get the even numbers in the list
# print(list_even)  # Output: [2, 4, 6, 8

# from functools import reduce

# list_3 = [1, 2, 3, 4, 5]
# list_sum = reduce(lambda x, y: x * y, list_3)  # using reduce and lambda function to get the sum of the numbers in the list
# print(list_sum)  # Output: 120  



# while txt := input("Enter a number (or 'q' to quit): "):
#     if txt.lower() == 'q':
#         break


# words = ["hello", "world", "python", "programming"]
# # lengths = [len(word) for word in words]  # using list comprehension to get the lengths of the words in the list
# lengths = [n for w in words if (n := len(w)) >= 4]
# print(lengths)  # using list comprehension to get the lengths of the words in the list



def sum_all(*args):
    return sum(args)


print(sum_all(1, 2, 3, 4, 5))  # Output: 15

def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")        


print_info(name="Alice", age=30, city="New York")

