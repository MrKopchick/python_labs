# try:
#     a = float(input("a="))
#     b = float(input("b="))
#     result = a/b
#     print(result)
# except ValueError:
#     print("enter number")

# try:
#     number = int(input("please enter a number"))
#     print(100/ number)
# except ValueError:
#     print("please enter a number")
# except ZeroDivisionError:
#     print("please enter not 0")
# finally:
#     print("goodbye")

# while True:
#     try:
#         grade = int(input("Enter ur grade 1..12: "))
#         if grade < 1 or grade > 12:
#             raise ValueError("Error must be between 1 and 12")
#         print(grade)
#         break
#     except ValueError as error:
#         print(f"Error: {error}")

# def int_input(message):
#     while True:
#         try:
#             return int(input(message))
#         except ValueError:
#             print("please enter a number")

# def input_grade():
#     while True:
#         try:
#             grade = int(input("etner 1-12 grade:"))
#             if grade < 1 or grade > 12:
#                 raise ValueError("grade must be from 1 to 12")
#             return grade
#         except ValueError as error:
#             print(error)
# grade = input_grade()
# print("прийнято ", grade)

line = 'Anna;111'
parts = line.strip().split(';')
if len(parts) != 2:
    print('error')
else:
    name = parts[0]
    grade = parts[1]
        