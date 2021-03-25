from django.urls import path
from .views import HomePage

app_name = 'mainapp'

urlpatterns = [
    path('', HomePage, name="home"),
]