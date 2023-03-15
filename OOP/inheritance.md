# Наследование

> Принцип ООП, где мы можем унаследовать, переопределять и использовать, менять все аттрибуты и методы родительского класса

```py
class A:   # A(object)
    def method(self):
        print('Метод в классе А')

obj_a = A()
obj_a.method()
# Метод в классе А

class B(A):
    pass

obj_b = B()
obj_b.method()
# Метод в классе А
```
> класс А - родительский
> класс В - дочерний

## Переопределение
> это когда мы создаем метод или атрибут с таким же названием, как и в родительских классах

```py
class C(A):
    def method(self):
        print('Метод в классе C')

obj_c = C()
obj_b.method()
# Метод в классе C
```

## Виды наследование
* **одиночное**  (когда один родитель)
* **множественное** (когда несколько родителей)

* многоуровневые (когда у родителей есть родитель)
* иерархическое (когда у каждого есть только один родитель, но у родителей может быть много детей)
* гибридное (совмещение разных видов наследование)

## Проблемы множественного наследования
1. Проблема ромба (решенная с помощью MRO (с версии 2.3))
> MRO - method resolution order (простраивает порядок для поиска аттрибутов)

```py
class A:
    pass
class B:
    pass
class C(A, B):
    pass

# до MRO
[C, A, object, C, B, object]

# после MRO
[C, A, B, object]
```

2. Проблема перекрестного наследования (не решенная, возникает когда невозможно построить приоритет родителей)

```py
# перекрестное наследование
class A:
    pass

class B:
    pass

class C(A, B):
    pass

class D(B, A):
    pass

class E(C, D):
    pass
# TypeError: Cannot create a consistent method resolution
# order (MRO) for bases A, B
```


