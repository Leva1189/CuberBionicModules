'''Завдання 2
    Створіть клас, який описує відгук до книги. 
    Додайте до класу книги поле – список відгуків. 
    Зробіть так, щоб при виведенні книги на екран за допомогою функції print також виводилися відгуки до неї.     
'''
class BookReview:
    def __init__():
        self.author = author
        self.name = name
        self.year = year
        self.genre = genre
    def info(self):
        print(f"{self.author}\n{self.name}\n{self.year}\n{self.genre}\n")
    def __repr__(self):
        print(f"{self.author}\n{self.name}\n{self.year}\n{self.genre}\n")
    def __str__(self):
        print(f"{self.author}\n{self.name}\n{self.year}\n{self.genre}\n")        

book1 = Book("Зед Шоу", "Learn Python the Hard Way", 2013, "Training")
book2 = Book("Олексій Васильєв", "Програмування мовою Python", 2024, "Training")
book3 = Book("Грегори Девид Робертс", "Шантарам", 2003, "Novel")


