class Person:     #  мы взяли из класса object    и потом переобределяем методы   напр __init__
    # аттрибуты - переменные внутри класса
    arms = 2
    legs = 2
    name = 'OMUR'

    
    def __init__(self, name):
        # __init__  -  dunder метод, который добавляет в обьект self аттрибуты, которые отличаются у разных обьектов
        self.name = name


    # функции внутри класса - методы
    def walk(self):
        #  ссылка на обьект, у которого мы вызываем данный метод
        print(self)
        print('я хожу')

    # walk = lambda: print('я хожу')

# Зачем нам наш класс
# Создание обьектов

# int('10')

# person1 =Person()
# print(person1)   #  <__main__.Person object at 0x7f6d22557b80>  P1 это обьект P


# person1 =Person()
# print(type(person1))  #  <class '__main__.Person'>

# print(__name__) # __main__

# print(dir(person1))

# print(person1.arms)  # 2

# print(person1.walk())

# person1 = Person()
# Person.walk(person1)
# person1.walk()   #  -  будем писать так

# p1 = Person()
# p2 = Person()
# p3 = Person()
# print(p1.name, p2.name, p3.name)  # OMUR OMUR OMUR



person1 =Person('Nastya')
person2 = Person('OMUR')
print(person1.name, person2.name)   #  Nastya OMUR      С помощью __init__ можно ...



# Аттрибуты класса и аттрибуты обьекта класса

class A:
    var1 = 'переменная класса'

    def __init__(self):
        self.var2 = 'переменная обьекта'

print(dir(A))

obj = A()         #   Пример Беки
print(dir(obj))  
# здесь есть и аттрибуты класса и еще свои    Сначала он перенимает все атирибуты своего класса а потом свои аттрибуты      А у класса только свои

print(A.var1)  #  'переменная класса'

print(obj.var1)   # 'переменная класса'
print(obj.var2)   # 'переменная обьекта'

# У обьекта можно вызвать и var1   и   var2


# Давайте воспринимать class  как шаблон

