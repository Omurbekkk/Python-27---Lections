"=============== Ассоциация ============="

# Ассоциация - принцип ООП, в котором два класса связаны друг с другом

# Ассоциация делится на 2 принципа:
# 1 - агрегация (более слабая связь)
# Когда мы созадаем класс как атрибут внутри класса
# 2 - композиция (более сильная связь)
# Когда мы создаем класс напр внутри инита

class Battery:
    power = 100

    def charge(self):
        if self.power < 100:
            self.power = 100
        
class Iphone:
    def __init__(self, color):
        self.color = color
        self.battery = Battery()
        # когда мы создаем обьект от другого класса прям внутри другого - композиция

# iphone = Iphone('золотой')
# print(iphone.battery.power) # 100

# del iphone
# обьект батарейки удаляется вместе с обьектом iphone

# print(iphone) # NameError: name 'iphone' is not defined. Did you mean: 'Iphone'?

class Nokia:
    def __init__(self, color, battery):
        self.color = color
        self.battery = battery
        # когда мы принимаем уже созданный вне класса обьект - агрегация

battery = Battery()
nokia = Nokia('черный', battery)

# print(nokia.battery.power) # 100

del nokia
# удаляется только обьект nokia
# обьект батарейки сохраняется

print(nokia.battery) # NameError: name 'nokia' is not defined. Did you mean: 'Nokia'?
print(battery.power) # 100

