# class Song:
    # def __init__(self, title, author, year): 
    #     self.title = title
    #     self.author = author
    #     self.year = year
#     def show_title(self):
#         return f'Название этой песни {self.title}'

#     def show_author(self):
#         return f'Автор этой песни {self.author}'
    
#     def show_year(self):
#         return f'Эта песня вышла в {self.year} году'
    


# song = Song('omur', 'dos', '2345')
# print(song.show_title())
# print(song.show_author())
# print(song.show_year())



# class Circle:
#     pi = 3.14
#     color = 'Синий'
#     def __init__(self, radius):
#         self.radius = radius
#     def get_area(self):
#         return self.pi * self.radius**2

# circle = Circle(2)
# # print(circle.radius)
# Circle.color = 'несиний'
# print(circle.color)
# print(circle.get_area())



# class BankAccount:
#     def __init__(self): 
#        self.balance = 0
    
#     def withdraw(self, som): 
#        self.balance -= som 
#        print('Ваш баланс:', self.balance, 'сом')
    
#     def deposit(self, som): 
#        self.balance += som 
#        print('Ваш баланс:', self.balance, 'сом')

# account = BankAccount()
# account.deposit(1000)
# account.withdraw(500)


# class Taxi:
#     def __init__(self, name, cost, cost_km): 
#         self.name = name
#         self.cost = cost
#         self.cost_km = cost_km
#     def get_total_cost(self, km):
#         res = self.cost + (self.cost_km*km)
#         return f'Такси {self.name}, стоимость поездки: {res} сом'


# taxi1 = Taxi('Namba',10, 5)
# taxi2 = Taxi('Yandex', 20, 10)
# taxi3 = Taxi('Jorgo', 30, 15)
# print(taxi1.get_total_cost(10)) 
# print(taxi2.get_total_cost(6)) 
# print(taxi3.get_total_cost(14))


# class Phone:
#     def __init__(self, name, last_name, phone): 
#         self.name = name
#         self.last_name = last_name
#         self.phone = phone
#     def get_info(self):
#         print(f'Контакт: {self.name} {self.last_name}, телефон: {self.phone}')


# contact = Phone('omur', 'dos', '+12345')
# contact.get_info()

# class Salary:
#     percent = 8
#     def __init__(self, salary, experience):
#         self.salary = salary
#         self.experience = experience
#     def count_percent(self):
#         res = self.salary * Salary.percent/100  * self.experience
#         return res 

# obj = Salary(10000, 10)
# print(obj.count_percent())




# from datetime import datetime, timedelta

# dt_now = datetime.now()
# print(dt_now.year)                 # 2023


# td_object =timedelta(days=0, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0)
# td_object
# print(timedelta(days=365))

# import datetime                               #Импорт модуля
# x = datetime.datetime.now()                   #Вызов метода now из класса datetime
# print(x.year)                    #2023        #Вывод на экран значения текущего года
# print(x.strftime("%A"))          # Monday     #Отображение на экране значения текущего дня


# class Nobel:
#     def __init__(self, category, year, winner):
#         self. category = category
#         self.year = year
#         self.winner = winner
#     def get_year(self):
#         import datetime
#         x = datetime.datetime.now()
#         res = x.year - self.year
#         return f'выиграл {res} лет назад'

# winner1 = Nobel("Литература", 1971, "Пабло Неруда") 
# print(winner1.category, winner1.year, winner1.winner) 
# print(winner1.get_year())

  
# winner2 = Nobel("Литература", 1994, "Кэндзабуро Оэ") 
# print(winner2.category, winner2.year, winner2.winner) 
# print(winner2.get_year())

# n = 0
# for i in range(1,11):
#     r = f'{n}*{i}={n*i}'
#     print(r)


# class Math:
#     def __init__(self, number):
#         self.number = number
#     def get_factorial(self):
#         r = 1
#         for n in range(1, self.number+1):
#             r *= n
#         return r
#     def get_sum(self):
#         rr = 0
#         for n in str(self.number):
#             rr += int(n)
#         return rr
#     def get_mul_table(self):
#         n = self.number
#         res = []
#         for i in range(1,11):
#             rrr = f'{n}x{i}={n*i}'
#             res.append(rrr+'\n')
#         return ''.join(res).rstrip()

# obj_ = Math(0)
# print(obj_.get_factorial())
# print(obj_.get_sum())
# print(obj_.get_mul_table())


# class ToDo:
#     instances = {}
#     def __init__(self, a):
#         self.a = a
#     def give_priority(self, priority):
#         ToDo.instances[priority] = self.a
#         return ToDo.instances
#     def list_of_tasks(self):
#         res = sorted(ToDo.instances.items())
#         return res

