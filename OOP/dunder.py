# dunder (double underscore) - методы у которых 2 __ в начале и в конце

# магия в том, что мы их не вызываем напрямую

class A:
    def __new__(cls):
        print('__NEW__')
        return super().__new__(cls)
    
    def __init__(self):
        print('__INIT__')
        pass

A()
# __NEW__
# __INIT__

# __new__, __init__ - вызываются при создании обьекта

# print(dir(object))

# print(dir(A))
# print(A.__dir__(A))

# __eq__ ==
# __ge__ >=
# __gt__ >
# __le__ <=
# __lt__ <
# __ne__ !=
" Это то как работают операторы сравнения под капотом"
" Можно использовать их в своих классах переопределив их"
" Также и работает всё, напр, +, - в int и тд"
# __add__ +
# __sub__ -



# __str__  -  str, print   (потому что в терминале строка)

'Все в питоне это Обьекты, поэтому dunder методы работают на них всех, при print и тд'

class A:
    pass
# __str__   str, print

print(A())
# <__main__.A object at 0x7f55bf757d30>

class A:
    def __str__(self) -> str:
        return 'Hello'

print(A())
# Hello

class A:
    def __init__(self, number):
        self.number = number

obj1 = A(5)
obj2 = A(5)

print(obj1 == obj2)  # False

class A:
    def __init__(self, number):
        self.number = number
        
    def __eq__(self, other):
        return self.number == other.number

obj1 = A(5)
obj2 = A(5)

print(obj1 == obj2)  # True
print(obj1.__eq__(obj2)) # True




print('Hello')   # Hello
print(str('Hello'))  # Hello
print(repr('Hello'))  # 'Hello'

class A:
    def __str__(self) -> str:
        return "A __STR__"
    
    def __repr__(self) -> str:
        return "A __REPR__"

print(A())
print(repr(A()))



