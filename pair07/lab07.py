#1
# import os
# chars_count = 0
# lines_count = 0
# words_count = 0
# longest_line_number = 0
# longest_line_length = 0
# longest_line_text = ""
# if os.path.exists('text.txt'):
#     with open("text.txt", "r", encoding="utf-8") as file:
#         for number, line in enumerate(file, start=1):
#             lines_count+=1
#             chars_count+=len(line)
#             words_count+=len(line.split()) 
#             clean_line = line.strip()
#             if len(clean_line) > longest_line_length:
#                 longest_line_length = len(clean_line)
#                 longest_line_number = number
#                 longest_line_text = clean_line
# else:
#     print("no file")
# print(f'lines: {lines_count}')
# print(f'words: {words_count}')
# print(f'chars: {chars_count}')
# print(f'longest: №{longest_line_number}, {longest_line_length} chars')
# print(f'text: {longest_line_text}')

#2
# import os
# fragemnt = input("enter fragment: ")
# if os.path.exists('text.txt'):
#     with open("text.txt", "r", encoding="utf-8") as file:
#         for number, line in enumerate(file, start=1):
#             if fragemnt.lower() not in line.strip().lower():
#                 continue
#             else:
#                 print(f'{number}: {line}')
# else:
#     print("no file")

#3
# import os
# best_students = []
# if os.path.exists('students.txt'):
#     with open("students.txt", "r", encoding="utf-8") as file:
#         for line in file:
#             clean_line = line.strip()
#             name, grade = clean_line.split(";")
#             if int(grade) > 80:
#                 best_students.append([name, grade])
# else:
#     print("no file")
# with open("result.txt", "w", encoding="utf-8") as file:
#     for name, grade in best_students:
#         print(f"{name};{grade}", file=file)

#4
# import os
# def grades_maching():
#     students = {}
#     summary = []
#     if os.path.exists('grades.csv'):
#         with open("grades.csv", "r", encoding="utf-8") as file:
#             for line in file:
#                 clean_line = line.strip()
#                 student, subject, grade = clean_line.split(";")
#                 if student not in students:
#                     students[student]=[]
#                 students[student].append(int(grade))
#     for name, grade in students.items():
#         summary.append([name, len(grade), avg(grade)])
#     summary.sort(key=lambda item: item[2], reverse=True)
#     return summary
# def avg(grades):
#     return sum(grades)/len(grades)
# def best_students(students_rates):
#     highest_avg_l = students_rates[0][2]
#     top_students = []
#     for name, count, avg in students_rates:
#         if avg == highest_avg_l:
#             top_students.append(name)
#     return " and ".join(top_students)
# with open("report.txt", "w", encoding="utf-8") as file:
#     data = grades_maching()
#     for name, count, avg in data:
#         print(f"{name} grades: {count} avg: {avg:.2f}", file=file)
#     print(f"best: {best_students(data)}", file=file)