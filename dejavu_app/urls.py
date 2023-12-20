from django.urls import path
from . import views

app_name = 'dejavu_app'

urlpatterns = [
    path('write_continue/', views.write_continue, name="write_continue"),
]