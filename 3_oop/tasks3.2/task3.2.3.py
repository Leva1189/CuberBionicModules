'''Завдання 3
   Створіть ієрархію класів із використанням множинного успадкування. 
   Виведіть на екран порядок вирішення методів для кожного класу. 
   Поясніть, чому лінеаризація даних класів виглядає саме так.       
'''

class Computer():
    def __init__(self, cpu:str, ram:int, hdd:int):
        self.cpu = cpu
        self.ram = ram
        self.hdd = hdd
    def info(self)->str:
        print(f'CPU: {self.cpu}\nRAM: {self.ram}\nHDD: {self.hdd}')

class Monitor():
    def __init__(self, diagonal:int, matrix:str):
        self.diagonal = diagonal
        self.matrix = matrix
    def info(self)->str:
        print(f'Diagonal: {self.diagonal}\nMatrix: {self.matrix}')


class Laptop(Computer, Monitor):
    def __init__(self, cpu:str, ram:int, hdd:int, diagonal:int, matrix:str):
        super().__init__(cpu, ram, hdd)
        super(Computer, self).__init__(diagonal, matrix)
    def info(self)->str:
        super().info()
        super(Computer, self).info()

print(Laptop.mro())

laptop = Laptop('Intel Core i5', 8, 256, 15, 'IPS')
laptop.info()
