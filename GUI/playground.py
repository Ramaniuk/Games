def add(*numbers): # unlimited arguments
    sum = 0
    for number in numbers:
        sum += number
    return sum
print(add(6,5,4,67,9,7,5,3,6))


class Car:
    def __init__(self, **kw):
        self.make = kw["make"]
        self.model = kw.get("model")

my_car = Car(make="Nissan")
print(my_car.make)
print(my_car.model)