# grades = [3, 10, 7]
# numbers = []
# grades[1] = 12
# print(grades)
# numbers.append(10)
# numbers.append([11,4])
# numbers.insert(100, [5,6])
# numbers.extend([7,8,9,7])
# numbers.remove (7)
# numbers.pop(1)
# #del numbers[1]
# numbers.clear()
# print(numbers.count(8))
# print(numbers.index(8))
# if 8 in numbers:
#     print("True")
# len()
# min()
# max()
# sum()
# print(numbers)
# numbers = [1, 2, 3]
# numbers.sort(reverse = True)
#
# numbers = [1, 2, 3]
# positive = []
# for number in numbers:
#     positive.append(number)
# print(positive)
# point = (-10, 22)
# rgb = (255, 0 ,0)
# data = ()
# student = "Ivan", "Vorobiov"
# a=(10,)
# b = a + (23,)
# print(b)
# point = point[:1] = point[:-1]
# point = (-12,6)
# x,y = point
# print(x)
# print(y)
# subjects = {"Python", "HTML", "C++"}
# data = {}
# print(type(data))
# subjects.add("C++")
# subjects.update(["Java", "Python"])
# subjects.remove("Java")
# subjects.discard("C#")
# print(subjects)
# if "Python" in subjects:
#     print("Python")
# names = ["Ivan", "Oleg", "Olha", "Ivan", "Maria", "Oleg"]
# unique_names = set(names)
# print(unique_names)
#
# group1 = {"Ivan", "Oleg", "Olha"}
# group2 = {"Ivan", "Mykola", "Ann"}
#
# peretyn =  group1 & group2
# obiednanya =  group1 | group2
# riznitsya =  group1 - group2
# print(obiednanya)
# print(peretyn)
# print(riznitsya)

student = {
    "name": "Ivan",
    "grade": 11
}
student2 = {}
student3 = dict()

print (student["name"])

student["age"] = 18
print(student)
student["age"] = 19
print(student)
student_update = student.pop("age")
print(student_update)
