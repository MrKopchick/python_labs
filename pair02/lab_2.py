# n = int(input())
# suma = 0
# avg = 0
# count = 0
# for i in range(1, n + 1):
#     if i % 3 == 0 or i % 5 == 0:
#         count += 1
#         suma += i
# avg = suma / count if count > 0 else 0
# print(f"Suma: {suma}")
# print(f"Average: {avg}")
# print(f"Count: {count}")

# n = int(input("enter number: "))
# suma = 0
# count = 0
# max = 0
# min = 0
# while n > 0:
#     digit = n % 10
#     suma += digit
#     count += 1
#     if digit > max:
#         max = digit
#     if min == 0 or digit < min:
#         min = digit
#     n //= 10
# print(f"Suma: {suma}")
# print(f"Count: {count}")
# print(f"Max: {max}")
# print(f"Min: {min}")

# n = int(input("enter number: "))
# for i in range(1, n + 1):
#     while i > 0:
#         digit = i % 10
#         if(digit == 0):
#             continue
#         if(i % digit == 0):
#             print(i)
#             break

# n = int(input("enter number: "))
# for i in range(1, n + 1):
#     num = i
#     ok = True
#     while num > 0:
#         digit = num % 10
#         if digit == 0:
#             ok = False
#         elif i % digit != 0:
#             ok = False        
#         num //= 10
#     if ok:
#         print(i, end=" ")

# width = int(input("Enter width: "))
# height = int(input("Enter height: "))
# fill_char = input("Enter fill character: ")
# border_char = input("Enter border character: ")
# for i in range(height):
#     for j in range(width):
#         if i == 0 or i == height - 1 or j == 0 or j == width - 1:
#             print(border_char, end="")
#         else:
#             print(fill_char, end="")
#     print()