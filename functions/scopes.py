'====================Области видимости / пространства имен=============='

# LEGB - (local, enclosed, global, build-in)

# build-in  -   встроенное пространство
    # print, input, str, sum

# global  -  глобальное пространство  (наш файл)
    # чтобы посмотреть все глобальные переменные  -  globals

# a = 5
# b = 7
# print(globals())

# enclosed  -  замкнутое пространство, которое находиться между двумя пространствами
# локальное пространство, внутри которого есть еще одно локальное пространство

var = 'глобальная'
def func():
    var = 'замкнутая'
    def inner_func():
        var = 'локальная'
        def inner_inner_func():
            var = 'супер локальная переменная'
            print(var)
        inner_inner_func()
        print(var)
    inner_func()
    print(var)
func()
print(var)


"=======>            func()         #    Можно вызывать ?!      !!!!!!!!!!!!!"


"====================>Разбор на доске,  Разбор того примера"
"Он ищет сначала в своем"
"Потом идет к предыдущей"
"Если находит то останавливается"
"Разобрать когда поменяли местами принты и вызов функции"

'''
print и тд -  это переменные?!   !!!!!!
Получается на компе это print = <func>

ключевые слова
'''


# local - локальное пространство  (внутри функции)

a = 'hello'

def func(a, b):
    print('GLOBAL', globals())  # GLOBAL {'a': 'hello', 'func': <function func at 0x7f721e32e0e0>}
    print('LOCAL', locals())  # LOCAL {'a': 10, 'b': 50}

func(10, 50)

num1 = 10

def func():
    print(num1)

func()


counter = 0

def increase_counter():
    global counter
    counter += 1
    print(counter)

increase_counter()
increase_counter()
increase_counter()
increase_counter()     #  4
#        print(counter)   4      !!!!!!


def count(i):
    counter = 0
    
    def increase_counter():
        nonlocal counter
        counter += 1
        print(counter)

    for _ in range(i):
        increase_counter()

count(10)

def func():
    a = 10
    def inner_f():
        a = 15
        def inner_inner():
            nonlocal a
            a += 1
        inner_inner()
        print(a)
    inner_f()
func()




        