# obj_1 = ToDo('сходить в кино')
# obj_2 = ToDo('сделать домашку')
# obj_3 = ToDo('выгулять собаку')
# print(obj_2.give_priority(2))
# print(obj_1.give_priority(1))
# print(obj_3.give_priority(3))
# print(obj_3.list_of_tasks())

'''
class A:
    def __init__(self):
        self.a = 0
    def change_(self, n):
        a = n
    
obj_ = A()
obj_.change_(2)
print(obj_.a)            # 0


class spam:
    val = 1
    def __init__(self, n):
        val = 5

obj = spam(5)
print(obj.val)           # 1
'''




# 2
# class A:
#     def method1(self):
#        print('Основной функционал')

# class B(A):
#     def method1(self):
#         super().method1()
#         print('Дополнительный функционал')

# obj = B()
# obj.method1()


# class MyString(str):
#     def __init__(self, word):
#         self.word = word
    
#     def append(self, new_word):
#         self.word += new_word
#         return self.word

#     def __str__(self):
#         return self.word

#     def pop(self):
#         pop = self.word[-1]
#         self.word = self.word[:-1]
#         return pop
    
#     def __str__(self):
#         return self.word

# example = MyString('String') 
# example.append('hello')
# print(example)

# print(example.pop()) 
# print(example)


# Задание 8

# class CustomError(Exception):
#     def init(self, word):
#         self.word = word
#         # super().__init(word)
#     pass
# def check_letters(string):
#     if string.isupper():
#         return f'ВСЕ ОТЛИЧНО! {string}'
#     else:
#         raise capitals_error

# capitals_error = CustomError('ТОЛЬКО БОЛЬШИЕ БУКВЫ РАЗРЕШЕНЫ В ЭТОМ КОДЕ')
# print(check_letters("HELLO"))



# class CustomError(Exception): 
#    def init(self, message): 
#       self.message = message 
# capitals_error = CustomError('ТОЛЬКО БОЛЬШИЕ БУКВЫ РАЗРЕШЕНЫ В ЭТОМ КОДЕ')

# def check_letters(message1): 
#    if message1 == message1.upper(): 
#       return f'ВСЕ ОТЛИЧНО! {message1}' 
#    else: 
#       raise capitals_error 
   
# print(check_letters("HELLO"))






# Files N1

# with open('task1.txt', 'r') as file:
#     x = file.readlines()

# for i in x:
#     if int(i.rstrip()) < 6:
#         print(i)


# file = open('task1.txt') 
# for i in file.readlines(9): 
#     print(i) 
# file.close()





# class User:
#     def __init__(self, name, lastname, email):
#         self.name = name
#         self.lastname = lastname
#         self.email = email

#     @staticmethod
#     def validate_email(x):
#         return '@' in x
    
#     @classmethod
#     def create_user(cls, string):
#         list1 = string.split(',')
#         name = list1[0]
#         lastname = list1[1]
#         email = list1[2]
#         return cls(name, lastname, email)

#     def __str__(self):
#         if self.validate_email(self.email):
#             return f'{self.name}:{self.email}'
#         else:
#             return "email в неправильном формате"

# user1 = User.create_user('John, Snow, john@email.com')
# user2 = User.create_user('Maks, Sun, Maksemail.com')
# print(user1) 
# print(user2) 



# class User:

#     def create_user(self, string):
#         list1 = string.split(',')
#         self.name = list1[0]; self.lastname = list1[1]; self.email = list1[2]

#     def __str__(self):
#         if '@' in self.email:
#             return f'{self.name}:{self.email}'
#         else: return "email в неправильном формате"
    
# user1 = User(); user1.create_user('John, Snow, john@email.com'); print(user1)
# user2 = User(); user2.create_user('Maks, Sun, Maksemail.com'); print(user2)



# class Product:
#     base_price = 20000

#     def __init__(self, model, year, color):
#         self.model = model
#         self.year = year
#         self.color = color
    
#     def has_garantiya(self, year):
#         if year <= self.year + 2:
#             return 'Гарантия действительна'
#         else: return 'Ваша гарантия истекла'

#     @classmethod
#     def change_price(cls, rate):
#         cls.base_price += cls.base_price * rate//100
#         return cls.base_price
    
# obj = Product('A218', 2008, 'red') 
# obj.change_price(2)
# print(obj.has_garantiya(2010))
# print(obj.base_price)

# class MyDict(dict):

#     def __init__(self, d):
#         self.d = d

#     def get(self, key):
#         for k,v in self.d.items():
#             if key == k:
#                 return v
#             else:
#                 return 'Are you kidding?'

# obj_dict = MyDict({'1': 1, '2':2, '3':3}) 
# print(obj_dict.get('1'))


