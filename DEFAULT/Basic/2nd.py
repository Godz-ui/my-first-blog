"""
number = 10

while number > 1:
    print(f"number = {number}")
    number -= 1
print("Работа программы завершена")
"""

"""number = 10
while number < 5:
    print(f"number = {number}")
    number += 1
else:
    print(f"number = {number}. Работа цикла завершена")
print("Работа программы завершена")
"""
"""
message = "Hello"

for c in message:
    print(c, end="  ")

message = ' ello'

for c in message:
        print(c)
"""
"""
for nam in range(1, 11):
    print(nam, end=" ")
    """
"""
i = 1
j = 1
while i < 11:
    while j < 11:
        print(i * j, end="\t")
        j += 1
    print("\n")
    j = 1
    i += 1
for c1 in  "ab":
    for c2 in "ba":
        print(f"{c1}{c2}")
"""
"""
for c1 in  "ab":
    for c2 in "ba":
        print(f"{c1}{c2}")
"""
"""
number = 0
while number < 5:
    number +=1
    if number == 4:
        break
    print(f"number = {number}")
"""


# def say_hello(name):
#     print(f"Hello, {name}")
#
#
# say_hello("Tom")
# say_hello("Bob")
# say_hello("Alice")

# def sum(*numbers):
#     result = 0
#     for n in numbers:
#         result += n
#     print(f"sum = {result}")
#
# sum(1, 2, 3, 4, 5)
# sum(3, 4, 5, 6)

# def print_person(name, age):
#     if age > 120 or age < 1:
#         print("Invalid age")
#         return
#     print(f"Name: {name}  Age: {age}")
#
#
# print_person("Tom", 22)
# print_person("Bob",122)

# def sum(a, b): return a + b
#
# def subtract(a, b): return a - b
#
# def multiply(a, b): return a * b
#
# def select_operation(choice):
#     if choice == 1:
#         return sum
#     elif choice == 2:
#         return subtract
#     else:
#         return multiply
#
# operation = select_operation(1)
# print(operation(10, 6))
#
# operation = select_operation(2)
# print(operation(10, 6))
#
# operation = select_operation(3)
# print(operation(10, 6))


# sum = lambda a,b:  a * b
# print(sum(3, 6))


# name = "Tom"
#
#
# def say_hi():
#     global name
#     name = "Bob"  # изменяем значение глобальной переменной
#     print("Hello", name)
#
#
# def say_bye():
#     print("Good bye", name)
#
#
# say_hi()  # Hello Bob
# say_bye()