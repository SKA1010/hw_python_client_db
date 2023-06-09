# Домашнее задание к лекции «Работа с PostgreSQL из Python» Sychugov Konstantin

## Задание 1
Создайте программу для управления клиентами на Python.

Требуется хранить персональную информацию о клиентах:

имя
фамилия
email
телефон
Сложность в том, что телефон у клиента может быть не один, а два, три и даже больше. А может и вообще не быть телефона (например, он не захотел его оставлять). Как email так и телефон не могут принадлежать двум клиентам.

Вам необходимо разработать структуру БД для хранения информации и несколько функций на Python для управления данными:

Функция, создающая структуру БД. Т.е. в данной функции создаются таблицы в базе данных
Функция, позволяющая добавить нового клиента как с номером телефона, так и без него
Функция, позволяющая добавить телефон для существующего клиента
Функция, позволяющая изменить данные о клиенте (имя, фамилию и email). Должна быть возможность как изменить одно значение, так и сразу несколько
Функция, позволяющая удалить телефон для существующего клиента
Функция, позволяющая удалить существующего клиента
Функция, позволяющая найти клиента по его данным (имени, фамилии, email-у и телефону) . Должна быть возможность найти клиента как по одному параметру, так и по нескольким. При передачи нескольких параметров, круг поиска должен сужаться.
Функции выше являются обязательными, но это не значит что должны быть только они. При необходимости можете создавать дополнительные функции и классы.

**Структура БД создана**

![image](https://user-images.githubusercontent.com/125235217/236743790-128fd81d-3b36-4926-8ec8-80426b4db209.png)

**Функция поиска работает**

![image](https://user-images.githubusercontent.com/125235217/236743988-c5fed490-6794-42bb-8b5b-308dded1a415.png)

