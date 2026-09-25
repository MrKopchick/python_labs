#1

#a
#a = int(input("enter number: "));
#if a % 2 == 0:
#    print("a is even")
#else:
#    print("a is not even")

#b
# a = int(input("enter your age: "))
# if(a >= 18):
#     print("you are an adult")
# else:
#     print("you are not an adult")

#c
# r = int(input("enter your radius: "))
# print("Area: "+ str(3.14 * r * r))
# print("Perimeter: "+ str(2 * 3.14 * r))

#d
# a = int(input("a: "))
# b = int(input("b: "))
# if a > b:
#     print(a)
# elif a < b:
#     print(b)
# else:
#     print("a = b")

#2
# x, y = map(int, input("x y").split());
# if(x > 0 and y > 0):
#     print("1st quadrant")
# elif(x < 0 and y > 0):
#     print("2nd quadrant")
# elif(x < 0 and y < 0):
#     print("3rd quadrant")
# elif(x > 0 and y < 0):
#     print("4th quadrant")
# else:
#     print("x or y is 0")

#3
# age = int(input("enter your age: "))
# if 11 <= age % 100 <= 14:
#     print(str(age) + " rokiv")
# elif age % 10 == 1:
#     print(str(age) + " rik")
# elif 2 <= age % 10 <= 4:
#     print(str(age) + " roky")
# else:
#     print(str(age) + " rokiv")

#4
# n = int(input("enter trip count: "))
# k =  int(input("enter count in stack of tickets: "))
# p1 = int (input("enter price of 1 ticket: "))
# p2 = int (input("enter price of 1 stack of tickets: "))
# cost = 0;
# if p2 >= k * p1:
#     cost = n * p1;
# else:
#     stack_cost = (n // k) * p2
#     single_cost = (n % k) * p1
#     if single_cost < p2:
#         cost = stack_cost + single_cost
#     else:
#         cost = stack_cost + p2;
# print("Total  cost: " + str(cost))