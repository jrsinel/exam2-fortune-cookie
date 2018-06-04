from django.urls import path

from . import views

urlpatterns = [
    path('result/', views.result, name='result'),
    path('<int:pk>/change/', views.FortuneUpdate.as_view(), name='change_fortune'),
]
