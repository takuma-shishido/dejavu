from django.urls import path
from . import views

app_name = 'dejavu_app'

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.SignupView.as_view(), name="signup"),
    path('login/', views.LoginView.as_view(), name="login"),
    path('logout/', views.LogoutView.as_view(), name="logout"),
    path('create/', views.CreateNovelView.as_view(), name="create_novel"),
    path('write_continue/<int:novel_id>/', views.WriteContinueView.as_view(), name="write_continue"),
    path('myProfile/', views.myProfile, name="myProfile"),
    path('novel_detail/<int:novel_id>/', views.Detail_view.as_view(), name="novel_detail"),
    path('create_comments/<int:novel_id>/', views.Create_comments.as_view(), name="create_comments")

]