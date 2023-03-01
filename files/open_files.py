'==========================Пакеты и Модули==========================='

# module - любой файл с расширением   .py

# import test
# print(test.a)

# from test import a
# print(a)

# package - набор модулей (в папке обязательно должен быть __init__.py)

# from package.test1 import hello
# hello()
# from package.test2 import list_

'1. Разобрать всё'



'==================Работа с файлами====================='

# open - функция, которая позволяет открывать файлы в определенном режиме

# r - read  (только для чтения)
# w - write (только для перезаписи, каждый раз при открытии очищает файл)
# a - append (только для дозаписи, добавляется в конец файла)

# x - создает файл, но если файл уже есть - ошибка
# b - бинарный вид


"============Read=============="

file = open('test.txt')

# если такого файла нет - выйдет ошибка
# если не указать режим - откроется в режиме чтения

print(dir(file))

'read', 'readable', 'readline', 'readlines'

print('readable', file.readable()) # True
print('writable', file.writable()) # False

print(file.read())  #  считывает от начала до конца
print(file.read())  #  пустая строка, если вызвать 2ой раз, потому что каретка в конце файла

file.seek(0) # Перенос каретки в начало (на индекс 0)
print(file.read())  # считывает от начала до конца

file.seek(5)
print(file.read()) # считываем от 5-го индекса до конца

file.seek(0)
print(file.read(5))  # Hello   считываем 5 символов
print(file.read()) # '\nWorld\nMakers\n'  считываем от 5 до конца

file.seek(0)
print(file.readline()) # 'Hello\n' считывает до \n
print(file.readline()) # 'World\n' считывает до \n

file.seek(0)
print(file.readlines()) # ['Hello\n', 'World\n', 'Makers\n']

file.seek(10)
print(file.tell()) # 10

file.read()  # считывает до конца (на 19 индекс)
print(file.tell()) # 19

print(file.name) # test.txt
print(file.closed) # False
file.close()  #  !важно закрывать файлы
print(file.closed) # True

'==========Write============'

file = open('new_file.txt', 'w')
#  если файла нет - создает
#  если есть - очищает

print('readable', file.readable()) # False
print('writable', file.writable()) # True

file.write('Hello\n')
file.write('Makers\n')

file.writelines(['Hello', 'World'])
# Hello
# Makers
# HelloWorld

file.writelines(['\nNew\nLine'])
# Hello
# Makers
# HelloWorld
# New
# Line

file.seek(0)
file.write('AAA')
# AAAlo
# Makers
# HelloWorld
# New
# Line

file.close()

'=============Append================'

file = open('new_file2.txt', 'a')

# если файла нет - создается новый

print('readable', file.readable()) # False
print('writable', file.writable()) # True

file.write('Hello')
# дозапись идет в конец файла (старые данные не удаляются)

file.seek(0)
file.write('New')
# все равно в конец

file.close()

'========Контекстный Менеджер========='

# try:
#     file = ('aaa.txt', 'w')
#     file.read()
# finally:
#     file.close()

with open('test.txt') as f:
    f.read()
#  файл закрывается
    print(f.closed)  # False

print(f.closed)  # True

















