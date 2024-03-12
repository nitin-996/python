# access modifiers


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


#####################################################################

# inheritance 
# types single , multilevel and multi inheritance


class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        print(f"{self.year} {self.make} {self.model}")

class Car(Vehicle):
    def __init__(self, make, model, year, num_doors):
        super().__init__(make, model, year)
        self.num_doors = num_doors

    def display_info(self):  # Overriding display_info method of the base class
        print(f"{self.year} {self.make} {self.model} - {self.num_doors} doors")

# Creating instances of the classes
vehicle1 = Vehicle("Toyota", "Camry", 2022)
car1 = Car("Honda", "Accord", 2023, 4)

# Calling methods
print("Vehicle Information:")
vehicle1.display_info()

print("\nCar Information:")
car1.display_info()


#################################################################################################




class Student:
    def set_name(self,name):
        self.name= name  # class attribute

    def get_name(self):
        return self.name
    


Student1 = Student()     

Student1.age = 24  # instance/object attribute
Student1.set_name("ronak")
tic=Student1.get_name()


print(Student1.age)
print(tic)


