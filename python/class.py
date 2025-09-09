# # access modifiers


class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def display_info(self):
        return f"{self.brand} {self.model}, {self.year}"

# Create an object from the Car class
my_car = Car("Toyota", "Corolla", 2020)

# Display the car's information
print(my_car.display_info())


# #####################################################################

# # inheritance
# # types single , multilevel and multi inheritance


# class Vehicle:
#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year

#     def display_info(self):
#         print(f"{self.year} {self.make} {self.model}")

# class Car(Vehicle):
#     def __init__(self, make, model, year, num_doors):
#         super().__init__(make, model, year)
#         self.num_doors = num_doors

#     def display_info(self):  # Overriding display_info method of the base class
#         print(f"{self.year} {self.make} {self.model} - {self.num_doors} doors")

# # Creating instances of the classes
# vehicle1 = Vehicle("Toyota", "Camry", 2022)
# car1 = Car("Honda", "Accord", 2023, 4)

# # Calling methods
# print("Vehicle Information:")
# vehicle1.display_info()

# print("\nCar Information:")
# car1.display_info()


# #################################################################################################


# class Student:
#     def set_name(self,name):
#         self.name= name  # class attribute

#     def get_name(self):
#         return self.name


# Student1 = Student()

# Student1.age = 24  # instance/object attribute
# Student1.set_name("ronak")
# tic=Student1.get_name()


# print(Student1.age)
# print(tic)


############################################################################


class Car:

    def __init__(self, model, year, color):
        self.chal = model
        self.saal = year
        self.rang = color

    def new_feat(self, tires):
        self.tire = tires


car1 = Car("toyota", 2020, "blue")


car1.new_feat("alloy wheels")
print(car1.tire)


# chaining ###########################3

class Calculator:
    def __init__(self, value=0):
        self.result = value

    def add(self, num):
        self.result += num
        return self  # Return self to allow chaining

    def subtract(self, num):
        self.result -= num
        return self  # Return self to allow chaining

    def multiply(self, num):
        self.result *= num
        return self  # Return self to allow chaining

    def divide(self, num):
        if num != 0:
            self.result /= num
        else:
            print("Error: Cannot divide by zero.")
        return self  # Return self to allow chaining


# Create an instance of the Calculator class
calc = Calculator()

# Perform method chaining to perform multiple operations
result = calc.add(5)\
             .multiply(2)\
             .subtract(3)\
             .divide(2)\
             .result

# Display the final result
print("Result:", result)


# 3


# super function = it is used to give access to the methods of a parent class.
#                    returns a temporary object of a parent class when used.


class Rectangle:

    def __init__(self, lenght, width):
        self.lenght = lenght
        self.width = width


class Square(Rectangle):

    def __init__(self, lenght, width):
        super().__init__(lenght, width)

    def area(self):
        return self.lenght*self.width


class Cube(Rectangle):

    def __init__(self, lenght, width, height) -> None:
        super().__init__(lenght, width)
        self.height = height

    def area(self):
        return self.lenght*self.width * self.height


cub = Cube(5, 5, 5)

print(cub.area())


# abstract class

# prevents a user from creating an object of that class
# comples a user  to override abstract methods in a child class

#  anstract class = a class which contains one or more abstract methods.
# abstract method =  a method that has a declaration but does not have an implementation.


# object argument

class Car:

    color = None


def change(car, color):

    car.color = color


car_1 = Car()


change(car_1, "blue")
print(car_1.color)


# duck typing concept = concept where the class of an object is less important than the method/attributes.
# class type is not checked if minimum methods/attributes are present
# https://www.geeksforgeeks.org/duck-typing-in-python/


class Duck:
    def walk(self):
        print("This duck is walking")

    def talk(self):
        print("This duck is quacking")


class Chicken:
    def walk(self):
        print("This chicken is walking")

    def talk(self):
        print("This chicken is clucking")


class Person:
    def catch(self, animal):
        animal.walk()
        animal.talk()
        print("You caught the critter")


duck = Duck()
chicken = Chicken()
person = Person()

person.catch(chicken)  # Passing an instance of the Chicken class


# walrus operatoe :=

# new to python 3.8
# assignment expression aka walrus operator
# assigns values to variables as part of a larger expression

print(happy := True)

foods = list()
while food := input("what food do you like") != "quit":
    foods.append(food)
