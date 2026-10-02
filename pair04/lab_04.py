#1
# num_list = [12, 3, 4, 14, -12, 5, 10, 16, -4]
# positive = []
# negative = []
# even = []
# multiples_3 = []

# for number in num_list:
#     if number > 0:
#         positive.append(number)
#     else:
#         negative.append(number)
#     if number % 2 == 0:
#         even.append(number)
#     if number % 3 == 0:
#         multiples_3.append(number)

# suma = sum(num_list)
# avg = suma / len(num_list)
# print("Positive numbers:", positive)
# print("Negative numbers:", negative)
# print("Even numbers:", even)
# print("Multiples of 3:", multiples_3)
# print("Minimum number:", min(num_list))
# print("Maximum number:", max(num_list))
# print("Sum of numbers:", suma)
# print("Average of numbers:", round(avg, 2))

# 2
# group1 = {'Anna','Ivan','Olha'}
# group2 = {'Ivan','Maksym','Olha'}
# joint = group1 & group2
# group1_only = group1 - group2
# group2_only = group2 - group1
# all_students = group1 | group2
# print("joint:", ', '.join(joint))
# print("group1_only:", ', '.join(group1_only))
# print("group2_only:", ', '.join(group2_only))
# print("all_students:", ', '.join(all_students))

#3
# products = {
#     'milk': '48',
#     'tea': '75',
#     'banana': '30',
#     'mango': '150'
# }
# search_product = input("Enter the product name to search: ")
# price = products.get(search_product)
# if price is not None:
#     print(f"{search_product}: {price} UAH")
# else:
#     print(f"'{search_product}' not found in the product list.")
# new_item = input("Enter the new product name: ")
# new_price = input("Enter the price for the new product: ")
# products[new_item] = new_price
# print("Updated product list:")
# for product, price in products.items():
#     print(f"{product}: {price} UAH")
# min_price = input("Enter the minimum price to filter products: ")
# max_price = input("Enter the maximum price to filter products: ")
# for product, price in products.items():
#     if int(min_price) <= int(price) <= int(max_price):
#         print(f"{product}: {price} UAH")

# 4
# group_book = {
#     'Ivan': [10, 11, 12, 9, 10],
#     'Anna': [8, 9, 10, 11, 9]
# }
# group_info = ('10-IT', '2026\\2027')
# best_student = ""
# best_average = 0
# print(f"Group: {group_info[0]}, {group_info[1]}")
# print("\nGroup book:")
# for student, grades in group_book.items():
#     print(f"{student}: {grades}")
# new_student = input("Enter the name of the new student: ")
# new_grades = input("Enter the grades for the new student (comma-separated): ")
# new_grades_list = [int(grade.strip()) for grade in new_grades.split(',')]
# is_valid = True
# if len(new_grades_list) != 5:
#     is_valid = False
# else:
#     for grade in new_grades_list:
#         if grade < 1 or grade > 12:
#             is_valid = False
#             break
# if is_valid:
#     group_book[new_student] = new_grades_list
#     print(f"Student {new_student} added")
#     print("Updated group book:")
#     for student, grades in group_book.items():
#         print(f"{student}: {grades}")
#     print("Average grades:")
#     rating = []
#     for student, grades in group_book.items():
#         average_grade = sum(grades) / len(grades)
#         print(f"{student}: {average_grade}")
#         rating.append((average_grade, student))
#         if average_grade > best_average:
#             best_average = average_grade
#             best_student = student
#     rating.sort(reverse=True)
#     print("\nRating:")
#     for average, student in rating:
#         print(f"{student}: {average}")
#     print("the best student is:", best_student, best_average)
# else:
#     print("Error: student must have exactly 5 grades in the range 1-12.")