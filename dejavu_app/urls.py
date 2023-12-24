from django.urls import path
from . import views

app_name = 'dejavu_app'

urlpatterns = [
    path('', views.home, name='home'),
    path('index/', views.IndexView.as_view(), name='index'),
    path('signup/', views.SignupView.as_view(), name="signup"),
    path('login/', views.LoginView.as_view(), name="login"),
    path('logout/', views.LogoutView.as_view(), name="logout"),
    path('create/', views.CreateNovelView.as_view(), name="create_novel"),
    path('write_continue/', views.write_continue, name="write_continue"),
    path('myProfile/', views.myProfile, name="myProfile"),
]