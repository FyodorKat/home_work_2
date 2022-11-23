import exceptions
from dataclasses import dataclass
from abc import ABC

class Vehicle(ABC):

    def __init__(self, weight=1, fuel=1, fuel_consumption=1): #потребление литры/100км
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption
        self.started = False

    def start(self):
        if not self.started:
            if self.fuel > 0:
                self.started
                return
            return exceptions.LowFuelError()
        print('уже заведена машина')
        return

    def move(self, distance): #distance = километры
        if self.started == False:
            self.start()
        need_fuel = distance*self.fuel_consumption/100
        if need_fuel <= self.fuel:
            self.fuel -= need_fuel
            print(f'Осталось топлива: {self.fuel}')
            return
        return exceptions.NotEnoughFuel()

#Создайте датакласс Engine, добавьте атрибуты volume и pistons
@dataclass
class Engine:
    volume: int = 10
    pistons: int = 10

#Cоздайте класс Car - класс Car должен быть наследником Vehicle - добавьте атрибут engine классу Car
#- объявите метод set_engine, который принимает в себя экземпляр объекта Engine и
# устанавливает на текущий экземпляр Car

class Car(Vehicle):
    def __init__(self, fuel, weight, fuel_consumption):
        super().__init__(fuel, weight, fuel_consumption)
        self.engine = Engine(10, 10)

    def set_engine(self, engine):
        self.engine = engine
        print(self.engine)

# Создайте класс Plane
#
# класс Plane должен быть наследником Vehicle
# добавьте атрибуты cargo и max_cargo классу Plane
# добавьте max_cargo в инициализатор (переопределите родительский)
# объявите метод load_cargo, который принимает число, проверяет, что в сумме с текущим cargo не будет перегруза,
# и обновляет значение, в ином случае выкидывает исключение exceptions.CargoOverload
# объявите метод remove_all_cargo, который обнуляет значение cargo и возвращает значение cargo,
# которое было до обнуления

class Plane(Vehicle):
    def __init__(self, max_cargo, cargo, weight, fuel, fuel_consumption):
        super().__init__(weight, fuel, fuel_consumption)
        self.max_cargo = max_cargo
        self.cargo = cargo
    def load_cargo(self, new_cargo):
        full_cargo = self.cargo + new_cargo
        if full_cargo <= self.max_cargo:
            self.cargo = full_cargo
            print(f'Новый вес груза: {self.cargo}')
            return
        return exceptions.CargoOverload()
    def remove_all_cargo(self):
        last_cargo = self.cargo
        self.cargo = 0
        return f'Занчение до обнуления: {last_cargo}'




a = Plane(fuel=100, max_cargo=100, cargo=20, weight=1, fuel_consumption=10)
a.load_cargo(new_cargo=50)
b = a.remove_all_cargo()
print(b)
print(a.cargo)
