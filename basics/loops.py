'======================Циклы=================='

# Цикл - блок кода, который отрабатывается несколько раз

# for - цикл, который работает с итерируемыми обьектами. Цикл заканчивает свою работу, когда он доходит до последнего эдлемента в итерируемом обьекте
# while - цикл, который работает до тех пор, пока условие верное

list1 = ['hello', 10, True, [1,2,3]]
for x in list1:
    print(x)
print(x)           #  ВЫВЕДЕТ ПОСЛЕДНИЙ ЭЛЕМЕНТ

for x in list1[::-1]:
    print(x)


string1 = 'hello world'
for letter in string1:
    print(letter)

# while True:
#     print('hello')

# i = 1
# while i != 10:
#     print('hello', i)
#     i = i + 1          #  до ПРИНТА или после не имеет отношение на колво Хелло НО имеет значение, напр для i после Хело

y = 0
while y:
    print('hello')
    y = y + 1             # вообще ни разу не отработает, потому что False

# А  for   только для итерируемых и посл

"=========================Ключевые слова в циклах==============="
# break  - полностью останавливает цикл
# continue   - переход к следующей итерации

for i in range(10):
    if i == 3:
        break
    print(i)
# 0
# 1
# 2

for i in range(10):
    if i == 3:
        continue
    print(i)
# 1
# 2
# 4
# 5
# 6
# 7
# 8
# 9

list11 = [1,2,1,1,1,1,1,1,1,1,23]
# с помощью метод remove удалите все еддиницы в списке 
# for i in list11:
#     if i == 1:
#         print(list11.remove(1))
# for i in list11:
#     if i == 1:
#         print(list11.remove(1))
# print(list11)

while 1 in list11:
    list11.remove(1)
print(list11)



