# # 12
# list1 = [1,2,3,4]
# list2 = [5,6,7,8]
# list1.extend(list2)
# x = 0
# for i in list1:
#     x += i
# print(x)

# 14
# list_ = [1, 2, 3]
# res = []
# for i in list_:
#     if list_.count(i)>1:
#         res.append(i)
# if len(res) > 0:
#     print('yes')
# else:
#     print('ERROR')


# 15
# list_ = []
# for i in range(54, 9184):
#     if i % 5 == 0:
#         list_.append(i)
# print(list_)

# 16
# list_ = [20, 10, 20, 1, 100]
# list_.sort()
# min_number = list_[0]
# print(min_number)

# 17
# tuples = [(), ('ram','15','8'), (), ('laxman', 'sita')]
# cleared_tuples = []
# for i in tuples:
#     if len(i) != 0:
#         cleared_tuples.append(i)
# print(cleared_tuples)

# 18
# x1 = input('Введите имя и фамилию: ')
# x2 = input('Введите имя и фамилию: ')
# x3 = input('Введите имя и фамилию: ')
# x4 = input('Введите имя и фамилию: ')
# x5 = input('Введите имя и фамилию: ')
# y1 = x1.split(' ')
# y2 = x2.split(' ')
# y3 = x3.split(' ')
# y4 = x4.split(' ')
# y5 = x5.split(' ')
# aaa = []
# aaa.append(y1[-1])
# aaa.append(y2[-1])
# aaa.append(y3[-1])
# aaa.append(y4[-1])
# aaa.append(y5[-1])
# aaa.sort()
# print(aaa)


# 19
# list_ = [8, 6, 8, 10, 8, 20, 10, 8, 8]
# number = 8
# x = list_.count(number)
# print(x)

# 20
# list_ = [1, 'abcd', 3, '1', 4, '2', 'xyz', 5, 'pqr', 7, 5, 12]
# ccc = []
# bbb = []
# for o in list_:
#     if type(o) == int:
#       ccc.append(o)
#     else:
#         bbb.append(o)
# ddd = []
# for i in bbb:
#     if i.isdigit():
#       ddd.append(int(i))
# ccc.extend(ddd)
# eee = len(ccc)
# fff = 0
# for i in range(eee):
#     fff = fff + ccc[i]
# print(fff)

# 21
# str_list = ['abc', 'xyz', 'aba', '1221']
# indexs = []
# for i in str_list:
#     if i[0] == i[-1]:
#         indexs.append(str_list.index(i))
# print(indexs)

# 22 !!!!!

# lists = [[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]
# sort_list = sorted(lists, key = len)

# if sort_list[0] == sort_list[-1]:
#     print(f'max_list {sort_list[-1]}')
#     print(f'min_list {None}')
# else:
#     print(f'max_list {sort_list[-1]}')
#     print(f'min_list {sort_list[0]}')


# lists = [[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]
# my_list=[]
# for i in lists:
#     if len(lists) <= 1:
#         my_list.append(len(i))  
#         bbb = my_list.index(max(my_list))
#         x=lists[bbb]
#     elif len(i) >= 0 and len(lists) > 1:
#         my_list.append(len(i))  
#         aaa = my_list.index(min(my_list))
#         bbb = my_list.index(max(my_list))
#         x=lists[bbb]
#         y=lists[aaa]
# if len(lists) <= 1:
#   print(f'max_list {x}')
#   print('min_list None')
# if len(x) == len(y):
#   print(f'max_list {x}')
#   print('min_list None')
# else:
#   print(f'max_list {x}')
#   print(f'min_list {y}')

# 23
# list_ = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']
# step = 3
# new_list = []
# for i in list_:
#   if list_.index(i) < step:
#     x = list_[list_.index(i)::step]
#     new_list.append(x)
# print(new_list)

# 24
# list_ = []
# size = 3
# for i in range(1, size + 1):
#   list_.append(list(range(1, size + 1)))
# print(list_)

# 25
# list_ = ['sun', 'flowers', 'rumor', 'stranger', 'adventure', 'architect', 'accompany', 'abandon', 'cartoon']
# res = []
# x = input()
# for i in list_:
#   if i[0] == x:
#     res.append(i)
# print(res)

# 26
# colors1 = ["red", "orange", "green", "blue", "white"]
# colors2 = ["black", "yellow", "green", "blue"]

# res = []
# res1 = []

# for color in colors1:
#     if color not in colors2:
#         res.append(color)

# for color in colors2:
#     if color not in colors1:
#         res1.append(color)

# print(res, res1)

# 27
# list1 = [1,2,3,4,5]
# list2 = [5,6,7,8,9]
# res = []
# for i in list1:
#     if i in list2:
#         res.append(i)
# if len(res)>0:
#   print("True")
# else:
#     print("False")
        

# 28
# list_ = [4, 6, 4, 3, 3, 8, 4, 3, 4, 3, 8, 8]
# res = []
# repeats = 3
# for i in list_:
#     if list_.count(i) >= repeats and i not in res:
#         res.append(i)
        
# print(res)


# 29
# list_ = [1, 2, 3]
# for x in list_:
#     for y in list_:
#         for z in list:
#             if x != y and y != z and x != z:  # x != y != z
#                 print((x, y, z))


#30
# list_ = []
# new_list = []
# K = 3
# for i in range(1, K + 1):
#   list_.append(0)
# for y in range(1, K + 1):
#   new_list.append(list_)
# print(new_list)

# Решение 2
# K = 3
# matrix = []

# for i in range(K):
#     matrix.append([])

#     for j in range(K):
#         matrix[i].append(0)

# print(matrix)

# 31
# colors = ["Red", "Green", "Blue", "White", "Black", "Yellow", "Orange"]
# list_ = []
# my_list=[]
# for i in colors:
#     list_.append(i[::-1])
# print(sorted(list_, key = len))

# 32

# list_ = [1,2,3,4,5,6,7,8,9,0]
# step = 2
# element = 'A'
# i = step

# while i <= len(list_):
#     list_.insert(i, element)
#     i = i + step + 1

# print(list_)

# Решение 2

# list_ = [1,2,3,4,5,6,7,8,9,0]
# n = 2
# x = 'A'
# result = []

# for st_idx in range(0, len(list_), n):

#     result.extend(list_[st_idx:st_idx+n])
#     result.append(x)

# result.pop()

# print(result)

# 33

# lists = [[1, 2, 3], [4, 5, 6], [10, 11, 12], [7, 8, 9]]
# max_ = max([x for x in lists], key = sum)
# print(max_)

# Решение 2
# lists = [[1, 2, 3], [4, 5, 6], [10, 11, 12], [7, 8, 9]]
# print(max(lists, key = sum))

# 34
# list_ = [10, 20, 30, 20, 20, 30, 40, 50, -20, 60, 60, -20, -20]
# res = []
# for i in list_:
#     if list_.count(i)>1 and i not in res:
#         res.append(i)
# print(res)


# 35
# chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
# merge_from = input()
# merge_to = input()
# # ['abcd', 'e', 'f', 'g']

# for let in chars:
#     for let2 in chars[1:]:
#         if merge_from == let and merge_to == let2:
#             index1 = chars.index(let)
#             index2 = chars.index(let2)

# chars[index1: index2 + 1] = ["".join(chars[index1: index2 + 1])]
# print(chars)



'==================================================DICTIONARY========================================================'

# 36
# a = {'a': 10, 'b': 9, 'c': 3}
# result = 1
# for x, y in a.items():
#     result *= y
# print(result)




