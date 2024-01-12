from django.contrib.auth import login, authenticate
from django.views.generic import TemplateView, CreateView
from django.contrib.auth.views import LoginView as BaseLoginView,  LogoutView as BaseLogoutView
from django.urls import reverse_lazy
from dejavu_app.forms import SignUpForm, LoginFrom


class IndexView(TemplateView):
    template_name = "index.html"


class SignupView(CreateView):
    form_class = SignUpForm # 作成した登録用フォームを設定
    template_name = "signup.html"
    success_url = reverse_lazy("accounts:index") # ユーザー作成後のリダイレクト先ページ

    def form_valid(self, form):
        # ユーザー作成後にそのままログイン状態にする設定
        response = super().form_valid(form)
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password1")

        user = authenticate(email=email, password=password)
        
        login(self.request, user)
        return response

# ログインビューを作成
class LoginView(BaseLoginView):
    form_class = LoginFrom
    template_name = "login.html"

class LogoutView(BaseLogoutView):
    success_url = reverse_lazy("accounts:index")
