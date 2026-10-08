# def sayHello():
#     print("Hello, World!")
#
# sayHello()
# def sayHello(name, surname): #name - параметр функції
#     print(f"Hello, {name} {surname}!")
#
# sayHello("Ivan", "Ivanov") #Ivan - аргумент функції
# sayHello("Oleg", "Olegov") #Oleg - аргумент функції
# def rectangle_area(length, width):
#     return length * width
#
# width = int(input("Enter the width of the rectangle: "))
# length = int(input("Enter the length of the rectangle: "))
# S = rectangle_area(length, width)
# print(f"The area of the rectangle is: {S}")
# def hello_world(name, message = "Welcome to the program!"):
#     print(f"Hello, {name}! {message}")
# hello_world("Ivan")
# def price_with_discount(price, discount = 0):
#     return price - price * discount / 100
# print(price_with_discount(1000, 10))
# def min_max(numbers):
#     return min(numbers), max(numbers)
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# min_, max_ = min_max(numbers)
# print(min_max(numbers))
# def is_even(number):
#     """Повертає True, якщо число парне, і False, якщо непарне."""
#     return number % 2 == 0
# print(is_even(5))
# print(is_even(6))
# print(is_even.__doc__)
def rectangle_area(length, width):
    return length * width
def main():
    length = int(input("Enter length: "))
    width = int(input("Enter width: "))

    print(f"width = {width}, length = {length}, area = {rectangle_area(length, width)}")