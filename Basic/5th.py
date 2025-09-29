# /////// First Ex ///////
# ///////          ////////

# nam1 = int(input("Введите первое число: "))
# nam2 = int(input("Введите второе число: "))
#
#
# if nam1 > nam2:
#     print("Первое число больше второго")
# elif nam1 < nam2:
#     print("Первое число меньше второго")
# else:
#     print("Числа равны")


# /////// First Ex ///////

# first_name = input("Введите имя: ")
# last_name = input("Введите фамилию: ")
# print("Вас зовут :", first_name, last_name)

# ///////          ////////



# /////// Second Ex ///////


# for list in range(1,21):
#     input(f"{list} Введите вашу фамилию: ")






# ///////          ////////



# /////// Third Ex ///////

# for list in range(1, 16):
#     print(list, end=" ")

# ///////          ////////



# /////// Fourth Ex ///////

# for list in range(0, 51, 2):
#     print(list, end=" ")

# for list in range(0, 51, 2):
#     print(int(list / 2 ), end=" ")

# ///////          ////////



# /////// Fifth Ex ///////

# nam = int(input("Введи число: "))
#
# if nam % 2 == 0:
#     print(f"Число |{nam}| четное")
#
# else:
#     print(f"Число |{nam}| не четное")

# ///////          ////////



# /////// КЛАССЫ ///////

# class Person:
#
#     def __init__(self, name):
#         self.__name = name
#
#     @property
#     def name(self):
#         return self.__name
#
#     def display_info(self):
#         print(f"Name: {self.__name} ")
#
#
# class Employee(Person):
#
#     def work(self):
#         print(f"{self.name} works")
#
#
# tom = Employee("Tom")
# print(tom.name)
# tom.display_info()
# tom.work()


class Employee:

    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name

    def work(self):
        print(f"{self.name} works")


class Student:

    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name

    def study(self):
        print(f"{self.name} studies")


class WorkingStudent(Employee, Student):
    pass


tom = WorkingStudent("Daniil")
tom.work()
tom.study()