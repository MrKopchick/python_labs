# book = {
#     'title': 'Кобзар',
#     'author': 'Шевченко',
#     'copies': 15
# }
# print(book)
# class Book:
#     def init(self,title, author, copies):
#         self.title = title
#         self.author = author
#         self.copies = copies
#     def available(self):
#         return self.copies > 0
# book1 = Book('Кобзар','Тарас Шевченко', 12)
# print(book1.title, book1.author, book1.copies)
# print(book1.available())
# class Rectangle:
#     def init(self,width,height):
#         self.width = width
#         self.height = height
#     def area(self):
#         return self.width * self.height
#     def perimetr(self):
#         return 2 * (self.width + self.height)
#     def info(self):
#         print(f'Ширина: {self.width}, висота: {self.width}')
#         print(f'Периметр: {self.perimetr()}')
#         print(f'Площа: {self.area()}')
# rectangle = Rectangle(4,5)
# rectangle.info()
# class Counter:
#     def init(self):
#         self.value = 0
#     def increment(self):
#         self.value += 1
# counter1 = Counter()
# counter2 = Counter()
# print(f'Було: {counter1.value, counter2.value}')
# counter1.increment()
# counter1.increment()
# print(f'Стало: {counter1.value, counter2.value}')
# class Book:
#     def init(self,title,copies):
#         self.title = title
#         self.copies = copies
#     def give_one(self):
#         if self.copies > 0:
#             self.copies -= 1
#             print(f'Книгу видано {self.title}')
#         else:
#             print(f'Немає доступних примірників {self.title}')
# book = Book('Кобзар', 3)
# book.give_one()
# book.give_one()
# print(f'Залишилось {book.copies}')
# class Student:
#     def init(self,name,grades):
#         self.name = name
#         self.grades = grades
#     def add_grade(self,grade):
#         if grade >= 1 and grade <= 12:
#             self.grades.append(grade)
#         else:
#             print('Неправильний діапазон')
#     def avarage_grade(self):
#         if len(self.grades) == 0:
#             return 0
#         return sum(self.grades) / len(self.grades)
#     def info(self):
#         print(f'Name: {self.name}, Grades: {self.grades}')
#     def str(self):
#         return f'Student {self.name}, Grades: {self.grades}, Avarage: {self.avarage_grade()}'
# student1 = Student('Ivan')
# student2 = Student('Anna')
# student1.add_grade(12)
# student2.add_grade(10)
# student2.add_grade(13)
# student1.info()
# student2.info()
# print(f'Іван: {student1.grades}, Анна: {student2.grades}')
# print(f'Середнє: {student1.avarage_grade()}')
# print(f'Середнє: {student2.avarage_grade()}')
# students = [
#     Student('Anna', [1,2,3]),
#     Student('Ivan', [12,10,11])
# ]
# print(f'Students: {len(students)}')
# for student in students:
#     print(f'Student: {student.name}, Grades: {student.grades}')
# class Product:
#     def init(self,name,price,count):
#         self.name = name
#         self.price = price
#         self.count = count
#     def total_price(self):
#         return self.price * self.count
# mouse = Product('Mouse', 1500, 10)
# keyboard = Product('Keyboard', 1800, 4)
# print(mouse.total_price())
# print(keyboard.total_price())