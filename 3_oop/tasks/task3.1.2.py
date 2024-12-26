'''Завдання 2
    Створіть клас, який описує відгук до книги. 
    Додайте до класу книги поле – список відгуків. 
    Зробіть так, щоб при виведенні книги на екран за допомогою функції print також виводилися відгуки до неї.     
'''
class BookReview:
    def __init__(self, author:str, text:str, rating:int):
        self.author = author
        self.text = text
        self.rating = rating
    def __repr__(self) -> str:
        return f"Reviewer: {self.author}\nText - {self.text}\nRating - {self.rating}\n"
    

class Book:
    def __init__(self, author:str, name:str, year:int, genre:str, review:BookReview):
        self.author = author
        self.name = name
        self.year = year
        self.genre = genre
        self.review = review
    def __repr__(self) -> str:
        return f"Book_repr - {self.name}\nAuthor - {self.author}\nYear - {self.year}\nGenre - {self.genre}\nReview - {self.review}\n"
    
    def __str__(self) -> str:
        return f"Book_ str- {self.name}\nAuthor - {self.author}\nYear - {self.year}\nGenre - {self.genre}\nReview - {self.review}\n"
    
book1 = Book("Зед Шоу", "Learn Python the Hard Way", 2013, "Training", BookReview("John", "Good book", 5))
book2 = Book("Олексій Васильєв", "Програмування мовою Python", 2024, "Training", BookReview("Piter", "Good book", 5))
book3 = Book("Грегори Девид Робертс", "Шантарам", 2003, "Novel", BookReview("John", "Good book", 5))

list_books = [book1, book2, book3]
print(list_books)