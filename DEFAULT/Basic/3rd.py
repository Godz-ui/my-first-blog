# lam = lambda a,: a * a
#
# print(lam(5))

# def do_operation(a, b, operation):
#     result = operation(a, b)
#     print(f"result = {result}")
#
#
# do_operation(5, 4, lambda a, b: a + b)
# do_operation(5, 4, lambda a, b: a * b)
# do_operation(5, 4, lambda a, b: (a * b ) * b)

# def select_operation(choice):
#     if choice == 1:
#         return lambda a, b: a + b
#     elif choice == 2:
#         return lambda a, b: a - b
#     elif choice == 3:
#         return lambda a,b,h: round((a + b) / 2 ) * h
#     else:
#         return lambda a, b: a * b
#
#
# operation = select_operation(1)
# print(operation(10, 6))
#
# operation = select_operation(2)
# print(operation(10, 6))
#
# operation = select_operation(3)
# print(operation(10, 6, 4))
#
# operation = select_operation(4)
# print(operation(10, 6))


# name = "Tom"
#
#
# def say_hi():
#     global name, age
#     name = "Bob"
#     age = 21
#     print(f"hello, my name is - {name} and my age is - {age}")
#
#
# def say_bye():
#     print("Good bye", name)
#
#
# say_hi()
# say_bye()


# def outer():
#     name = 'Tom'
#     print(f"name: {name}")
#
#     def say_hi():
#         nonlocal name
#         name = "Bob"
#         print(f"hello, my name is - {name} ")
#
#     say_hi()
#
#     def say_bye():
#         global name
#         name= "Mr.S"
#         print(f"Good Bye: {name}")
#     say_bye()
#
#
#     def repeat_bye():
#         print(f"Repeat Good Bye: {name}")
#     repeat_bye()
#
#
# outer()
# ////////   First Ex   //////////
while True:
    First = int(input("Введите первое число:"))
    Second = int(input("Введите второе число:"))
    # sums= First + Second
    print("Сумма обоих чисел: ", First + Second)


    push = input("Нажмите Y или y для завершения программы:")
    if (push == "Y" or push == "y"): break
    print("The operation is continuing")
print("The operation is over")
# ////////              //////////
# while True:2
#     # вводим первое число
#     num1 = int(input("Введите первое число: "))
#     # вводим второе число
#     num2 = int(input("Введите второе число: "))
#     # вычисление суммы чисел
#     print("Сумма чисел: ", num1+num2 )
#     # запрос на выход из цикла
#     str = input ("Нажмите Y или y для завершения программы: ")
#     # выходим из цикла
#     if (str =="Y" or str =="y"):  break



# ////////   Second Ex   //////////






# ////////              //////////
# class Person:
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#
# tom = Person("Tom", 22)
#
# print(tom.name)
# print(tom.age)
#
# tom.age = 37
# print(tom.age)