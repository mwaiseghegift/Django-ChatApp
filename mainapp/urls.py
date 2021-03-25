from django.urls import path
from .views import HomePage, RoomView

app_name = 'mainapp'

urlpatterns = [
    path('', HomePage, name="home"),
    path('room', RoomView, name='room'),
]