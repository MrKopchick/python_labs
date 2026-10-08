#1
# pi = 3.14159
# def rectangle_area(length, width):
#     return length * width
# def circle_area(radius):
#     return pi * radius ** 2
# def triangle_area(base, height):
#     return 0.5 * base * height
# def main():
#     action = input("Choose a shape (rectangle, circle, triangle): ").strip().lower()
#     if action == "rectangle":
#         length = float(input("Enter the length: "))
#         width = float(input("Enter the width: "))
#         area = rectangle_area(length, width)
#         print(f"The area of the rectangle is: {area}")
#     elif action == "circle":
#         radius = float(input("Enter the radius: "))
#         area = circle_area(radius)
#         print(f"The area of the circle is: {area}")
#     elif action == "triangle":
#         base = float(input("Enter the base: "))
#         height = float(input("Enter the height: "))
#         area = triangle_area(base, height)
#         print(f"The area of the triangle is: {area}")
#     else:
#         print("Invalid shape selected.")
# main()

#2
# def is_prime(num):
#     if num <= 1:
#         return False
#     for i in range(2, num):
#         if num % i == 0:
#             return False
#     return True
# def divisor(num):
#     divisors = []
#     for i in range(1, num + 1):
#         if num % i == 0:
#             divisors.append(i)
#     return divisors
# def digit_sum(num):
#     return sum(map(int, str(abs(num))))
# def main():
#     number = int(input("Enter a number: "))
#     if is_prime(number):
#         print(f"{number} is a prime number.")
#     else:
#         print(f"{number} is not a prime number.")
#     print(f"Divisors of {number}: {divisor(number)}")
#     print(f"Sum of digits of {number}: {digit_sum(number)}")
# main()

#3
# def average(grades):
#     return sum(grades) / len(grades)
# def minimum(grades):
#     return min(grades)
# def maximum(grades):
#     return max(grades)
# def count_above(grades, threshold):
#     count = 0
#     for grade in grades:
#         if grade > threshold:
#             count += 1
#     return count
# def main():
#     grades = int(input("Enter the number of grades: "))
#     grades_list = []
#     for _ in range(grades):
#         grade = float(input("Enter a grade: "))
#         grades_list.append(grade)
#     threshold = int(input("Enter a threshold to count grades above: "))
#     print(f"Average grade: {average(grades_list)}")
#     print(f"Minimum grade: {minimum(grades_list)}")
#     print(f"Maximum grade: {maximum(grades_list)}")
#     print(f"Number of grades above {threshold}: {count_above(grades_list, threshold)}")
# main()

#4
# def len_pass(password):
#     if len(password) < 8:
#         return False
#     else:
#         return True
# def has_digit(password):
#     for char in password:
#         if char.isdigit():
#             return True
#     return False
# def has_upper(password):
#     for char in password:
#         if char.isupper():
#             return True
#     return False
# def has_lower(password):
#     for char in password:
#         if char.islower():
#             return True
#     return False
# def has_special(password):
#     for char in password:
#         if not char.isalnum():
#             return True
#     return False
# def main():
#     password = input("Enter a password: ")
#     if len_pass(password) and has_digit(password) and has_upper(password) and has_lower(password) and has_special(password):
#         print("Password is strong.")
#     else:
#         print("Password is weak.")
#         if not len_pass(password):
#             print("Password must be at least 8 characters long.")
#         if not has_digit(password):
#             print("Password must contain at least one digit.")
#         if not has_upper(password):
#             print("Password must contain at least one uppercase letter.")
#         if not has_lower(password):
#             print("Password must contain at least one lowercase letter.")
#         if not has_special(password):
#             print("Password must contain at least one special character.")
# main()