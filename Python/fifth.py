
'''
decorators are a powerful feature in Python that allow you to modify the behavior of a function or class. They are often used to add functionality to existing code without changing its structure. In this example, we will create a simple decorator that adds print statements before and after the execution of a function.
it takes function, it creats a new function and returns it. the new function will call the original function and add some functionality before and after it.

'''
# def decorator(func):
#     def wrapper():
#         print("Before the function is called.")
#         func()
#         print("After the function is called.")
#     return wrapper




# @decorator
# def say_hello():
#     print("Hello, World!")


# # this is print statement which will call the function say_hello, but if we want to have other statements before and after the we need decorators


# say_hello()

# f = decorator(say_hello)

# f()
#  instead of do the above we can use the @decorator syntax to apply the decorator to the function directly



# decortor with arguments

# def repeat(n):
#     def decorator(func):
#         def wrapper():
#             for a in range(n):
#                 func(a)
#         return wrapper
#     return decorator

# @repeat(5)
# def say_hello(a):
#     print(f"Hello, World! {a}")


# say_hello()


# def uppercase_decorator(func):
#     def wrapper():
#         result = func()
#         return result.upper()
#     return wrapper

# def exclaim_decorator(func):
#     def wrapper():
#         # result = func()
#         return func() + "!"
#     return wrapper

# @uppercase_decorator
# @exclaim_decorator
# def greet():
#     return "Hello, World"

# print(greet())


# getters and setters



 

# class Student:

#     def __init__(self, name):
#         self._name = name


#     # Getter
#     @property
#     def name(self):
#         return self._name


#     # Setter
#     @name.setter
#     def name(self, value):

#         if len(value) < 3:
#             print("Name is too short")
#         else:
#             self._name = value


# s1 = Student("Ahmad")

# print(s1.name)   # Getter
# s1.name = "khan jan shah"

# print(s1.name)  # Getter
# s1.name = "Ali"  # Setter

# print(s1.name)

