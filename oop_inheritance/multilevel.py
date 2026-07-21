# Example of Multilevel Inheritance (Car)

# Base Class
class Vehicle:
    def getVehicle(self):
        self.company = input("Enter Company Name: ")
        self.color = input("Enter Color: ")

# First Derived Class
class Car(Vehicle):
    def getCar(self):
        self.model = input("Enter Model Name: ")
        self.price = int(input("Enter Price: "))

# Second Derived Class
class ElectricCar(Car):
    def getElectricCar(self):
        self.battery = int(input("Enter Battery Capacity (kWh): "))
        self.range = int(input("Enter Range (km): "))

    def display(self):
        print("\n----- Electric Car Details -----")
        print("Company :", self.company)
        print("Color   :", self.color)
        print("Model   :", self.model)
        print("Price   :", self.price)
        print("Battery :", self.battery, "kWh")
        print("Range   :", self.range, "km")


# Object
e1 = ElectricCar()

# Method Calls
e1.getVehicle()
e1.getCar()
e1.getElectricCar()
e1.display()