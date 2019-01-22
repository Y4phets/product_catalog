# journal/urls.py
from django.urls import path

from . import views

urlpatterns = [
    path('', views.JournalList.as_view()),
    # path('', views.JournalList.as_view()),
    path('<int:pk>/', views.JournalDetail.as_view()),
]