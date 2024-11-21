'''Завдання 1
    Створіть клас, який описує книгу. 
    Він повинен містити інформацію про автора, назву, рік видання та жанр. 
    Створіть кілька різних книжок. Визначте для нього методи _repr_ та _str_.
'''
class Book:
    def __init__(self, author:str, name:str, year:str, genre:str):
        self.author = author
        self.name = name
        self.year = year
        self.genre = genre

book1 = Book("",)
book2 = Book("",)
book3 = Book("")

