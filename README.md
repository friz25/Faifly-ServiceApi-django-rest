# 👨‍⚕️ Faifly-ServiceApi-django-rest
Status of last Deployment:<br>
<img src="https://github.com/friz25/Flask-Online-Store-45/workflows/My-GitHub-Actions-Basics/badge.svg?branch=master"><br>

Простите что так поздно сдаю работу (должен был доделать другой заказ) поэтому начал делать только сегодня утром 😅.

Сделал django rest приложение (с PostgreSQL в качестве БД) <br>

Могу также прикрутить Wagtail (уже работал с ним) и простенький симпотичный frontend - но на это нужно будет еще пару дней (сдаю так, боюсь что поздно его сдаю)

<details><summary>🏗 Cамо Тестовое задание :</summary>

Написать бекенд для контроля записи пользователей на услуги 
Написать web API с набором эндпоинтов, позволяющим клиентам получать список свободных специалистов в определённое время, а также записываться на прием к специалистам. Специалисты должны получать список записанных на определённое время клиентов. Кроме того, администратор должен иметь возможность управлять специалистами и их рабочим временем.
Примеры использования:
запись на прием к врачу , запись на косметологическую процедуру, стрижку, массаж, и т.п. запись на оформление документов
Проект можно условно разделить на 3 части:
API для клиентов, позволяющая записаться на свободное время к определенному специалисту 
API для специалистов, позволяющая видеть записанных на приём клиентов
Админ-панель для администраторов, позволяющая управлять специалистами, их рабочими часами

Основные сущности:
- Location - место для работы специалиста. В одном месте в одно время может работать только один специалист
- Worker - специалист, предоставляющий услугу
- Schedule - временной отрезок работы специалиста.
Для каждого рабочего дня можно устанавливать отдельный отрезок, также в один день можно установить несколько рабочих отрезков (например, с 8:00 до 10:00 и с 17:00 до 21:00 того же дня)
- Appointment - забронированная запись на прием, создаваемая клиентом через API. Запись должна содержать время начала и время конца (разные процедуры могут занимать разное время)

API для клиентов - web API, позволяющее получить список специалистов, время приема специалиста для определенного дня, а также возможность записаться на приём в определённое (свободное) время. Пользовательский API должен предоставлять следующую информацию
список специалистов с возможностью фильтрации по их специальности выбор расписания специалиста по дате

API для специалистов - web API, позволяющее получить список клиентов, записанных на приём. API должен предоставлять следующую информацию:
список клиентов и временных отрезков, на которые они зарегистрированы, с возможностью фильтрации их по дате

Обязательные требования по стеку технологий: Использование реляционной базы данных Использование python и Django для написания бекенда

Будет плюсом: 
- Использование Django REST Framework  
- Использование Wagtail (для админ панели)
- Создание frontend части для клиентов/специалистов

На своё усмотрение можно добавить любую функциональность

</details>

<details><summary>🏰 what else can i implemented :</summary>

### FrontEnd part:

- jinja templating
- bootstrap
- admin panel (images in admin panel) (article editor - ckeditor)
- reviews
- worker, service, location filter
- worker, service search
- worker, service, location ratings
- Ajax filtering (dynamic content)
- pagination
- flat pages
- newsletter subscription
- multilangualism
- authorization and registration
- login via Vk, Gmail


</details>
<details><summary>🧙 Как запустить / Установка :</summary>

