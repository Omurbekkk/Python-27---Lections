# 1

# a = {'x': 1, 'y': 2, 'z': 1}
# for i in a:
#     print(i)
#     break


# Задание 10 и 22

# dict_ = {'a': None, 'b': 1, 'c': 2, 'd': None, 'e': 3}
# b = {}
# for x, y in  dict_.items():
#     if y == None:
#         b[x] = y
# print(b)

# dict_ = {'a': None, 'b': 1, 'c': 2, 'd': None, 'e': 3}
# for x, y in  list(dict_.items()):
#     if y != None:
#         dict_.pop(x)
# print(dict_)

#     Амина:    Можно сделать копию

# Проблема связана с тем, что вы пытаетесь модифицировать словарь, по элементам которого итерируетесь.
# В условиях вашего кода это не проблема. Но вы должны сначала прежде чем начнётся цикл с удалениями) взять список пар элементов из вашего словаря.
# products.items() возвращает не список, а итератор по элементам словаря. Само собой этот итератор ломается как только вы удаляете из словаря первый элемент.
# Но если этот итератор до первого удаления полностью превратить в список, то удалять потом можно что хотите.

# Или так:

# new_products_dict = {k: v for k, v in products.items() if v['g_1'] != 0}


#15

# ingredients = {"cыр чеддар","грибы", "соус","шпинат"}
# ingredients.add('помидор')
# ingredients.discard('колбаса')
# ingredients.remove('шпинат')
# ingredients.add('базилик')
# ingredients.remove('cыр чеддар')
# ingredients.add('сыр моцарелла')
# print(ingredients)


# employees = [
#   {'name': 'Jack', 'salary': 10000, 'overTime': 4},
#   {'name': 'Tom', 'salary': 15000, 'overTime': 3},
#   {'name': 'Jessica', 'salary': 20000, 'overTime': 9},
#   {'name': 'Helen', 'salary': 25000, 'overTime': 2},
#   {'name': 'Peter', 'salary': 30000, 'overTime': 7}
# ]
# new_emp = []
# def func17(a):
#     for i in a:
#         x = i['overTime']*200
#         y = i['salary'] + x
#         new_emp.append(dict([('name', i['name']), ('salary', y)]))
#     return new_emp


# print(func17(employees))
            

# ccc = [{'name': 'Pack', 'salary': 10000, 'overTime': 6}, {'name': 'Xom', 'salary': 45400, 'overTime': 5}, {'name': 'Sessica', 'salary': 543500, 'overTime': 3}, {'name': 'Pelen', 'salary': 250445, 'overTime': 2}, {'name': 'Qeter', 'salary': 30450, 'overTime': 0}]

# print(func17(ccc))

# bbb = [{'name': 'Pack', 'salary': 10000, 'overTime': 6}, {'name': 'Xom', 'salary': 45400, 'overTime': 5}, {'name': 'Sessica', 'salary': 543500, 'overTime': 3}, {'name': 'Pelen', 'salary': 250445, 'overTime': 2}, {'name': 'Qeter', 'salary': 30450, 'overTime': 0}]

# print(func17(bbb))


# students = [
#   {'student': 'Jack', 'marks': 43},
#   {'student': 'Tom', 'marks': 92}, 
#   {'student': 'Helen', 'marks': 85}, 
#   {'student': 'Peter', 'marks': 58},
#   {'student': 'Jessica', 'marks': 78}
# ]

# def func19(a):
#     for i in a:
#         for k, v in i.items():
#             a.sort(key=v, reverse=True)
#     return a
# print(func19(students))


# inp1 = input()
# inp2 = input()
# if type(inp1) != int or type(inp2) != int:
#     inp1


# 14

# dict_ = {'Timur': {'history': 90, 'math': 95, 'literature': 91},
 
# 'Olga': {'history': 92, 'math': 96, 'literature': 81},
 
#  'Nik': {'history': 84, 'math': 85, 'literature': 87}}

# new_dict = {k:a for k,v in dict_.items() for a,b in v.items() if b == max(v.values())}

# print(new_dict)



'''
Множества нельзя анхэшибл
d = {{'a':1}, 3, 3}
print(v)
'''


"""
def func(a=2,b=3):
    print(a+b)

func()
"""


# def func(a=2,b=3):
#     return a+b

# print(func(5,6))


products = [
  {
    'title': 'Samsung S10', 
    'price': 800, 
    'count': 6, 
    'category': 'samsung'},
  {
    'title': 'iPhone 13 Pro', 
    'price': 1200, 
    'count': 9, 
    'category': 'apple'},
  {
    'title': 'Xiaomi Mi 10', 
    'price': 500, 
    'count': 2, 
    'category': 'xiaomi'},
  {
    'title': 'Samsung S9', 
    'price': 600, 
    'count': 4, 
    'category': 'samsung'},
  {
    'title': 'iPhone 11', 
    'price': 850, 
    'count': 1, 
    'category': 'apple'}
]

xxx = {'title': 'SFSDffsdf'}, {'title': 'SFSDffsdf'}, {'title': 'SFSDffsdf'}


res = []

def func20(x,y):
    for i in x:
        if str(y) in i['title']:
            res.append(i)
    return res
# print(func20(products, 'i'))
print(func20(xxx, 'SF'))





def foo():
    var = 'переменная foo'
    print('переменная в foo: ', var)
    def bar():
        var = 'переменная bar'
    return var
    bar()
foo()
# print('переменная в foo: ', var)



