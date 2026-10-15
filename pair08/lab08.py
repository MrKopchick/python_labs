#1
# while True:
#     try:
#         a = int(input("enter number 1: "))
#         b = int(input("enter number 2: "))
#         match input("enter operation + - / *: "):
#             case '+': print(a+b)
#             case '-': print(a-b)
#             case '*': print(a*b)
#             case '/': print(a/b)
#             case _:
#                 raise ValueError("unknown operation") 
#     except ZeroDivisionError:
#         print("no dibision by zero")
#     except ValueError as error:
#         if not error == "unknown operation":
#             print("enter number")
#         else:
#             print(error)

#2
# def input_grade():
#     while True:
#         try:
#             try:
#                 grade = int(input("Оцінка: "))
#             except ValueError:
#                 print("required integer number")
#                 continue
#             if grade < 1 or grade > 12:
#                 raise ValueError("grade must be from 1 to 12")
#             return grade
#         except ValueError as error:
#             print(error)
# grade = input_grade()
# print(f"grade is: {grade}")

#3
# students = ["Vorobiov", "Leshenko", "Plush", "Sidelnik"]
# grades = {
#     "Math": 11,
#     "Ukranian": 2,
#     "Phisycs": 9,
#     "History": 6
# }
# try:
#     choice = int(input("1-student; 2-subject: "))
#     if choice not in [1,2]:
#         raise ValueError("1 or 2")
# except ValueError as error:
#     if str(error) == "1 or 2":
#         print(error)
#     else:
#         print("enter int number")
# else:
#     if choice == 1:
#         try:
#             print(f'student: {students[int(input("Index: "))]}')
#         except ValueError:    
#             print("enter int number")
#         except IndexError:
#             print("no student has been found")
#     elif choice == 2:
#         try:
#             print(f'Grade: {grades[input("name of subject: ")]}')
#         except KeyError:
#             print("no subject has been found")

#4
try:
    students=[]
    failed_lines=0
    with open("students.txt", "r", encoding="utf-8") as file:
        for number, line in enumerate(file, start=1):
            line = line.strip()
            if not line:
                continue
            try:
                parts = line.split(";")
                if not len(parts) == 2: raise ValueError("wrong line format")
                student, grade = parts[0].strip(), parts[1].strip()
                try:
                    grade = int(grade)
                except ValueError:
                    raise ValueError("grade must be int number")
                if grade > 100 or grade<0:
                    raise ValueError("grade must be 0-100")
                students.append((student, grade))
            except ValueError as error:
                failed_lines+=1
                print(f'line {number}: {error}')
except FileNotFoundError:
    print("no file")
else:
    students.sort(key=lambda item: item[1], reverse=True)
    with open("report.txt", "w", encoding="utf-8") as report:
        for name, grade in students:
            #report.write(f'{name};{grade}')
            print(f'{name};{grade}', file=report)
    print(f'Correct lines: {len(students)}')
    print(f'Skipped: {failed_lines}')
    print(f'report has been created')