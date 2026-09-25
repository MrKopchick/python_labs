#a = int(input("#1: "));
#b = int(input("#2: "));

#print(a+b)

a = int(input("#1: "))
b = int(input("#2: "))
c = int(input("#3: "))

if a > b:
    print("a is greater than b")
    if a > c:
        print("a is greater than c")
    else:
        print("c is greater than a")
elif(b > a):
    print("b is greater than a")
    if b > c:
        print("b is greater than c")
    else:
        print("c is greater than b. C the bigger number")
elif(c > a):
    print("c is greater than a")
    if c > b:
        print("c is greater than b")
    else:
        print("b is greater than c. B the bigger number")
else:
    print("a = b = c")