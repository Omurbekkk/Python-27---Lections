# Slash commands
* \l - список всех базы данных
* \c - показывает через какого юзера и к какой БД мы подключены
* \c name_of_db - подключение к какой-то БД
* \du - список всех юзеров в postgres
* \dt - список всех таблиц в текущей БД
* \d+ - более подробная информация о табицах в текущей БД
* \d+ name_of_table - более подробная информация о табице
* \q - выход из СУБД (PSQL)

# Создание БД и таблиц
```sql
CREATE DATABASE name_of_db;
-- создание БД
```

```sql
CREATE TABLE name_of_table (
    column1 data_type1,
    column2 data_type2,
    ...
);
-- создание таблицы с полями
```

# Удаление БД и таблиц
```sql
DROP DATABASE name_of_db;
-- удаление БД
```

```sql
DROP TABLE name_of_table;
-- удаление таблицы
```

# Заполнение таблиц

```sql
INSERT INTO name_of_db VALUES
(val1, val2),
(val1.2, val2.2);
-- запись данных в таблицу (заполнение всех полей)
```

# Вывод данных из таблицы

```sql
SELECT * FROM name_of_table;
-- вывод всех записей со всеми полями
```

```sql
SELECT column1, column3 FROM name_of_table;
--вывод конкретных полей
```

# Условия

```sql
DELETE FROM name_of_table WHERE condition;
-- удаление всех записей из таблицы соответствующих данному условию
```


