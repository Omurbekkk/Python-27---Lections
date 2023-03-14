"======================Миксины==================="

# 1. Миксины - это классы, которые будут использоваться для наследования
# Но от миксинов не создаются обькты

# 2. Миксины - классы-примеси, которые служат для расширения функционала класса


# От миксинов нельзся создавать обьекты, поскольку миксины - несамостоятельные классы

# При наследовании миксины должны идти в первую очередь

class WalkMixin:
    def walk(self):
        print('я могу ходить')

class SwimMixin:
    def swim(self):
        print('я могу плыть')

class FlyMixin:
    def fly(self):
        print('я могу летать')

class Human(WalkMixin, SwimMixin):
    name = 'человек'

    def talk(self):
        print('я могу говорить')

class Fish(SwimMixin):
    name = 'рыба'

class Exocoetidae(SwimMixin, FlyMixin):
    name = 'летучая рыба'

class Duck(WalkMixin, SwimMixin, FlyMixin):
    name = 'утка'

obj_ = Exocoetidae()
obj_.swim()
obj_.fly()
# я могу плыть
# я могу летать

obj_ = Duck()
obj_.walk()
obj_.swim()
obj_.fly()
# я могу ходить
# я могу плыть
# я могу летать


obj_ = Duck()
print(hasattr(obj_, 'fly'))   #  True

obj_ = Human()
print(hasattr(obj_, 'fly'))   #  False


print(getattr(obj_, 'walk'))
# <bound method WalkMixin.walk of <__main__.Human object at 0x7f2624357e20>>

method = getattr(obj_, 'walk')
method()
# я могу ходить

print(getattr(obj_, 'name'))
# человек


objects = [Human(), Fish(), Exocoetidae(), Duck()]

for obj in objects:
#     print(obj.name)
# человек
# рыба
# летучая рыба
# утка

    attrs = ['fly', 'swim', 'walk', 'talk']
    for attr in attrs:
        if hasattr(obj, attr):
            method = getattr(obj, attr)
            method()
# я могу плыть
# я могу ходить
# я могу говорить
# я могу плыть
# я могу летать
# я могу плыть
# я могу летать
# я могу плыть
# я могу ходить


obj = Human()
setattr(obj, 'new_attr', 'hello_world')
# print(dir(obj))
# ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'name', 'new_attr', 'swim', 'talk', 'walk']

print(obj.new_attr)
# hello_world

print(obj.name)
# человек


# hasattr - функция, которая принимает обьект и название аттрибута. Возвращает True, если у обьекта есть такой аттрибут

# getattr - функция, которая принимает обьект и название аттрибута. Возвращает значение аттрибута

# setattr - функция, которая принимает обьект, название нового аттрибута и значение нового аттрибута. Добавляет в обьект новый аттрибут или перезаписывает одноименный аттрибут





    


