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




