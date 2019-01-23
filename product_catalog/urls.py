# product_catalog/urls.py

from django.contrib import admin
from django.urls import include, path
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='Documentation')

urlpatterns = [
    path('swagger/', schema_view),
    path('admin/', admin.site.urls),
    path('product/', include('product.urls')),
    path('journal/', include('journal.urls')),
]
