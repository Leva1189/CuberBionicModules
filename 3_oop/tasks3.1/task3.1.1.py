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
    # def info(self):
        # print(f"{self.author}\n{self.name}\n{self.year}\n{self.genre}\n")
    def __repr__(self) -> str:
        return f"Book_repr - {self.name}\nAuthor - {self.author}\nYear - {self.year}\nGenre - {self.genre}\n"
    
    def __str__(self) -> str:
        return f"Book_ str- {self.name}\nAuthor - {self.author}\nYear - {self.year}\nGenre - {self.genre}\n"        

book1 = Book("Зед Шоу", "Learn Python the Hard Way", 2013, "Training")
book2 = Book("Олексій Васильєв", "Програмування мовою Python", 2024, "Training")
book3 = Book("Грегори Девид Робертс", "Шантарам", 2003, "Novel")


list_books = [book1, book2, book3]
# 
print(list_books)

# print(repr(book1))
# print(repr(book2))
# print(repr(book3))
# print("____________________________\n")
# 
# print(str(book1))
# print(str(book2))
# print(str(book3))




