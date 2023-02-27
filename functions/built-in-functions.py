'=================================Встроенные функции=============================='

# enumrate - функция, которая принимает последовательность и возвращает генератор, где элементы генераторы tuple ...

string1 = 'hello'
enum = enumerate(string1)
print(enum)   # <enumerate object at 0x7f7f226f9c80>

print(list(enum))
#  [(0, 'h'), (1, 'e'), (2, 'l'), (3, 'l'), (4, 'o')]

string2 = 'world'
enum = enumerate(string2, 5)
print(list(enum))
#  [(5, 'w'), (6, 'o'), (7, 'r'), (8, 'l'), (9, 'd')]

# Дан список с числами, умножьте на 2 все числа под нечетным индексом, потом умножьте на 3 все числа под индексом, кратным 3

list1 = [1,4,78,3,7,0,4,2,7]

for i in range(len(list1)):
    element = list1[i]
    if i % 2: # i %2 != 0
        list1[i] = element * 2
    if i % 3  == 0:  # i % 3
        list1[i] = element * 3

print(list1)  # [3, 8, 78, 9, 7, 0, 12, 4, 7]


list1 = [1,4,78,3,7,0,4,2,7]
for i, element in enumerate(list1):
    if i % 2:
        list1[i] = element * 2
    if i % 3  == 0:
        list1[i] = element * 3

print(list1)  # [3, 8, 78, 9, 7, 0, 12, 4, 7]


# создайте словарь, где ключом будет порядковый номер буквы в алфавите, а значением буква в алфавите

list1 = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
x = enumerate(list1, 1)
print(dict(x))

string1 = 'abcdefghijk'
print(dict(enumerate(string1,1)))


# zip

list1 = [1,2,3,4,5]
list2 = 'abcdef'
list3 = [0.5, 0.3,0.6]

print(list(zip(list1, list2,list3)))
#  [(1, 'a', 0.5), (2, 'b', 0.3), (3, 'c', 0.6)]


'===================Функция высшего порядка================'

# это функция, которая:
#              принимает в аргумент другую функцию
#              возвращает функцию
#              создает внутри функцию
#              вызывает внутри функцию


# map  -  принимает в аргументы функцию и итерируемый обьект. Возвращает генератор, в котором все элементы - рузультат принимаемой функции, в которую передали элементы последовательности

mapped = map(int, ['1','2','3'])
print(mapped)
# <map object at 0x7f3266c7ff10>

print(list(mapped))
#  [1, 2, 3]

# дан список с числами, создайте новый список где эелемент +1

list1 = [1,2,3,4,5]
def x(i):
    return i+1
res = list(map(lambda i:i+1, list1))
print(res)

 # filter   -  принимает в аргументы функцию и итерируемый обьект. Возвращает генератор, в котором элементы из последовательности прошедшие фильтр (функция вернула True)

list1 = [-3,7,0,34,-23,435,10]
def is_positive(i):
    return i > 0
print(list(filter(is_positive, list1)))
#  [7, 34, 435, 10]

print(list(filter(lambda i: i>0, list1)))
#  [7, 34, 435, 10]


# дан список со строками, оставьте только те строки, которые начинают с большой буквы

list1 = ['Hello', 'wORLD', 'MAKERS']
print(list(filter(lambda i: i[0].isupper(), list1)))


#  reduce  -  функция, которая импортируется из модуля functools.
#  тоже принимает функцию и итерируемый обьект.
#  возвращает 1 результат

from functools import reduce

list1 = [1,2,3,4,5,65,8]

def mul(x,y):
    return x*y

res = reduce(mul, list1)
print(res)
#  62400 = 1*2*3*4*5*65*8


string = 'hello'
print(reduce(lambda x,y: x+'$'+y, string))
# h$e$l$l$o
# x='h', y='e' -> 'h$e'
# x='h$e', y='l' -> 'h$e$l'
# x='h$e$l', y='l' -> 'h$e$l$l'
# x='h$e$l$l', y='o' -> 'h$e$l$l$o'


' ====================>     ОБЯЗАТЕЛЬНО 2 ЭЛЕМЕНТА !!!!!!!'




list1 = ['hello','world','makers','bootcamp','aaa']
# bootcamp
print(reduce(
    lambda x, y: x if len(x) > len(y) else y,
    list1))

def func(x,y):
    if len(x) > len(y):
        return x
    return y
print(reduce(func, list1))


# Мое решение:

list_ = ['hello', 'world', 'makers', 'bootcamp']

def func(a,b):
    if len(a)>len(b):
        return a
    return b

res = reduce(func, list_)
print(res)















