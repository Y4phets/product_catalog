# Product catalog on Django Rest Framework
## После зугрузки из GIT'a для запуска проекта нужно:

### Активироввать вертуальное окружнение
```
(корень проекта/env/Srripts)$ cd activate
```
### Скачать все зависимость проекта из requirements.txt

### Сделать миграции 
```
(корень проекта)$ python manage.py makemigrations
(корень проекта)$ python manage.py migrate
```
### Для входа под администратором нужно создать администратора
```
(корень проекта)$ python manage.py createsuperuser
```
### Запустить на локальном сервере
```
(корень проекта)$ python manage.py runserver
```
## URL:
Примеры ссылок:
```
http://127.0.0.1:8000/admin/
http://127.0.0.1:8000/product/
http://127.0.0.1:8000/journal/
http://127.0.0.1:8000/swagger/
```
## Запустить unit test'ы
### Обязательно закомментируйте все атрибуты в разделе REST_FRAMEWORK файла settings.py
```
(корень проекта)$ python manage.py test
```
