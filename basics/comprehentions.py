"==========================Compehentions========================="

# генератор, с помощью которого можно создавать последовательность используя цикл for

list1 = [i for i in range(1, 11)]
# print(list1) [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# результат for элемент in последовательность
# результат for элемент in последовательность if фильтр

comprehention = (i for i in range(1, 11))
print(comprehention)
# <generator object <genexpr> at 0x7feb55242490>
# генератор - итерируемый обьект, который не хранит в себе полностью все элементы последовательности, а генерирует их когда требуется

# print(next(comprehention)) 
# print(next(comprehention))
# print(next(comprehention))
# print(next(comprehention))
# print(next(comprehention))
# print(next(comprehention))
# print(next(comprehention))
# print(next(comprehention))
# print(next(comprehention))
# print(next(comprehention))
# print(next(comprehention)) # StopIteration


# next - это функция, которая принимает в себя генератор, запрашивает след элемент и возвращает его

comprehention = (i for i in range(1, 4))
print(list(comprehention))  # [1, 2, 3]
print(list(comprehention))  # []

"============================Синтаксический сахар====================="

# list comprehentiion
list_compr = [i for i in 'hello']
print(list_compr)
# ['h', 'e', 'l', 'l', 'o']

# dict comprehention
dict_compr = {i:str(i) for i in range(1,11)}
print(dict_compr)
# {1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: '10'}


# фильтр

string = 'HelLo WorlD'
res = [i for i in string if i.islower()]
print(res)    #  ['e', 'l', 'o', 'o', 'r', 'l']
res = []
for i in string:
    if i.islower():
        res.append(i)
print(res)
# ['e', 'l', 'o', 'o', 'r', 'l']



list111 = [i for i in range(2, 11, 2)]
print(list111)

list222 = list(range(1,11))
res2 = [i for i in list222 if i%2 == 0]
print(res2)


# Решение
list1 = [i*100 for i in range(1, 11)]
print(list1)





# Решения

# 1
res = []
listttt = ['hello']
for i in range(5):
    for i in listttt:
        res.append(i)
print(res)

# 2
listttt = ['hello']
res = [i for i in range(5) for i in listttt]
print(res)




users = ['test1', 'test2', 'test3']

# Решения
# 1
# res = ['Hello'+' ' + i for i in users]
# print(res)

# #2
# res = [f'Hello {i}' for i in users]
# print(res)

# Решения
# 1
res = []
x = range(2, 7)
for i in x:
    res.append(list(range(1, i)))
print(res)

# 2
res2 = [list(range(1,i)) for i in range(2,7)]
print(res2)



dict1 = {
    "a": {"aaa1":1},
    "b": {"aaa2":2},
    "c": {"aaa3":3}
}
# res = {"a":1, "b":2, "c":3}
res = {}
for key, value in dict1.items():
    for x, y in value.items():
        res[key] = y
print(res)

res333 = {y:key for key, value in dict1.items() for x, y in value.items()}
print(res333)

res333 = {value:key for key, y in dict1.items() for x, value in y.items()}
print(res333)



# Решение

res5 = {i:list(range(1,i+1)) for i in range(1,6)}
print(res5)

# set comprehension

set_comprehension = {x for x in range(10)}
print({1, True, 'hello', 10, 1})
# {1, 'hello', 10}
# 1 == True
# 0 == False




