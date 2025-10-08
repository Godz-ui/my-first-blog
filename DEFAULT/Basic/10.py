# /////// First Ex ///////
from django.template.defaultfilters import yesno


# class Phone:
#
#     def __init__(self, model, number):
#         self.model = model
#         self.number = number
#
#     def info(self):
#         print(f"Модель телефона: {self.model} и его номер: {self.number}")
#
#     def cell(self):
#         print(f"Идет звонок на {self.number}")
#
# Milard = Phone("Samsung", 98832)
#
# Milard.info()
#
# Milard.cell()
#
# Timur = Phone("Google Pixel", 98432)
# # phone = Phone("")
#
#
# Timur.info()
#
# Timur.cell()

# ///////          ////////



# /////// Second Ex ///////

# class Car:
#
#     def __init__(self, model, year):
#         self.model = model
#         self.year = year
#
#     def print(self):
#         print(f"Модель авто: {self.model}\nГод выпуска: {self.year}")
#
#
# car1 = Car('BMW', 1995)
#
# car1.print()

# ///////          ////////


# /////// Third Ex ///////

class Calc:

    def __init__(self, nam1 = "Введи первое число: ",
                 nam2 = 'Введи второе число: '):
        self.nam1 = int(input(nam1))
        self.nam2 = int(input(nam2))

    def pl(self):
        result = self.nam1 + self.nam2
        print(f"{self.nam1} + {self.nam2} = {result}")

    def mn(self):
        result = self.nam1 - self.nam2
        print(f"{self.nam1} - {self.nam2} = {result}")


    def pos(self):
        result = self.nam1 * self.nam2
        print(f"{self.nam1} * {self.nam2} = {result}")

    def neg(self):
        result =  self.nam1 / self.nam2
        return f"{self.nam1} / {self.nam2} = {result}"

    def cva(self, nam):
        self.nam = nam
        print (f"{self.nam} в квадрате = {self.nam * self.nam}")

    def cube(self, nam):
        self.nam = nam
        print (f"{self.nam} в кубе = {self.nam * self.nam * self.nam}")


ca = Calc()

ca.pl()
ca.mn()
ca.pos()
print(ca.neg())

# ca.cva()
# ca.cube()

# ///////          ////////