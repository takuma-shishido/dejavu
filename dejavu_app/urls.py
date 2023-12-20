from django.urls import path
from . import views

app_name = 'dejavu_app'

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.SignupView.as_view(), name="signup"),
    path('login/', views.LoginView.as_view(), name="login"),
    path('logout/', views.LogoutView.as_view(), name="logout"),
    path('create/', views.create_novel, name="create_novel"),
]