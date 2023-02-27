# num1 = int(input('Введите первое число: '))
# num2 = int(input('Введите второе число: '))
# znak = input('Выберите операцию из следующих (+ - * / % ** //)  : ')
# if znak == '+':
#     o = num1 + num2
#     print(f'Ответ: {o}')
# elif znak == '-':
#     o = num1 - num2
#     print(f'Ответ: {o}')
# elif znak == '*':
#     o = num1 * num2
#     print(f'Ответ: {o}')
# elif znak == '/':
#     o = num1 / num2
#     print(f'Ответ: {o}')
# elif znak == '//':
#     o = num1 // num2
#     print(f'Ответ: {o}')
# elif znak == '%':
#     o = num1 % num2
#     print(f'Ответ: {o}')
# elif znak == '**':
#     o = num1 ** num2
#     print(f'Ответ: {o}')
# else:
#     print('Ответ: Данной операции нет в системе')


# num1 = int(input('Введите первое число: '))
# num2 = int(input('Введите второе число: '))
# znak = input('Выберите операцию из следующих (+ - * / % ** //)  : ')
# if znak == '+':
#     try:
#         o = num1 + num2
#         print(f'Ответ: {o}')
#     except ValueError:
#         print('Вы ввели не число')
# elif znak == '-':
#     try:
#         o = num1 - num2
#         print(f'Ответ: {o}')
#     except ValueError:
#         print('Вы ввели не число')
# elif znak == '*':
#     try:
#         o = num1 * num2
#         print(f'Ответ: {o}')
#     except ValueError:
#         print('Вы ввели не число')
# elif znak == '/':
#     try:
#         o = num1 / num2
#         print(f'Ответ: {o}')
#     except ValueError:
#         print('Вы ввели не число')
#     except ZeroDivisionError:
#         print("Нельзя делить на 0")
# elif znak == '//':
#     try:
#         o = num1 // num2
#         print(f'Ответ: {o}')
#     except ValueError:
#         print('Вы ввели не число')
#     except ZeroDivisionError:
#         print("Нельзя делить на 0")
# elif znak == '%':
#     try:
#         o = num1 % num2
#         print(f'Ответ: {o}')
#     except ValueError:
#         print('Вы ввели не число')
# elif znak == '**':
#     try:
#         o = num1 ** num2
#         print(f'Ответ: {o}')
#     except ValueError:
#         print('Вы ввели не число')
# else:
#     print('Ответ: Данной операции нет в системе')

# from decimal import Decimal
# num1 = Decimal(input('Введите первое число: '))
# num2 = Decimal(input('Введите второе число: '))
# znak = input('Выберите операцию из следующих (+ - * / % ** //)  : ')
# if znak == '+':
#     try:
#         o = num1 + num2
#         print(f'Ответ: {o}')
#     except ValueError:
#         print('Вы ввели не число')
# elif znak == '-':
#     try:
#         o = num1 - num2
#         print(f'Ответ: {o}')
#     except ValueError:
#         print('Вы ввели не число')
# elif znak == '*':
#     try:
#         o = num1 * num2
#         print(f'Ответ: {o}')
#     except ValueError:
#         print('Вы ввели не число')
# elif znak == '/':
#     try:
#         o = num1 / num2
#         print(f'Ответ: {o}')
#     except ValueError:
#         print('Вы ввели не число')
#     except ZeroDivisionError:
#         print("Нельзя делить на 0")
# elif znak == '//':
#     try:
#         o = num1 // num2
#         print(f'Ответ: {o}')
#     except ValueError:
#         print('Вы ввели не число')
#     except ZeroDivisionError:
#         print("Нельзя делить на 0")
# elif znak == '%':
#     try:
#         o = num1 % num2
#         print(f'Ответ: {o}')
#     except ValueError:
#         print('Вы ввели не число')
# elif znak == '**':
#     try:
#         o = num1 ** num2
#         print(f'Ответ: {o}')
#     except ValueError:
#         print('Вы ввели не число')
# else:
#     print('Ответ: Данной операции нет в системе')


# from decimal import Decimal
# try:
#     num1 = Decimal(input('Введите первое число: '))
#     num2 = Decimal(input('Введите второе число: '))
# except:
#     print('Вы ввели не число')
# else:
#     znak = input('Выберите операцию из следующих (+ - * / % ** //)  : ')
#     if znak == '+':
#         try:
#             o = num1 + num2
#             print(f'Ответ: {o}')
#         except ValueError:
#             print('Вы ввели не число')
#     elif znak == '-':
#         try:
#             o = num1 - num2
#             print(f'Ответ: {o}')
#         except ValueError:
#             print('Вы ввели не число')
#     elif znak == '*':
#         try:
#             o = num1 * num2
#             print(f'Ответ: {o}')
#         except ValueError:
#             print('Вы ввели не число')
#     elif znak == '/':
#         try:
#             o = num1 / num2
#             print(f'Ответ: {o}')
#         except ValueError:
#             print('Вы ввели не число')
#         except ZeroDivisionError:
#             print("Нельзя делить на 0")
#     elif znak == '//':
#         try:
#             o = num1 // num2
#             print(f'Ответ: {o}')
#         except ValueError:
#             print('Вы ввели не число')
#         except ZeroDivisionError:
#             print("Нельзя делить на 0")
#     elif znak == '%':
#         try:
#             o = num1 % num2
#             print(f'Ответ: {o}')
#         except ValueError:
#             print('Вы ввели не число')
#     elif znak == '**':
#         try:
#             o = num1 ** num2
#             print(f'Ответ: {o}')
#         except ValueError:
#             print('Вы ввели не число')
#     else:
#         print('Ответ: Данной операции нет в системе')














    
