"""
Объявите следующие исключения:
- LowFuelError
- NotEnoughFuel
- CargoOverload
"""
class LowFuelError(Exception):
    def __init__(self):
        print('Нет топлива, бро')

class NotEnoughFuel(Exception):
    def __init__(self):
        print('Топлива не хватит')

class CargoOverload(Exception):
    def __init__(self):
        print('Перегруз')