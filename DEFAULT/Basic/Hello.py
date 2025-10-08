#name = input("Введите ваше имя: ")
#print("Привет,", name)
#print(2 + 3)
#print("hello")
# if (5 > 2):
    # print("hello")
'''
    Вывод на консоль
    сообщения Hello World
'''
from email.utils import encode_rfc2231

from django.db.models.expressions import result
from django.template.defaultfilters import yesno

# print("Hello World")
# print ("Full name:", "Даниил", "Аслан")
#name = "Tom"
#print(name)
#name = "Bob"
#print(name)
#isMarried = False
#print(isMarried)
#isAlive = True
#print(isAlive)
#age = 21
#print("Возраст:", age)
#count = 15
#print("Количество:", count)
#a = 0b11
#b = 0b1011
#c = 0b100001
#print(a)
#print(b)
#print(c)
#a = 0o7
#b = 0o11
#c = 0o17
#print(a)
#print(b)
#print(c)
#a = 0x0A
#b = 0xFF
#c = 0xA1
#print(a)
#print(b)
#print(c)
#height = 1.68
#pi = 3.14
#weight = 68.
#print(height)
#print(pi)
#print(weight)
#x = 3.9e3
#print(x)
#x = 3.9e-3
#print(x)
#complexNumber = 1+2j
#print(complexNumber)
#message = "Hello World!"
#print(message)
#name = 'Tom '
#print(name)
#text = ("Laudate omnes gentes laudate" "Magnificat in secula")
#print(text)

#text = '''Laudate omnes gentes laudate
#Magnificat in secula
#Et anima mea laudate
#Magnificat in secula
#print(text)
#text = "Message:\n\"Hello World\""
#print(text)
#path = "C:\python\name.txt"
#print(path)
#path = r"C:\python\name.txt"
#print(path)
#userName = "Tom"
#userAge = 37
#user = f"name: {userName} age: {userAge}"
#print(user)
#userId = "abc"
#print(userId)

#userId = 234
#print(userId)
#userId = "abc"
#print(type(userId))

#userId = 234
#print(type(userId))
#print("Hello World", end=" ")
#print("Hello METANIT.COM", end=" ")
#print("Hello Python")
#name = input("Bведите свое имя: ")
#print(f"Ваше имя: {name}")
#name = input("Your name: ")
#age = input("Your age: ")
#print(f"Name: {name} Age: {age}")
#print(6+2)
#print(6-2)
#print(6*2)
#print(6/2)
#print(7/2)
#print(7//2)
#print(6 ** 2)
#print(6 ** 2)
#print(7 % 2)
#number = 3+ 4 * 5 ** 2+7
#print(number)
#number = (3+4) * ( 5 ** 2 + 7)
#print (number)
#number = 10
#number += 5
#print(number)
#number -= 3
#print(number)
#number *= 4
#print(number)
#first_number = 2.0001
#second_number = 5
#third_number = first_number / second_number
#print(third_number)
#print(2.0001+0.1)
#first_number = 2.0001
#second_number = 0.1
#first_number = first_number + second_number
#print(round(first_number))
#first_number = 2.0001
#second_number = 0.1
#first_number = first_number + second_number
#print(round(first_number, 4))
#print(round(2.49))
#print(round(2.51))
#print(round(2.5))
#print(round(3.5))
#print(round(2.554, 2))
#print(round(2.5551, 2))
#print(round(2.554999, 2))
#print(round(2.499, 2))
#print(round(2.545, 2))
#print(round(2.555, 2))
#print(round(2.565, 2))
#print(round(2.575, 2))

#print(round(2.655, 2))
#print(round(2.665, 2))
#print(round(2.675, 2))
#number = 5
#print(f"number = {number:0b}")
#number = 0b101
#print(f"number = {number:0b}")
#print(f"number = {number}")
#number1 = 1
#number2 = 2
#number3 = 3
#number4 = 4
#number5 = 5
#number6 = 6
#x1 = 2
#y1 = 5
#z1 = x1 & y1
#print(f":z1 = {z1}")

#x2 = 4
#y2 = 5
#z2 = x2 & y2
#print(f"z2 = {z2}")
#print(f"z2 = {z2:0b}")
#x1 = 2
#y1 = 5
#z1 = x1|y1
#print(f"z1 = {z1}")
#print(f"z1 = {z1:0b}")
#x2 = 4
#y2 = 5
#z2 = x2 | y2
#print(f"z2 = {z2}")
#print(f"z2 = {z2:0b}")
#x = 9
#y = 5
#z = x ^ y
#print(f"z = {z}")
#print(f"z = {z:0b}")
#x = 45
#key = 102
#encrypt = x ^ key
#print(f"Зашифрованное число: {encrypt}")
#decrypt = encrypt ^ key
#print(f"Расшифрованное число: {decrypt}")
#x = 9
#y = 5
#x = x ^ y
#y = x ^ y
#x = x ^ y

#print(f"x = {x}")
#print(f"y = {y}")
#x = 5
#y = ~x;
#print(f"y: {y}")
#a = 16
#b = 2
#c = a << b
#print(c)

#d = a >> b
#print(d)
#a = 22
#b = 2
#c = a << b
#print(c)

#d = a >> b
#print(d)
#a = 5
#b = 6
#result = 5 == 6
#print(result)
#print(a != b)
#print(a > b)
#print(a < b)

#bool1 = True
#bool2 = False
#print(bool1 == bool2)
#age = 22
#weight = 58
#result = age > 21 and weight == 58
#print(result)
#result = 4 and "w"
#print(result)

#result = 0 and "w"
#print(result)
#age = 22
#isMarried = False
#result = age > 21 or isMarried
#print(result)
#result = 4 or "w"
#print(result)

#result = 0 or "w"
#print(result)
#age = 22
#isMarried = False
#print(not age > 21)
#print(not isMarried)
#print(not 4)
#print(not 0)
#message = "hello world!"
#hello = "hello"
#print(hello in message)

#gold = "gold"
#print(gold in message)


