'''Завдання 1
    Створіть клас, який описує книгу. 
    Він повинен містити інформацію про автора, назву, рік видання та жанр. 
    Створіть кілька різних книжок. Визначте для нього методи _repr_ та _str_.
'''
class Book:
    def __init__(self, author:str, name:str, year:int, genre:str):
        self.author = author
        self.name = name
        self.year = year
        self.genre = genre

book1 = Book("Зед Шоу", "Learn Python the Hard Way", 2013, "Training")
book2 = Book("Олексій Васильєв", "Програмування мовою Python", 2024, "Training")
book3 = Book("Грегори Девид Робертс", "Шантарам", 2003, "Novel")

print(book1.author)

