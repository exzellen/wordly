# Wordly API
## Описание
API позволяет пользователям заходить под своими никами, создавать лобби, после чего играть в Wordly с другим игроком.

## Технологии
- Python 3.11
- Django 5.0.2
- Django REST Framework 3.14.0

# Установка
## Копирование репозитория
Клонируем репозиторий и переходим в папку проекта:
```
~ git clone git@github.com:Certelen/Wordly.git
~ cd wordly
```

## Развертывание на текущем устройстве:
Устанавливаем и активируем виртуальное окружение из папки с проектом
```
~ py -3.11 -m venv venv
~ . venv/Scripts/activate
```
Устанавливаем требуемые зависимости:
```
~ pip install -r requirements.txt
```

Переходим в папку
```
~ cd wordly
```
Перед первым запуском создаем и выполняем миграции:
```
python manage.py makemigrations players lobbys
python manage.py migrate
```
Создаем суперпользователя, если необходимо:
```
python manage.py createsuperuser
```
# Запуск
Запуск сервиса производится командой:
```
~ py manage.py runserver
```

# Инструкция по игре
## Первый логин:
Для начала требуется [создать игрока](http://127.0.0.1:8000/) (Требуется только логин), после создания откроется страница с созданием или поиском лобби. 

## Повторный логин:
Если игрок уже создавал аккаунт, нужно [авторизироваться](http://127.0.0.1:8000/) (Требуется только логин), после этого откроется страница с созданием или поиском лобби. 

## Пройти в лобби:
Если есть id лобби, можно присоединиться к нему, вписав id в поле "Найти лобби". Иначе можно создать лобби, выбрав количество букв (4-6), оставив поле "Найти лобби" пустым.
После отправки запроса страница перенаправится на саму игру, если вы нашли лобби, ваш ход первый - просто вводите слово, если создали лобби - без второго игрока игра не начнется, отправьте код второму игроку.

# Для администратора
В [админке](http://127.0.0.1:8000/admin) у каждого пользователя есть статистика, которую можно просмотреть, у каждого лобби можно узнать слово для победы.

# Адресные пути
- [Создание пользователя/вход](http://127.0.0.1:8000/)
- [Админка](http://127.0.0.1:8000/admin)

