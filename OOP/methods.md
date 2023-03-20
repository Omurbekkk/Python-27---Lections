# class/static/instance methods

> **instance методы** - это методы, которые первым аргументом принимают обьект от класса (instance, self). Используются они для работы с обьектом и его аттрибутами

```py
class A:
    def instance_method(self):
        print('метод обьекта')
        print('self', self)

obj = A()
obj.instance_method()
```

> **class methods** - это методы, которые первым аргументом принимают класс (cls). Используются они для работы с классом и его аттрибутами

```py
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
```

> для создания class метода, нужно использовать декоратор 'classmethod'



> **static methods** - методы, которые не взаимодействуют с обьектом и классом, но находится внутри класса (по принципу инкапсуляции (всё, что нужно для работы класса лежит внутри класса))




