'''Завдання 1
    Створіть клас Editor, 
    який містить методи view_document та edit_document. 
    Нехай метод edit_document виводить на екран інформацію про те, що редагування документів недоступне для безкоштовної версії. 
    Створіть підклас ProEditor, у якому цей метод буде перевизначено. 
    Введіть ліцензійний ключ із клавіатури і, якщо він коректний, створіть екземпляр класу ProEditor, інакше Editor. 
    Викликайте методи перегляду та редагування документів.        
'''

class Editor:
    def view_document(self):
        print('Document viewing is available')

    def edit_document(self):
        print('Document editing is not available in the free version')

class ProEditor(Editor):
    def edit_document(self):
        key = input('Enter the license key: ')
        if key == '12345':
            print('Document editing is available')
        else:
            print('Document editing is not available in the free version')        

editor = ProEditor()

print(f"Перегляд документів: {editor.view_document()}\n Редагування документів: {editor.edit_document()}")


