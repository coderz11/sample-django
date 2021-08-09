from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.hello, name='hello'),
    path('list/', views.list, name='list'),
    path('detail/<int:pk>/', views.detail, name='detail'),
]