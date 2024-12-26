'''Завдання 4
    Створіть клас, який описує автомобіль. 
    Створіть клас автосалону, що містить в собі список автомобілів, 
    доступних для продажу, і функцію продажу заданого автомобіля.         
'''

class car:
    def __init__(self, brand:str, model:str, year:int, price:int):
        self.brand = brand
        self.model = model
        self.year = year
        self.price = price

    def __repr__(self)->str:
        return f'Auto: {self.brand}\n {self.model}\n {self.year}\n {self.price}$'


class AutoSalon:
    def __init__(self, title:str, cars:car):
        self.title = title
        self.cars = cars

    def __repr__(self)->str:
        return f'{self.title}\n{self.cars}'

Car1 = car("BMW", "X5", 2010, 10000)
Car2 = car("Audi", "A6", 2015, 15000)
Car3 = car("Mercedes", "E-class", 2018, 20000)       

Dealer1 = AutoSalon("AutoRia", (Car1, Car2))
Dealer2 = AutoSalon("AutoService", Car3)

Dealer_list = [Dealer1, Dealer2]
print(Dealer_list)

