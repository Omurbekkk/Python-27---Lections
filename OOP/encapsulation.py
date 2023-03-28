# class A:
#     attr1 = 'public'
#     _attr2 = 'protected'
#     __attr3 = 'private'

# print(A.attr1)
# print(A._attr2)
# # print(A.__attr3)
# print(A._A__attr3)
# # public
# # protected
# # # AttributeError: type object 'A' has no attribute '__attr3'. Did you mean: '_A__attr3'?
# # private





# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.__age = age

#     def get_age(self):
#         return self.__age
    
#     # Не трогайте, но можно через set_age:

#     def set_age(self, new_age):
#         if new_age > 0 and new_age < 120:
#             self.__age = new_age
#         else:
#             raise Exception('Invalid age')

# obj = Person('Nastya', 12)
# print(obj.name)
# print(obj.get_age())
# obj.set_age(45)
# print(obj.get_age())
# obj.set_age(-123)   # Exception: Invalid age

# # obj.age = -45
# # print(obj.age)





# class A:
#     @property
#     def Hello(self):
#         return 5

# obj = A()
# print(obj.Hello)  # 5
# obj.Hello = 7     # AttributeError: can't set attribute 'Hello'
# ' property делают функцию аттрибутом '










