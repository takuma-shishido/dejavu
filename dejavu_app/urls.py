from django.urls import path
from . import views

app_name = 'dejavu_app'
urlpatterns = [
    path('create/', views.create_novel, name="create_novel"),
]