# class MoneyFmt:
#     def __init__(self, amount):
#         self.amount = amount
    
#     @staticmethod
#     def dollarize(float_num):
#         if float_num >= 0:
#             return f"${float_num:,.2f}"
#         float_num = abs(float_num)
#         return f"-${float_num:,.2f}"

#     def update(self, new_amount):
#         self.amount = new_amount
    
#     def __repr__(self):
#         return str(self.amount)
    
#     def __str__(self):
#         return self.dollarize(self.amount)

# cash = MoneyFmt(12345678.021) 
# print(cash) 
# cash.update(100000.4567) 
# print(cash) 
# cash.update(-0.3) 
# print(cash) 
# print(repr(cash))


# from datetime import datetime
# class Clock:
#     def current_time(self):
#         print(datetime.now().strftime("%H:%M:%S"))
    
# class Alarm:
#     def on(self):
#         print("Будильник включен")

#     def off(self):
#         print("Будильник выключен")

# class AlarmClock(Clock, Alarm):
#     def alarm_on(self):
#         self.on()

# clock = AlarmClock()
# clock.current_time() 
# clock.alarm_on()

# from datetime import datetime
# class Clock:
#     @staticmethod
#     def current_time():
#         print(datetime.now().strftime("%H:%M:%S"))
    
# class Alarm:
#     @staticmethod
#     def on():
#         print("Будильник включен")

#     @staticmethod
#     def off():
#         print("Будильник выключен")

# class AlarmClock(Clock, Alarm):
#     def alarm_on(self):
#         self.on()

# clock = AlarmClock()
# clock.current_time() 
# clock.alarm_on()






# from datetime import datetime 

# class CreateMixin: 
#     def create(self, todo, key): 
#         if key in self.todos: 
#             return 'Задача под таким ключом уже существует' 
#         self.todos[key] = todo 
#         return self.todos 

# class DeleteMixin: 
#     def delete(self, key): 
#         delete_ = self.todos.pop(key, None) 
#         if not delete_:
#             return 'нет такого ключа'
#         return delete_

# class UpdateMixin: 
#     def update(self, key, new_value): 
#         self.todos[key] = new_value 
#         return self.todos 

# class ReadMixin: 
#     def read(self): 
#         return sorted(self.todos.items())

# class ToDo(CreateMixin, DeleteMixin, UpdateMixin, ReadMixin): 
#     todos = {} 

#     def set_deadline(self, deadline): 
#         day, month, year = deadline.split("/")
#         datetime_deadline = datetime(int(year), int(month), int(day))
#         datetime_now = datetime.now()
#         return (datetime_deadline - datetime_now).days + 1

# task = ToDo() 
# print(task.set_deadline('31/12/2022'))




# nums = [2,8,15,4,3]
# target = 11
# nn = nums[1:]
# for i in nums:
#     for ii in nn:
#         res = []
#         if i+ii == target:
#                 res.append(nums.index(i))
#                 res.append(nn.index(ii)+1)
#                 print(res)

    
# nums = [3,6,3]
# target =  6
# nn = nums[1:]
# for i in nums:
#     for ii in nn:
#         res = []
#         if i+ii == target:
#                 res.append(nums.index(i))
#                 res.append(nn.index(ii)+1)
#                 print(res)

# class Solution:
#     def twoSum(self, nums, target):
#         for ind, num1 in enumerate(nums):
#             num2 = target - num1
#             if num2 in nums:
#                 if ind != nums.index(num2):
#                     return [ind, nums.index(num2)]



# list1 = []
# for t in range(1, 25):
#     res = 4* t**2 + (24-t)**2
#     list1.append(res)
# print(min(list1))

# for t in range(1, 24):
#     res = 4* t**2 + (24-t)**2
#     if res == 461:
#         print(t)

# t = 5
# print(t, 24-t)




# list1 = []
# list2 = []
# for t in range(1, 25):
#     t2 = 24 - t
#     res = 4* t**2 + t2**2
#     list1.append(res)
#     if res == min(list1):
#         list2.append(t)
# print(min(list1))
# print(list2[-1], 24-list2[-1])

# list1 = []
# list2 = []
# for t in range(1, 25):
#     t2 = 24 - t
#     res = 4* t**2 + t2**2
#     list1.append(res)
#     if res == min(list1):
#         list2.append((t, t2))
# print(min(list1))
# print(list2[-1])

# t1 = 0
# s1 = 1000000
# for t in range(1, 25):
#     t2 = 24 - t
#     s = 4* t**2 + t2**2
#     if s<s1:
#         s1 = s
#         t1 = t

# print(t1, 24-t1, s1)








