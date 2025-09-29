


# /////// First Ex ///////
#
# name = input("Какое твое имя? ")
#
# print("Мое имя:", name)
#
# age = int(input(f"А сколько тебе лет {name}? "))
#
# print("Мне:", age)
#
# ///////          ////////

# /////// Second Ex ///////

# nam1 = int(input("Введите первое число: "))
# print(f"Ваше первое число: {nam1}")
#
# nam2 = int(input("Введите второе число: "))
# print(f"Ваше второе число: {nam2}")
#
# print("\n","///// Начало операции на числа /////")
#
# print(f"Сумма чисел: {nam1+nam2}")
# print(f"Сумма умножение: {nam1*nam2}")
# print(f"Сумма вычитание : {nam1-nam2}")
# print(f"Сумма деление: {nam1/nam2}")
#
# print("///// Конец операции на числа /////")

# ///////          ////////

# /////// КЛАССЫ ///////

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

# /////// Second Ex ///////

# class BankAccount:
#     def __init__(self,name,balance):
#         self.accounNam = name
#         self.balance = balance
#
#     def print_info(self):
#         print(f"Твой номер ячейки: {self.accounNam}\tТвой баланс: {self.balance}")
#
#
#     def add(self):
#         new = int(input("Введите сколько хотите добавить: "))
#         print(f"Твой номер ячейки: {self.accounNam}\tТвой баланс: {new + self.balance}")
#
#     def withdraw(self):
#         new = int(input("Введите сколько хотите вычесть: "))
#         if self.balance > new:
#             print(f"Твой номер ячейки: {self.accounNam}\tТвой баланс: {self.balance - new}")
#         else:
#             print("На вашем аккаунте не достаточно средств")
#
#
# acc = BankAccount(1,100)
#
# acc.print_info()
# acc.add()
# acc.withdraw()


# ///////          ////////

