from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('events/<str:title>/', views.event_detail, name='event_detail'),
    path('add_event/', views.add_event, name='add_event'),
]