клонируем проект из github'a себе на рабочий пк<br>
создадим venv `python -m venv venv`<br>
зайдём в виртуальное окружение
с терминала (venv/Scripts/activate):
```
pip install django
pip install pillow
pip install djangorestframework
pip install psycopg2-binary
pip install django-filter
pip install djoser
pip install djangorestframework_simplejwt
pip install django-cors-headers 
pip install django-ckeditor
```
Установим PostgreSQL. Запустим. Создадим таблицу `service`<br>
*заёдём в файл `settings.py` укажем свои данные БД там :
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'db.name',
        'USER': 'user_name',
        'PASSWORD': 'pass',
        'HOST': 'localhost',
        'PORT':  '5432',
     }
}
```
*создаём админа
`python manage.py createsuperuser`
*проведём миграции в БД
```
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```
*если всё ОК, проект запустился 🧙<br><br>
http://127.0.0.1:8000/admin/ <br>
http://127.0.0.1:8000/swagger/

</details>

# 🏂 СКРИНШОТЫ :

## Общие результаты работы

<details><summary>Что было сделано</summary>

1. ckeditor (удобный редактор текста в админке) добавлен для service, worker, location, appointment (можно добавить еще для schedule, review, ServiceCategory) 
2. добавление и вывод отзывов/комментов для worker (атакже в бете - для service, location, appointment)
3. добавление и обновление, вывод рейтинга (1-5 звёзд) для worker (атакже в бете - для service)
4. фильтрация по типам услуг, услугам и цене (django-filter) (в бете)
5. djoser регистрация, авторизация, отправка email с подтверждением
6. drf-yasg автодокументирование api
7. добавление cors header'ов
8. пагинация в api (общая и частная)

</details>

<details><summary>Админка + SWAGGER (общие результаты работы)</summary>

Админка - Главная страница

<img src="https://i.ibb.co/KG6FWPH/Django-Google-Chrome.jpg" width="300">

SWAGGER (Полный отчёт)

<img src="https://i.ibb.co/tcNRrhm/screencapture-127-0-0-1-8000-swagger-2022-07-01-12-27-32.png" width="300">

</details>

## Location
<details><summary>Location (Локация / Кабинет)</summary>

Locations (API) - Все Локации / Кабинеты

<img src="https://i.ibb.co/JcFFDGH/screencapture-127-0-0-1-8000-api-v1-location-2022-07-04-09-54-14.png" width="300">

Location/1 (API) - Инфа об одной Локация / Кабинет

<img src="https://i.ibb.co/0F6CFwx/Locations-1-Django-REST-framework-Google-Chrome.jpg" width="300">

Location - Список Локация / Кабинет (в админке)

<img src="https://i.ibb.co/S5BsYvG/screencapture-127-0-0-1-8000-admin-services-location-2022-07-01-13-02-15.png" width="300">

Location - Редактировать Локация / Кабинет (в админке)

<img src="https://i.ibb.co/bJr1TDv/screencapture-127-0-0-1-8000-admin-services-location-5-change-2022-07-01-13-02-28.png" width="300">

</details>

## Schedules
<details><summary>Schedules (Рабочие смены специалистов)</summary>

Schedule (API) - Рабочие смены специалистов

<img src="https://i.ibb.co/rpFY33V/screencapture-127-0-0-1-8000-api-v1-schedule-2022-07-04-09-53-51.png" width="300">

Schedule/1 (API) - Инфа об одной Рабочей смене специалиста

<img src="https://i.ibb.co/wppxV5C/Schedules-1-Django-REST-framework-Google-Chrome.jpg" width="300">

Schedule - Список всех Рабочих смен специалистов (в админке)

<img src="https://i.ibb.co/pR4BJjX/Django-Google-Chrome.jpg" width="300">

</details>

## Appointment
<details><summary>Appointment (Запись на приём) </summary>

Appointment (API) - Запись на приём

<img src="https://i.ibb.co/KbF2vw4/Appointment-Django-REST-framework-Google-Chrome.jpg" width="300">

Appointment - Запись на приём (в админке)

<img src="https://i.ibb.co/5kYTkcR/screencapture-127-0-0-1-8000-admin-services-appointment-3-change-2022-07-01-13-04-32.png" width="300">

Appointment - Список всех Записей на приём (в админке)

<img src="https://i.ibb.co/Y2TqJXS/Django-Google-Chrome.jpg" width="300">

</details>

## Review
<details><summary>Review (Отзывы) </summary>

Review Create (API) - Создать отзыв о Специалисте

<img src="https://i.ibb.co/tCXhMjc/screencapture-127-0-0-1-8000-api-v1-review-2022-07-01-12-25-15.png" width="300">

Review - Список Отзывов (в админке)

<img src="https://i.ibb.co/JvP6pzx/screencapture-127-0-0-1-8000-admin-services-review-2022-07-01-13-01-42.png" width="300">


Review - Редактировать Отзыв (в админке)

<img src="https://i.ibb.co/8rRck8p/Django-Google-Chrome.jpg" width="300">

</details>

## Service

<details><summary>Service (Услуги)</summary>

Service - Редактировать Услугу (в админке)

<img src="https://i.ibb.co/FhxbNBQ/screencapture-127-0-0-1-8000-admin-services-service-2-change-2022-07-01-12-59-31.png" width="300">

ServiceShots - Список Фото Услуг (в админке)

<img src="https://i.ibb.co/PDvPD2r/screencapture-127-0-0-1-8000-admin-services-serviceshots-2022-07-01-13-03-09.png" width="300">

Service - Список всех Услуг (в админке)

<img src="https://i.ibb.co/1RJ2vQk/Django-Google-Chrome.jpg" width="300">

Service/1 (API) - Описание одной Услуги

<img src="https://i.ibb.co/bFmp9GP/screencapture-127-0-0-1-8000-api-v1-service-1-2022-07-01-12-20-06.png" width="300">

Service (API) - Список всех Услуг

<img src="https://i.ibb.co/d7CfwD7/screencapture-127-0-0-1-8000-api-v1-service-2022-07-04-09-55-11.png" width="300">

</details>

## Worker

<details><summary>Worker - Специалист </summary>

Worker - Редактировать Специалиста (в админке) 

<img src="https://i.ibb.co/cL2pXgj/screencapture-127-0-0-1-8000-admin-services-worker-5-change-2022-07-01-13-00-04.png" width="300">

Worker - Список Специалистов (в админке)

<img src="https://i.ibb.co/gmM0SDq/screencapture-127-0-0-1-8000-admin-services-worker-2022-07-01-12-59-48.png" width="300">

Workers (API) - Список всех Специалистов

<img src="https://i.ibb.co/qFTFg6D/screencapture-127-0-0-1-8000-api-v1-worker-2022-07-04-09-56-25.png" width="300">

Worker/1 (API) - Описание одного Специалиста

<img src="https://i.ibb.co/mqD3q0g/Workers-Django-REST-framework-Google-Chrome.jpg" width="300">

</details>

## StarRating

<details><summary>StarRating (Оценки пользователей Специалистам)</summary>

Add Star Rating (API) - Добавить оценку пользователя Специалисту

<img src="https://i.ibb.co/M191jWS/screencapture-127-0-0-1-8000-api-v1-rating-2022-07-01-12-28-09.png" width="300">

Rating - Список всех оставленых Оценок Специалистам (в админке)

<img src="https://i.ibb.co/vXDzfSc/Django-Google-Chrome.jpg" width="300">

</details>

## AddUser
<details><summary>UserList (API) - Создать Пользователя</summary>

<img src="https://i.ibb.co/VLLcQKK/screencapture-127-0-0-1-8000-auth-users-2022-07-01-12-22-50.png" width="300">

</details>

<style>
img{
box-shadow: 0px 10px 15px 10px #222;
}
img:hover {
box-shadow: 0 0 0 1px #ccc,
0 -20px 10px -5px #6BFA76,
20px 0 10px -5px #FBC16A,
0 20px 10px -5px #F4F171,
-20px 0 10px -5px #6BA5FA;	
-webkit-transition: all 0.5s ease;
-moz-transition: all 0.5s ease;
transition: all 0.5s ease;
}
</style>