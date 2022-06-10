# API YATUBE
## Оглавление
1. [Описание проекта](https://github.com/TomatoInOil/api_final_yatube#описание-проекта)
2. [Как развернуть](https://github.com/TomatoInOil/api_final_yatube#как-развернуть)
3. [Примеры запросов и ответов](https://github.com/TomatoInOil/api_final_yatube#примеры-запросов-и-ответов)
    1. [Доступные эндпоинты](https://github.com/TomatoInOil/api_final_yatube#доступные-эндпоинты)
    2. [Authorization](https://github.com/TomatoInOil/api_final_yatube#authorization)
    3. [Работа с постами](https://github.com/TomatoInOil/api_final_yatube#работа-с-постами)
    4. [Работа с группами](https://github.com/TomatoInOil/api_final_yatube#работа-с-группами)
    5. [Работа с комментариями](https://github.com/TomatoInOil/api_final_yatube#работа-с-комментариями)
    6. [Работа с подписками](https://github.com/TomatoInOil/api_final_yatube#работа-с-подписками)
    7. [Работа с пользователями](https://github.com/TomatoInOil/api_final_yatube#работа-с-пользователями)
4. [Об авторе](https://github.com/TomatoInOil/api_final_yatube#об-авторе)
## Описание проекта
API сервис для форума писателей "Yatube". Реализована возможность работы с постами, комментариями, группами и пользователями. Подробнее в разделе [примеров запросов и ответов](https://github.com/TomatoInOil/api_final_yatube#примеры-запросов-и-ответов). Аутентификация пользователей реализована по стандарту **JWT**.
## Как запустить
Клонировать репозиторий и перейти в него в командной строке:
```
git clone https://github.com/TomatoInOil/api_final_yatube.git
```
```
cd api_final_yatube
```
Cоздать и активировать виртуальное окружение:
```
python3 -m venv env
```
```
source env/bin/activate
```
Обновить менеджер пакетов
```
python3 -m pip install --upgrade pip
```
Установить зависимости из файла `requirements.txt`:
```
pip install -r requirements.txt
```
Перейти в директорию с `manage.py`:
```
cd yatube_api
```
Выполнить миграции:
```
python3 manage.py migrate
```
Запустить проект:
```
python3 manage.py runserver
```
## Примеры запросов и ответов
### Доступные эндпоинты
| Путь | Методы | Описание|
|------|:------:|---------|
|`.../api/v1/jwt/create/`| POST | Передаём логин и пароль, получаем токены.|
|`.../api/v1/jwt/refresh/`| POST | Передаём refresh токен и получаем новый access токен.|
|`.../api/v1/jwt/verify/`| POST | Передаём access токен, в случае успеха получаем код 200.|
|`.../api/v1/posts/`| GET, POST | Получаем список всех постов или создаём новый пост.|
|`.../api/v1/posts/{pk}/`| GET, PUT, PATCH, DELETE | Получаем, редактируем или удаляем пост по id.|
|`.../api/v1/groups/`| GET | Получаем список всех сообществ.|
|`.../api/v1/groups/{pk}/`| GET | Получаем информацию о сообществе по id.|
|`.../api/v1/posts/{post_id}/comments/`| GET, POST | Получаем список всех комментариев поста с id=post_id или создаём новый, указав id поста, который хотим прокомментировать.|
|`.../api/v1/posts/{post_id}/comments/{comment_id}/`| GET, PUT, PATCH, DELETE | Получаем, редактируем или удаляем комментарий по id у поста с id=post_id.|
|`.../api/v1/follow/`| GET, POST | Получаем список всех подписок или подписываемся на автора, передав в following его никнейм. |
|`.../api/v1/users/`| GET | Получаем список всех пользователей. |
|`.../api/v1/users/{pk}/`| GET | Получаем по id информацию о пользователе: никнейм, имя и фамилию, список id постов. |
### Authorization
Пример запроса токенов
***POST .../api/v1/jwt/create/***
```JSON
{
    "username": "ivan",
    "password": "password_ivana"
}
```
Пример ответа
```JSON
{
    "refresh": "string",
    "access": "string"
}
```
### Работа с постами
Пример запроса создания нового поста с использованием токена Ивана. Ключ `"group"` необязательный.  
***POST .../api/v1/posts/***
```JSON
{
    "text": "Я Иван Иванов! Меня знают все!",
    "group": 1
}
```
Пример ответа
```JSON
{
    "id": 7,
    "text": "Я Иван Иванов! Меня знают все!",
    "pub_date": "2022-06-07T13:57:32.807900Z",
    "author": "ivan",
    "image": null,
    "group": 1
}
```
Пример запроса редактирования поста Ивана. Редактировать посты могут только их авторы.  
***PATCH .../api/v1/posts/7/***
```JSON
{
    "text": "Я просто Иван! Давайте знакомиться в комментариях!"
}
```
Пример ответа
```JSON
{
    "id": 7,
    "text": "Я просто Иван! Давайте знакомиться в комментариях!",
    "pub_date": "2022-06-07T13:57:32.807900Z",
    "author": "ivan",
    "image": null,
    "group": 1
}
```
### Работа с группами
Пример запроса на получение всех групп.  
***GET .../api/v1/groups/***  
В теле запроса ничего передавать не требуется.  
Пример ответа
```JSON
[
    {
        "id": 1,
        "title": "Ivanovo",
        "slug": "ivanovo-slug",
        "description": "Посты из Ivanovo"
    },
    {
        "id": 2,
        "title": "Петрово",
        "slug": "petrovo-slug",
        "description": "Тестовые посты из Петрово"
    }
]
```
Пример запроса по получению информаии о группе с id=2.  
***GET .../api/v1/groups/2/***  
В теле запроса ничего передавать не требуется.  
Пример ответа
```JSON
{
    "id": 2,
    "title": "Петрово",
    "slug": "petrovo-slug",
    "description": "Тестовые посты из Петрово"
}
```
### Работа с комментариями
Пример запроса на создание поста с id=7 с использованием токена Петра.  
***POST .../api/v1/posts/7/comments/***
```JSON
{
    "text": "Привет! Меня зовут Пётр! Я тоже сижу на этом форуме!"
}
```
Пример ответа
```JSON
{
    "id": 4,
    "author": "petr",
    "post": 7,
    "text": "Привет! Меня зовут Пётр! Я тоже сижу на этом форуме!",
    "created": "2022-06-07T14:27:39.832691Z"
}
```
Пример запроса удаления комментария по id=4 у поста с id=7. Удалять комментарии могу только их авторы.  
***DELETE .../api/v1/posts/7/comments/4/***  
В теле запроса ничего передавать не требуется.  
Пример ответа.
```Python
Status: 204 No Content
# в теле ответа ничего не возвращается
```
### Работа с подписками
Пример запроса получения списка своих подписок (требует авторизации). Возможен поиск по подпискам по параметру search.  
***GET .../api/v1/follow/***  
В теле запроса ничего передавать не требуется.  
Пример ответа.
```JSON
[
  {
    "user": "string",
    "following": "string"
  }
]
```
Пример запроса на подписку (требует авторизации).  
***POST .../api/v1/follow/***  
```JSON
{
  "following": "username"
}
```
Пример ответа.  
```JSON
{
  "user": "username",
  "following": "username"
}
```
### Работа с пользователями
Пример запроса пользователя с id=3.  
***GET .../api/v1/users/3/***  
В теле запроса ничего передавать не требуется.  
Пример ответа.  
```JSON
{
    "id": 3,
    "username": "ivan",
    "first_name": "Ivan",
    "last_name": "Ivanov",
    "posts": [
        1,
        6,
        7
    ]
}
```
## Об авторе
Я Даниил Паутов, сейчас я начинающий backend-разработчик. Этот проект дополнение к одному из учебных проектов, выполенных в рамках прохождения курса Яндекс.Практикума "Python-Разработчик". 
