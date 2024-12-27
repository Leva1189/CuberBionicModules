'''Завдання 2
    Опишіть класи графічного об'єкта, 
    прямокутника та об'єкта, 
    який може обробляти натискання миші. 
    Опишіть клас кнопки. 
    Створіть об'єкт кнопки та звичайного прямокутника. 
    Викличте метод натискання на кнопку.       
'''

class GraphicObject:
    def click(self):
        print('Click on the object')

class Rectangle(GraphicObject):
    def __init__(self, width:int, height:int):
        self.width = width
        self.height = height

class Button(Rectangle):
    def click(self):
        print('Click on the button')

Button1 = Button(10, 20)
Rectangle1 = Rectangle(10, 0)

Button1.click()














