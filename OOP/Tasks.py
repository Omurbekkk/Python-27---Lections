class Song:
    def __init__(self, title, author, year): 
        self.title = title
        self.author = author
        self.year = year
    def show_title(self):
        return f'Название этой песни {self.title}'

    def show_author(self):
        return f'Автор этой песни {self.author}'
    
    def show_year(self):
        return f'Эта песня вышла в {self.year} году'
    


song = Song('omur', 'dos', '2345')
print(song.show_title())
print(song.show_author())
print(song.show_year())



class Circle:
    pi = 3.14
    color = 'Синий'
    def __init__(self, radius):
        self.radius = radius
    def get_area(self):
        return self.pi * self.radius**2

circle = Circle(2)
# print(circle.radius)
Circle.color = 'несиний'
print(circle.color)
print(circle.get_area())



class BankAccount:
    def __init__(self): 
       self.balance = 0
    
    def withdraw(self, som): 
       self.balance -= som 
       print('Ваш баланс:', self.balance, 'сом')
    
    def deposit(self, som): 
       self.balance += som 
       print('Ваш баланс:', self.balance, 'сом')

account = BankAccount()
account.deposit(1000)
account.withdraw(500)


class Taxi:
    def __init__(self, name, cost, cost_km): 
        self.name = name
        self.cost = cost
        self.cost_km = cost_km
    def get_total_cost(self, km):
        res = self.cost + (self.cost_km*km)
        return f'Такси {self.name}, стоимость поездки: {res} сом'


taxi1 = Taxi('Namba',10, 5)
taxi2 = Taxi('Yandex', 20, 10)
taxi3 = Taxi('Jorgo', 30, 15)
print(taxi1.get_total_cost(10)) 
print(taxi2.get_total_cost(6)) 
print(taxi3.get_total_cost(14))


class Phone:
    def __init__(self, name, last_name, phone): 
        self.name = name
        self.last_name = last_name
        self.phone = phone
    def get_info(self):
        print(f'Контакт: {self.name} {self.last_name}, телефон: {self.phone}')


contact = Phone('omur', 'dos', '+12345')
contact.get_info()



