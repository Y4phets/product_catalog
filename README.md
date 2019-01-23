# product_catalog
Django Rest Framework
После зугрузки из GIT'a для запуска проекта нужно:

# Сделать миграции 
```
(корень проекта)$ python manage.py makemigrations
(корень проекта)$ python manage.py migrate
```
# Для входа под администратором нужно создать администратора
```
(корень проекта)$ python manage.py createsuperuser
```
# Запустить на локальном сервере
```
(корень проекта)$ python manage.py runserver
```
# URL:

```
#product_catalog/urls.py

urlpatterns = [
    path('admin/', admin.site.urls),           //для входа под аминистратором
    path('product/', include('product.urls')), //подключение urls товаров и указание начального маршрута
    path('journal/', include('journal.urls')), //подключение urls журнала и указание начального маршрута
]

#product/urls.py

urlpatterns = [
    path('', views.ProductList.as_view()),            //страница расположена на product/
    path('<int:pk>/', views.ProductDetail.as_view()), //по первичному ключу записи, страница расположена на product/# 
]

#journal/urls.py

urlpatterns = [
    path('', views.JournalList.as_view()),            //страница расположена на journal/
    path('<int:pk>/', views.JournalDetail.as_view()), //по первичному ключу записи, страница расположена на journal/# 
]
```
