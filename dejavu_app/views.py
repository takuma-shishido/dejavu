from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.views.generic import TemplateView, CreateView
from django.contrib.auth.views import LoginView as BaseLoginView,  LogoutView as BaseLogoutView
from django.urls import reverse_lazy
from .forms import SignUpForm, LoginFrom
from django.contrib.auth.decorators import login_required


# Create your views here.
def home(request):
    dummy_top_data = [
        {
            "title": "amazing storyadfjlakdjsfjaksdjfajdsfdsasdfasdkfjasdkflsdf",
            "description": "You are intelligent person, my mother told me. But I think it isn't.",
        },
        {
            "title": "WAWARA",
            "description": "You are intelligent person, my mother told me. But I think it isn't.",
        },
        {
            "title": "Users can do it",
            "description": "You are intelligent person, my mother told me. But I think it isn't.sdkfjadskfasldfjklasjdfkjalsjdfadsfhaksdjfljasdjflkaskdf",
        },
        {
            "title": "awesome story",
            "description": "You are intelligent person, my mother told me. But I think it isn't.",
        },
        {
            "title": "awesome story",
            "description": "You are intelligent person, my mother told me. But I think it isn't.",
        },
        {
            "title": "awesome story",
            "description": "You are intelligent person, my mother told me. But I think it isn't.",
        },
        {
            "title": "awesome story",
            "description": "You are intelligent person, my mother told me. But I think it isn't.",
        },
        {
            "title": "awesome story",
            "description": "You are intelligent person, my mother told me. But I think it isn't.",
        },
        {
            "title": "awesome story",
            "description": "You are intelligent person, my mother told me. But I think it isn't.",
        },
        {
            "title": "awesome story",
            "description": "You are intelligent person, my mother told me. But I think it isn't.",
        },
        {
            "title": "awesome story",
            "description": "You are intelligent person, my mother told me. But I think it isn't.",
        },
    ]

    # ここに詳細ページに飛ぶためのURLも追加かな〜
    dummy_book_data = [
        {
            "image_url": "https://m.media-amazon.com/images/I/416l93denJL._AC_UF1000,1000_QL80_.jpg"
        },
        {
            "image_url": "https://m.media-amazon.com/images/I/71PRHp6lTXL._AC_UF1000,1000_QL80_.jpg"
        },
        {
            "image_url": "https://m.media-amazon.com/images/I/71EunwGQXML._AC_UF1000,1000_QL80_.jpg"
        },
        {
            "image_url": "https://m.media-amazon.com/images/I/91B9Jfvrq4L._AC_UF1000,1000_QL80_.jpg"
        },
        {
            "image_url": "https://tshop.r10s.jp/book/cabinet/1014/9784102071014.jpg?fitin=560:400&composite-to=*,*|560:400"
        },
        {
            "image_url": "https://m.media-amazon.com/images/I/61HiPS0fiaL._AC_UF1000,1000_QL80_.jpg"
        },
        {
            "image_url": "https://m.media-amazon.com/images/I/8180Z7cPoxL._AC_UF1000,1000_QL80_.jpg"
        },
        {
            "image_url": "https://m.media-amazon.com/images/I/71ajQBRHXiL._AC_UF1000,1000_QL80_.jpg"
        },
    ]

    context = {"dummy_top_data": dummy_top_data, "dummy_book_data": dummy_book_data}

    return render(request, "home/home.html", context)

class SignupView(CreateView):
    form_class = SignUpForm # 作成した登録用フォームを設定
    template_name = "signup.html"
    success_url = reverse_lazy("accounts:index") # ユーザー作成後のリダイレクト先ページ

    def form_valid(self, form):
        # ユーザー作成後にそのままログイン状態にする設定
        response = super().form_valid(form)
        account_id = form.cleaned_data.get("account_id")
        password = form.cleaned_data.get("password1")
        user = authenticate(account_id=account_id, password=password)
        login(self.request, user)
        return response

# ログインビューを作成
class LoginView(BaseLoginView):
    form_class = LoginFrom
    template_name = "login.html"

class LogoutView(BaseLogoutView):
    success_url = reverse_lazy("accounts:index")

class IndexView(TemplateView):
    template_name = "index.html"