# x = int(input('inp1 '))
# y = int(input('inp2 '))
# z = int(input('inp3 '))
# r_1 = x * y
# r_2 = r_1 % z
# print(r_2)

# x = input('inp1 ')
# y = input('inp2 ')
# z = input('inp3 ')
# r_1 = int(x) * int(y)
# r_2 = r_1 % int(z)
# print(r_2)

# r_1 = int(input('inp1 ')) * int(input('inp2 '))
# r_2 = r_1 % int(input('inp3 '))
# print(r_2)


# inp1 = int(input())
# inp2 = int(input())
# inp3 = int(input())
# r_1 = inp1 * inp2
# r_2 = r_1 % inp3
# print(r_2)

# radius = 5
# import math
# pi_ = round(math.pi, 2)
# p =  int(pi_) * radius
# s = int(pi_) * radius ** 2
# print(p, s)

# radius = 5
# import math
# pi_ = round(math.pi, 2)
# p =  2 * pi_ * radius
# s = pi_ * radius ** 2
# print(p, s)

# first, second, third = 1, 2, 3
# first = second; third = first; second = third


# first = 1
# second = 2
# third = 3

# first, second, third = second, third, first
# print(first, second, third)

# num1 = 4
# num2 = 2
# num3 = 3.0
# x = num1 % num2
# y = x * num3
# print(x, y)

# print('string4'.startswith('str'))   # True

# name = input('Your name: ')
# hello = 'Hello, {}!'.format(name)
# print(hello, 'How are you?')
# Your name: Omurbek
# Hello, Omurbek! How are you?


# s = 'cow loves good milk'
# y = s.replace('o', 'e', 2)
# print(y)

# string1 = "America" 
# string2 = "Japan"
# print(string1[0] + string2[0] + string1[int(int(len(string1))//2)] + string2[int(int(len(string2))//2)] + string1[-1] + string2[-1])


# string = 'helooooo'
# print(string.replace(string[int(5-int(len(string))):int(6-int(len(string)))], 'K', 1))
# print(string[:5] + 'K' + string[6:])

# title = 'Пирог'
# price = 35
# print('Название:', title, ',', 'цена:', price)

# year = int(input())
# if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
#     print('YES')
# else:
#     print('NO')

# count = '0'
# number = input()
# if number.isdigit():
#     print(count.replace('0', number))

# count = 0
# number = input()
# if number.isdigit():
#     count = count+int(number)
# print(count)

# n = input()
# if n.endswith('1') and n != '11':
#     print(f'На лугу пасется {n} корова')
# elif n.endswith('2') and n != '12' or n.endswith('3') and n != '13' or n.endswith('4') and n != '14':
#     print(f'На лугу пасется {n} коровы')
# else:
#     print(f'На лугу пасется {n} коров')

# x1 = int(input())
# y1 = int(input())
# x2 = int(input())
# y2 = int(input())
# if x1 == x2 and y1 != y2 or y1 == y2 and x1 != x2:
#     print('YES')
# else:
#     print('NO')

# ХОД ЛАДЬИ
# x1 = int(input())
# y1 = int(input())
# x2 = int(input())
# y2 = int(input())
# if x1 == x2 and y1 != y2 and 1 <= x1 <= 8 and 1 <= x2 <= 8 and 1 <= y1 <= 8 and 1 <= y2 <= 8 or y1 == y2 and x1 != x2 and 1 <= x1 <= 8 and 1 <= x2 <= 8 and 1 <= y1 <= 8 and 1 <= y2 <= 8:
#     print('YES')
# else:
#     print('NO')

# ХОД СЛОНА
# x1 = int(input())
# y1 = int(input())
# x2 = int(input())
# y2 = int(input())
# if 1 <= x2 <= 8 and 1 <= y2 <= 8 and x2 == y2 and x1 != x2 and y1 != y2: 
#     print('YES')
# else:
#     print('NO')g

# print(chr(69))

# num = int(input())
# res = chr(num)
# if res.isalpha():
#     print(f'Это буква "{res}"')
# else:
#     print(f'Это не буква, а символ "{res}"')

# a = int(input())
# b = int(input())
# c = int(input())
# if (a + b > c) and (c + b > a) and (a + c > b):
#     if (a*a + b*b == c*c) or (a*a + c*c == b*b) or (c*c + b*b == a*a):
#         print("rectangular")
#     elif (a*a + b*b < c*c) or (a*a + c*c < b*b) or (c*c + b*b < a*a):
#         print("obtuse")
#     elif (a*a + b*b > c*c) or (a*a + c*c > b*b) or (c*c + b*b > a*a):
#         print("acute")
# else:
#     print("impossible")

