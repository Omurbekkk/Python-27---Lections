"==========================LIST========================="

# списки -  это изменяемый, итерируемый, индексируемый и упорядоченный тип данных, предназначенный для хранения элементов в строгом порядке.

list1 = [1, 3.5, 'hello', [1, 2, 3], (1, 2), None, True]
#   Можно хранить любой тип данных

list1[0]  # 10
list1[3]  # [1, 2, 3]

list1[3][-1] # 3               !!!!!!!!!

list1 [-1] # False

list2 = list('hello')
print(list2)    # ['h', 'e', 'l', 'l', 'o']

# Функция list() преращает в список из отдельных каждых элементов этого аргумента. 
# Только то что можно разделить по элементам

# print(list(range(3,10,2))) # [3, 5, 7, 9]
print(list(range(3,10,1))) # [3, 4, 5, 6, 7, 8, 9]

# Функция range  (начало, конец ДО, шаг)    как срез 
# Сочетание   функций  LIST    и    RANGE

"================== Изменяемость ==============================="

string = 'hello'
res = string.upper()
print(string)   # 'hello'
print(res)  # 'Hello'


list1 = []
list1.append(1)
list1.append(2)
list1.append(3)
print(list1)    # [1, 2, 3]

"============================= МЕТОДЫ списков ======================="

# append - метод, который добавляет элемент в конец списка

list1 = []
list1.append('hello')
list1.append(500)
list1.append([1,2,3])
print(list1)   # ['hello', 500, [1, 2, 3]]

# remove - это метод, который удаляет элемент из списка по значению, но только первого вхождения этого элемента.   Выдаст ошибку ValieError, если такого  элемента нет в списке.

list2 = ['hello', 500, 'world', 1000, 'hello', 500]
list2.remove('hello')
print(list2)  # [500, 'world', 1000, 'hello', 500]

# Удаляет только первый нашедший элемент  !!!!

# pop  -   метод, который удаляет элемент из списка по индексу, если  этого индекса нет, выдаст ошибку IndexError

list3 = [10, 20, 30, 40, 50]
list3.pop()
print(list3) # [10, 20, 30, 40]
list3.pop(1)
print(list3) # [10, 30, 40]      !!!!!!!!!

# Также метод POP возвращяет удаленный элемент
list4 = [10, 20, 30, 40, 50]
popa4 = list4.pop(0)
print(list4)   # [20, 30, 40, 50]
print(popa4)   # 10

# list5 = []
# list5.pop()
# IndexError: pop from empty list

# insert  -  метод, который ДОБАВЛЯЕТ элемент в список по индексу

list5 = [1,2,3,4]
list5.insert(0, 'hello')
print(list5)   # ['hello', 1, 2, 3, 4]

#                                                        Выведите список с числами в обратном порядке

# list6 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# list6.insert(0, list6.pop())
# list6.insert(1, list6.pop())
# list6.insert(2, list6.pop())
# list6.insert(3, list6.pop())
# list6.insert(4, list6.pop())
# list6.insert(5, list6.pop())
# list6.insert(6, list6.pop())
# list6.insert(7, list6.pop())
# list6.insert(8, list6.pop())
# print(list6)              


#                   list6 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#                   list6 = list(range(1,11))
#                   print(list6[::-1])
#                   list1.reverse()
#                   print(list.reverse(list6))                       !!!!!!

# print(dir(list))

# Метод count

# list1 = [1, 2, 3, 4, 5, 6, 1, 2 ,3]
# list1.count(1)   # 2

# list2 = ['hello', 'hello']
# list1.count('hello')   # 3
# list1.count('l')   # 0


list6 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list6.insert(0, list6.pop())
list6.insert(1, list6.pop())
list6.insert(2, list6.pop())
list6.insert(3, list6.pop())
list6.insert(4, list6.pop())
list6.insert(5, list6.pop())
list6.insert(6, list6.pop())
list6.insert(7, list6.pop())
list6.insert(8, list6.pop())
print(list6)  

#  ПОЛУЧИЛОСЬ


# copy   -   возвращает копию списка

# extend - ...


#   SORT    REVERS     из ГИТА   и COPY   и   EXTEND                         !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!








