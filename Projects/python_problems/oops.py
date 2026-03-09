class Car:
    total_car = 0
    
    def __init__(self,brand,model):
        self.__brand = brand
        self.model = model
        Car.total_car += 1

    def full_name(self):
        return f"{self.__brand} {self.model}"
    
    def get_brand(self):
        return self.__brand + " ! "
    
    def fuel_type(self):
        return "Petrol or Diesel"

    

class ElectricCar(Car):
    def __init__(self,brand,model,battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size
    def fuel_type(self):
        return "Electric charge"


my_tesla = ElectricCar("Tesla","Model s","85Kwh")
safari = Car("tata","tiago")
test =Car("test","test")
print(my_tesla.get_brand())
print(safari)
print(safari.fuel_type())
print(my_tesla.fuel_type())
print(safari.total_car)
print(Car.total_car)