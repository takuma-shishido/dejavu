from django.urls import path
from . import views

app = "dejavu_app"

urlpatterns = [
    path('', views.home, name='home')
]