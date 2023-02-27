"======================Функции====================================="

# функция   -   именованнный блок кода, который принимает аргументы и возвращает результат

func = lambda num1, num2: num1 + num2
res = func(5, 10)
print(res)    # 15

# lambda - ключевое слово, для создания анонимной функции

def func_2(num1, num2):
    return num1 + num2
print(func_2)   # <function func_2 at 0x7f75bfa6e0e0>

res = func_2(10, 5)
print(res)

def calc(num1, num2, oper):
    """
    oper - строка, с операцией для вычислений
    "+" - сложение
    "-" - вычитание
    """

    if oper == '+':
        return num1 + num2
    if oper == '-':
        return num1 - num2
    if oper == '*':
        return num1 * num2
    if oper == '/':
        return num1 / num2
    
print(calc(10, 12, '+'))  # 22
print(calc(20, 8, '-'))   # 12
print(calc(10, 2, '*'))   # 20
print(calc(15, 5, '/'))   # 3.0

print(calc(15, 23, '5'))  # None

def my_len(obj):
    "Возвращает длину обьекта"
    count = 0
    for i in obj:
        count += 1
    return count

print(my_len([1,2,3,4,5]))   # 5

def super_len(obj):
    try:
        return my_len(obj)
    except:
        return my_len(str(obj))

print(super_len([1,2,3,4]))  # 4
print(super_len(1234567))    # 7
print(super_len(None))       # 4 ('None')


"=====================================DRY============================="

# DRY  -  don't repeat yourself  (не повторяйся)

# представим, что у нас нет функции len

str_ = "Hello World"
count = 0
for i in str_:
    count += 1
# count - длина строки str_

list_ = [1,2,3,4,4,56,5,7,8]
count = 0
for i in list_:
    count += 1
# count - длина списка list_

def len_(obj):
    count = 0
    for i in obj:
        count += 1
    return count

str_ = 'Hello world'
count = len_(str_)

list_ = [1,2,3,4,4,56,5,7,8]
count = len_(list_)


"==============Аргументы и Параметры==========================="

# Параметры  -  локальные переменные, значения которым мы задаем при вызове функции
# Аргументы - значения, которые мы задаем параметрам при вызове функции

# Обьяснение локальности:

def func(parameter):
    local_var = 5
    print(locals())
    # {'parameter': 6, 'local_var': 5}

func(6)
# print(local_var) NameError
# print(parameter) NameError



"=====================Виды параметров=================="

#  1. Обязательные
#  2. Необязательные 

#  2.1  с дефолтным значением ( по умолчанию)
#  2.2 args (arguments)
#  2.3 kwargs  (key word arguments)

def func(a):
    print(a)

# func()
# TypeError: func() missing 1 required positional argument: 'a'

def func(a, b='default'):
    print(a, b)

func('hello') # 'hello' 'default' () {}
func('hello', 100) # 'hello' 100 () {}

def func(a, b='default', *args):
    print(a, b, args)

func('hello', 100, 84, 23, 'world')
# 'hello' 100 (84, 23, 'world') {}

def func(a, b='default', *args, **kwargs):
    # args  -  tuple, куда попадут все позиционные аргументы, которые не попали по позиции
    # kwargs  -  dict, куда попадут все именованные аргументы, которые не попали по имени
    print(a, b, args, kwargs)

func('hello', 100, 10, 20, 30, key1='value1', key2=500)
# 'hello' 100 (10, 20, 30) {'key1': 'value1', 'key2': 500}



'             Нельзя одно по позиции а другие именнованно:   '

# func('hello', a=100)
# TypeError: func() got multiple values for argument 'a'


"===========Виды аргументов=============="

# позционные    (по порядку)
# именнованные  (по имени параметров)

def func2(a, b):
    print(f'a={a}, b={b}')

func2(10, 20) # позиционно
# a=10, b=20

func2(a=30, b=40) # именнованно
#  a=30, b=40

func2(b=50, a=60)
#  a=60, b=50

"==========================Звездочки==========================="

#   *  - распаковка  (итерация)

list1 = [1,2,3,4]  
list2 = [*list1]  
print(list2)   
# [1, 2, 3, 4]

list1 = 'hello'  
list2 = [*list1]  
print(list2) 
# ['h', 'e', 'l', 'l', 'o']


#   **  - распаковка ключ-значение

dict1 = {'a':1, 'b':2}
list3 = [*dict1]
print(list3)    #  ['a', 'b']

dict1 = {'a':1, 'b':2}
dict3 = {**dict1}
print(dict3)    #  {'a': 1, 'b': 2}






