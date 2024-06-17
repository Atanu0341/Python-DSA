# Problem (Class and Object) : Create a Car class with attributes like brand and model. Then create an instance of this class
# Problem (Class Method and Self) : Add a method to the Car class that displays the full name of the car (brand and model)
# Problem (Inheritance) : Create an ElectricCar class that inherits from the Car class and has an additional attribute battery_size
# Problem (Encapsulation) : Modify the Car class to encapsulate the brand attribute, making it private, and provide a getter method for it
# Problem (Polymorphism) : Demonstrate polymorphism by defining a method fuel_type in both Car and ElectricCar classes, but with different behaviours.
# Problem (Class Variable) : Add a class variable to the Car class that keeps track of the number of cars created.
# Problem (Static Method) : Add a static method to the Car class that returns description of cars.
# Problem (Property Decorators) : Use a property decorator in the Car class to make the model attribute read-only
# Problem (Class Inheritance and isinstane() function) : Demonstrate the use of isinstance() to check if my_tesla is an instance of Car and ElectricCar .
#  Problem (Multiple Inheritance) : Create two classes battery and Engine, and let the Electric Car class inherit from both, demonstrating multiple inheritance. 

class Car:
    total_car = 0
    
    def __init__ (self, brand, model):
        self.__brand = brand
        self.__model = model
        Car.total_car += 1

    def get_brand(self):
        return self.__brand + " !"

    def full_name(self):
        return f"{self__brand} {self.__model}"

    def fuel_type(self):
        return "Petrol or Disel"

    @staticmethod   
    def general_description():
        return "Cars are means of transport"

    @property
    def model(self):
        return self.__model


class ElectricCar(Car):
    def __init__ (self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

    def fuel_type(self):
        return "Electric Charge"


# my_tesla = ElectricCar("Tesla", "Model S", "85kWh")

# print(isinstance(my_tesla, Car))
# print(isinstance(my_tesla, ElectricCar))


# print(my_tesla.full_name())
# print(my_tesla.battery_size)
# print(my_tesla.__brand)
# print(my_tesla.get_brand())
# print(my_tesla.fuel_type())

# safari = Car("Tata", "Safari")
# Car("Tata", "Nexon")
# print(safari.fuel_type())

# print(Car.total_car)
# print(Car.general_description())
# safari.model = "City"
# print(safari.model)


# my_car = Car("Toyota","Corolla")

# print(my_car.brand)
# print(my_car.model)
# print(my_car.full_name())

# my_new_car = Car("Tata", "Safari")
# print(my_new_car.brand)
# print(my_new_car.model)


class Battery:
    def battery_info(self):
        return "this is battery"

class Engine:
    def engine_info(self):
        return "this is engine"

class ElectricCarTwo(Battery, Engine, Car):
    pass

my_new_tesla = ElectricCarTwo("Tesla", "Model W")
print(my_new_tesla.battery_info())
print(my_new_tesla.engine_info())


    