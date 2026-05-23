# # OOP in python

# '''
# class is the blueprint
# object is the instance of that class

# '''

# class Employee:
#     company = "Anord"  # this is class attribute
    
#     def __init__(self, name, salary,bond, company): # company here is instance attribute if we have this will be first all the time if not the the class attribute will be first
            
#             self.salary = salary
#             self.name = name
#             self.bond = bond
#             self.company = company

#     def _empployee_info(self):
#          print(f'employee name is {self.name} and the salary is {self.salary} and the bond is {self.bond}')

#     # salary = 0
#     # def set_salary(self,s):
#     #     self.salary = s
#     #     return s
#     def get_salary(self):
#         return self.salary
    


# # e1 = Employee() # this is without constructor

# e1 = Employee('shah',3220000,4,'tasla')
# # e1.set_salary(3333)
# print(e1.get_salary())
# print(e1.company)
# e1._empployee_info()
# # e2 = Employee() this is without constructor
# e2 = Employee('khan',3440000,2,'honda') # this is with constructor
# # e2.set_salary(444444)
# print(e2.get_salary())
# print(e2.company)
# e2._empployee_info()


# print(Employee.company) # if we want to run the class attribute we can do it like this 

# # object intorspection : this help us to find all the attributes and methods of a class or instance

# print(dir(e1))

    

# inheritance in python
'''
it is like family tree child class inherits traits (attributes and methods) from it parent class. help to prevent from rewriting the code
'''


# class Animal:
#     laction = 'Afghanistan'

#     def __init__(self,name):
#         self.name = name

#     def sound(self):
#         print('this is genric sound for animals')



# class Dog(Animal):
    
#     def sound(self):
#         print('Woof!!!! this is dog')

        
# class Cat(Animal):
    
#     def sound(self):
#         super().sound() # this is supper which help us to class parent method inside the child method
#         print('Meow!!!! this is cat')

        

# a1 = Animal('this is animal')
# print(a1.laction)
# print(a1.name)
# a1.sound()

# d1 = Dog('this is dog')
# print(d1.name)
# print(d1.laction)

# d1.sound()

# c1 = Cat('this is cat')
# print(c1.name)
# print(c1.laction)
# c1.sound()



# class Car:
    
#     def drive(self):
#         print('car is moving')



# car1 = Car()
# car1.drive()


# class Person:
    
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age


# person_1 = Person('shah',33)

# print(person_1.name)
# print(person_1.age)
# # we can have multi leavl of inheritance






