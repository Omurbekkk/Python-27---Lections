class A:
    def instance_method(self):
        print('метод обьекта')
        print('self', self)

obj = A()
obj.instance_method()
# метод обьекта
# self <__main__.A object at 0x7f5cd6957a90>
# когда мы вызываем метод у обьекта, то нам нужно передавать его в self, он передается автоматически


A.instance_method(obj)
# метод обьекта
# self <__main__.A object at 0x7fc7ccf57a90>
# когда мы вызываем метод у класса, то нам нужно передавать обьект




class A:
    @classmethod
    def class_method(cls):
        print('метод класса')
        print('cls', cls)

A.class_method()      
# метод класса
# cls <class '__main__.A'>
'Теперь пришел сам класс и не ругается потому что принимает в себя классы'


obj = A()
obj.class_method()
# метод класса
# cls <class '__main__.A'>
'все равно откуда вы будете вызывать classmethod (от обькта или класса), первым аргументом будет приходить класс'


# примеры

class C:
    counter = 0

    def __init__(self):
        # или __new__
        # обьект создается
        # для создания

        #C.counter += 1       первый вар

        self._inc_counter()

    def __del__(self):
        # обьект удаляется

        # C.counter -= 1      первый вар

        self._dec_counter()

# 'Так можно как в первом варианте, но лучше не обращаться напрямую к классу, а classmethod или super'

    @classmethod
    def _inc_counter(cls):
    # cls - class C
    # увеличиваем аттрибут класса counter на один
        cls.counter += 1

    @classmethod
    def _dec_counter(cls):
        cls.counter -= 1

obj1 = C()
obj2 = C()
obj3 = C()
obj4 = C()
print(C.counter)  # 4
del obj1
print(C.counter)  # 3




class Pizza:
    def __init__(self, radius, *ingridients):
        self.r = radius
        self.i = ingridients
    
    def cook(self):
        print(f'Пиццы размером {self.r*2}')
        print(f'Ингридиенты: {self.i}')
    
    @classmethod
    def four_cheese(cls, radius):
        pizza = cls(radius, 'Сыр 1', 'Сыр 2', 'Сыр 3', 'Сыр 4')
        # pizza2 = Pizza(10, 'Сыр 1', 'Сыр 2', 'Сыр 3', 'Сыр 4')
        return pizza

pizza1 = Pizza(15, 'Сыр', 'Колбаса')
pizza1.cook()
# Пиццы размером 30
# Ингридиенты: ('Сыр', 'Колбаса')

pizza2 = Pizza(10, 'Сыр 1', 'Сыр 2', 'Сыр 3', 'Сыр 4')
pizza2.cook()
# Пиццы размером 20
# Ингридиенты: ('Сыр 1', 'Сыр 2', 'Сыр 3', 'Сыр 4')


pizza3 = Pizza.four_cheese(10)
pizza3.cook()
# Пиццы размером 20
# Ингридиенты: ('Сыр 1', 'Сыр 2', 'Сыр 3', 'Сыр 4')

pizza4 = Pizza.four_cheese(20)
pizza4.cook()
# Пиццы размером 40
# Ингридиенты: ('Сыр 1', 'Сыр 2', 'Сыр 3', 'Сыр 4')


class A:
    @staticmethod
    def static_method():
        print('статик метод')
    
obj = A()
obj.static_method()  # статик метод


class Cylinder:
    def __init__(self, diameter, height):
        self.di = diameter
        self.hi = height
        self.area = Cylinder.get_area(diameter, height)

    @staticmethod
    def get_area(di, hi):
        from math import pi
        circle_area = pi * di**2 / 4
        side_area = pi * di * hi
        return circle_area*2 + side_area
    
c1 = Cylinder(3, 10)
print(c1.area)  # 108.38494654884785

print(Cylinder.get_area(3, 10))  # 108.38494654884785

'''
Мы не создали обьект, но получили нужные нам расчеты
Можно и вытащить за класс, но чтобы использовать внутри - статик
'''


'''
Пример проекта парсинга Насти
Например при чистке данных
Можно создать статик методы
Для парсинга создала классы и обьекты
А другие вещи, которые не касаются обьектов или классов, обернуть в статик
'''

