# password = input('Введите пароль: ')
# if password.isdigit() and len(password) >= 8:
#     print('Ваш пароль сохранен')
# elif len(password) >= 8 and not password.isdigit():
#     print('Ваш пароль должен хранить только числа')
# elif password.isdigit() and not len(password) >= 8:
#     print('Ваш пароль должен содержать не менее 8 символов')
# else:
#     print('Ваш пароль должен хранить только числа\nВаш пароль должен содержать не менее 8 символов')


# a, b, c = input('Введите свои баллы по математике, английскому языку и литературе через запятую:').split(', ')
# Ball = round((int(a) + int(b) + int(c)) / 3, 1)
# if Ball > 69:
#     print(f'Вы допущены к экзаменам. Ваш средний балл составляет {Ball}')
# else:
#     print(f'У Вас недопуск к экзаменам. Ваш средний балл составляет {Ball}')

# Вариант №2
# a, b, c = [int(x) for x in input('Введите свои баллы по математике, английскому языку и литературе через запятую:').split(', ')]
# Ball = round(a + b + c) / 3, 1)
# if Ball > 69:
#     print(f'Вы допущены к экзаменам. Ваш средний балл составляет {Ball}')
# else:
#     print(f'У Вас недопуск к экзаменам. Ваш средний балл составляет {Ball}')


# polzov = input('Ваш выбор: ')
# xxx = ['камень ', 'ножницы ', 'бумага ']
# import random
# compik = random.choice(xxx)
# vyvod = print('Выбор компьютера:' + ' ' + compik)
# K = xxx[0]
# N = xxx[1]
# B = xxx[2]
# if compik == K and polzov == 'камень':
#     print('Ничья')
# elif compik == K and polzov == 'ножницы':
#     print('Вы проиграли')
# elif compik == K and polzov == 'бумага':
#     print('Вы выиграли')
# elif compik == N and polzov == 'ножницы':
#     print('Ничья')
# elif compik == N and polzov == 'бумага':
#     print('Вы проиграли')
# elif compik == N and polzov == 'камень':
#     print('Вы выиграли')
# elif compik == B and polzov == 'бумага':
#     print('Ничья')
# elif compik == B and polzov == 'камень':
#     print('Вы проиграли')
# elif compik == B and polzov == 'ножницы':
#     print('Вы выиграли')
# else:
#     print('Ошибка. Вводите верно и без пробелов')

# polzov = input('Ваш выбор: ')
# xxx = [' камень ', ' ножницы ', ' бумага ']
# import random
# compik = random.choice(xxx)
# vyvod = print('Выбор компьютера:' + compik)
# if polzov == 'камень' and compik == ' камень ':
#     print('Ничья')
# elif polzov == 'ножницы' and compik == ' камень ':
#     print('Вы проиграли')
# elif polzov == 'бумага' and compik == ' камень ':
#     print('Вы выиграли')
# elif polzov == 'ножницы' and compik == ' ножницы ':
#     print('Ничья')
# elif polzov == 'бумага' and compik == ' ножницы ':
#     print('Вы проиграли')
# elif polzov == 'камень' and compik == ' ножницы ':
#     print('Вы выиграли')
# elif polzov == 'бумага' and compik == ' бумага ':
#     print('Ничья')
# elif polzov == 'камень' and compik == ' бумага ':
#     print('Вы проиграли')
# elif polzov == 'ножницы' and compik == ' бумага ':
#     print('Вы выиграли')

polzov = input('Ваш выбор: ')
xxx = ['камень ', 'ножницы ', 'бумага ']
import random
compik = random.choice(xxx)
vyvod = print('Выбор компьютера:' + ' ' + compik)
if compik == 'камень ' and polzov == 'камень':
    print('Ничья')
elif compik == 'камень ' and polzov == 'ножницы':
    print('Вы проиграли!')
elif compik == 'камень ' and polzov == 'бумага':
    print('Вы выиграли!')
elif compik == 'ножницы ' and polzov == 'ножницы':
    print('Ничья')
elif compik == 'ножницы ' and polzov == 'бумага':
    print('Вы проиграли!')
elif compik == 'ножницы ' and polzov == 'камень':
    print('Вы выиграли!')
elif compik == 'бумага ' and polzov == 'бумага':
    print('Ничья')
elif compik == 'бумага ' and polzov == 'камень':
    print('Вы проиграли!')
elif compik == 'бумага ' and polzov == 'ножницы':
    print('Вы выиграли!')
else:
    print('Ошибка. Вводите верно и без пробелов')






