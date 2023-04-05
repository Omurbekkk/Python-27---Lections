from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

# driver://user:password@host:port/db_name
db_url = 'postgresql://user:1@127.0.0.1:5432/sqlalchemy_test'
engine =  create_engine(db_url)
# подключение к БД


Base = declarative_base()
# базовыый класс для таблиц

class Product(Base):
    __tablename__ = 'product'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    price = Column(Integer)

    def __repr__(self):
        return f"({self.id} -> {self.title})"

Base.metadata.create_all(bind=engine)
# записываем таблицу в БД

SessionLocal = sessionmaker(bind=engine)
# создаем класс для сессий (один объект от данного класса - это одна сессия)

session = SessionLocal()
# создаем сессию

new_product = Product(title='product1', price=120)
# создаем продукт (запись в таблицу)
# для ОРМ создаем запрос на запись в таблицу

# session.add(new_product)
# # добавляем запрос в сессию

# session.commit()
# # отправляем набор запросов БД


products = session.query(Product).all()
# получаем все записи из таблицы Product
print(products)


res = session.query(Product).filter(Product.price > 100).all()
# получаем все записи из таблицы product у которых цена больше 100
print(res)

product3 = session.query(Product).get(3)
# получаем продукт под id 3
print(product3)

product4 = session.query(Product).get(4)
# получаем продукт под id 4
# session.delete(product4)
# # удаляем продукт
# session.commit()
# сохраняем изменения в БД


product3.title = 'new title'
product3.price = 100
# изменяем продукт
session.commit()
# сохраняем изменения в БД







