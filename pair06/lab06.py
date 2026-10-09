#1
# import math

# radius = int(input("enter radius: "))
# sides_leg = list(map(int, input("enter sides leg separate with coma: ").split(',')))
# items = int(input("enter items count: "))
# pack_size = int(input("enter pack size: "))
# print(f'Area of circle: {round(math.pi * math.pow(radius, 2),2)}')
# print(f'hypo: {math.hypot(sides_leg[0], sides_leg[1])}')
# print(f'packs needed: {math.ceil(items/pack_size)}')

#2
# import math
# import random
# import statistics as st
# number_of_rating = int(input("enter number of ratings: "))
# rating_list = []
# for i in range(0, number_of_rating):
#     rating_list.append(random.randint(1,12))
# print(rating_list)
# print(f'min: {min(rating_list)}')
# print(f'max: {max(rating_list)}')
# print(f'average: {round(st.mean(rating_list), 1)}')
# print(f'median: {st.median(rating_list)}')

#3
# from datetime import date
# year = int(input("year: "))
# month = int(input("month: "))
# day = int(input("day: "))
# now = date.today()
# target = date(year, month, day)
# left = target-now
# if left.days > 0:
#     print(f'will be in {left.days} days')
# elif left.days < 0:
#     print(f'{abs(left.days)} behind')
# else:
#     print("its today:)")

#4
# import student_utils
# import tkinter as tk

# students = ['Anna','Ivan','Olha']

# def report():
#     raw_value = entry_count.get().strip()

#     if not raw_value.isdecimal():
#         messagebox.showerror(
#             "error",
#             "int number from 1 to 20"
#         )
#         return
#     count = int(raw_value)
#     if not (1 <= count <= 20):
#         messagebox.showerror(
#             "error",
#             "int number from 1 to 20"
#         )
#         return
#     report_lines = []
#     for student in students:
#         grades = student_utils.generate_grades(count)
#         avg = student_utils.average_grade(grades)
#         level = student_utils.get_level(avg)
#         report_lines.append(f"{student}: {grades} -> {avg} -> {level}")
#     full_report = "\n".join(report_lines)
#     print(full_report)
#     text_result.delete("1.0", tk.END)
#     text_result.insert(tk.END, full_report)

# window = tk.Tk()
# window.title("student statistic")
# window.geometry("500x500")

# label_instruction = tk.Label(window, text="Enter grades count(1-20):")
# entry_count = tk.Entry(window, width=15, justify="center")
# entry_count.insert(0, "5")
# entry_count.pack(pady=5)
# btn_generate = tk.Button(
#     window,
#     text="Сформувати звіт",
#     bg="green",
#     fg="white",
#     command=report,
# )
# btn_generate.pack(pady=10)
# text_result = tk.Text(window, height=8, width=54)
# text_result.pack(padx=15, pady=(5, 15))

# if __name__ == "__main__":
#     window.mainloop()