class Car:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model

    def full_name_car(self):
        return self.brand + " " + self.model

my_car = Car("Toyota","Corolla")
print(my_car.brand)
print(my_car.model)
my_car.full_name_car()
result = my_car.full_name_car()
print(result)