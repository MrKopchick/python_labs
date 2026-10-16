#1
# class Rectangle:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#     def info(self):
#         print(f'{self.width} x {self.height}: area = {self.width * self.height}')
# rect1 = Rectangle(5,3)
# rect2 = Rectangle(10,4)
# rect1.info()
# rect2.info()

#2
# class Student:
#     def __init__(self, name):
#         self.name = name
#         self.grades = []
#     def add_grade(self, grade):
#         try:
#             clean_grade = int(grade)
#             if 1 <= clean_grade <= 12:
#                 self.grades.append(clean_grade)
#             else:
#                 raise ValueError()
#         except ValueError as error:
#             print(f"problem to add {grade}. Must be int number in 1-12 range")
#     def average(self):
#         if len(self.grades) > 0:
#             return sum(self.grades) / len(self.grades)
#         else:
#             return 0
#     def __str__(self):
#         return f'{self.name}: {self.grades}, average: {self.average()}'

# 2 - result
# std1 = Student("Spanch Bob")
# std1.add_grade(10)
# std1.add_grade(2)
# std1.add_grade(100)
# std1.add_grade("abc")
# print(std1.__str__())

# 3
# best_avg = 0
# students = [
#     Student("Tverdohlib"),
#     Student("Vorobiov"),
#     Student("Plyushch"),
#     Student("Leshenko"),
#     Student("Sidelnik")
# ]
# for i in [10, 11, 11]:
#     students[0].add_grade(i)
# for i in [9, 10]:
#     students[1].add_grade(i)
# for i in [11, 11, 12]:
#     students[2].add_grade(i)
# for i in [8, 9, 10]:
#     students[3].add_grade(i)
# for i in [11, 12, 11]:
#     students[4].add_grade(i)
# for student in students:
#     if student.average() > best_avg:
#         best_avg = student.average()
#     print(f'{student.name} - {round(student.average(), 2)}')
# for student in students:
#     if student.average() == best_avg:
#         print(f"Best: {student.name}, {round(student.average(), 2)}")

# 4
# class BankAccount:
#     def __init__(self, owner, balance=0):
#         self.owner = owner
#         self.balance = balance
#     def deposit(self, amount):
#         try:
#             value = int(amount)
#             if value <= 0:
#                 raise ValueError("amount must be bigger thab 0")
#             else:
#                 self.balance+=value
#         except ValueError as error:
#             print(error)
#     def withdraw(self, amount):
#         try:
#             value = int(amount)
#             if value <= 0:
#                 raise ValueError("amount must be bigger than 0")
#             elif value > self.balance:
#                 raise ValueError(f"not enough money on balance for -{value}")
#             else:
#                 self.balance+=value
#         except ValueError as error:
#             print(error)
#     def info(self):
#         print(f'{self.owner}: {self.balance}grn')
# o1 = BankAccount("Ivan", 1000)
# o2 = BankAccount("Olha", 700)
# o1.deposit(500)
# o1.withdraw(300)
# o1.withdraw(2000)
# o1.deposit(-50)

# o2.withdraw(200)
# o2.deposit(100)
# o2.withdraw(0)
# o2.withdraw(1000)

# o1.info()
# o2.info()