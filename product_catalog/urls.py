# product_catalog/urls.py

from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path('admin/', admin.site.urls),
    path('product/', include('product.urls')),
    path('journal/', include('journal.urls')),
]