from django.forms.models import BaseModelForm
from django.http import HttpResponse, HttpResponseNotFound

from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.views.generic import TemplateView, CreateView
from django.contrib.auth.views import LoginView as BaseLoginView,  LogoutView as BaseLogoutView
from django.urls import reverse_lazy
from .forms import SignUpForm, LoginFrom, NovelCreateForm, NovelDetailCreateForm
from django.contrib.auth.decorators import login_required
from django.views import generic
from .models import Novels, NovelDetail
from django.utils.decorators import method_decorator




# Create your views here.

def home(request):
    novels = Novels.objects.all()
    context = {
        'novels': novels
    }
    try:
        top_novel = Novels.objects.get(id=8)
        middle_novels = Novels.objects.filter(id__lte=5)
        context = {'novels': novels, 'top_novel': top_novel, 'middle_novels': middle_novels}
    except:
        print('要素数が8未満です or 5未満です')
    return render(request, "home/home.html", context)

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
    success_url = reverse_lazy("dejavu_app:home")

class IndexView(TemplateView):
    template_name = "index.html"

@method_decorator(login_required, name='dispatch')
# create_novel画面

class CreateNovelView(CreateView):
    model = Novels
    form_class = NovelCreateForm
    success_url = reverse_lazy("dejavu_app:home")
    template_name = "create_novel.html"
    # userを入れる
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class WriteContinueView(CreateView):
    model = NovelDetail
    form_class = NovelDetailCreateForm
    success_url = reverse_lazy("dejavu_app:home")
    template_name = "write_continue.html"

    def setup(self, request, *args, **kwargs):
        if hasattr(self, "get") and not hasattr(self, "head"):
            self.head = self.get
        self.request = request
        self.args = args
        self.kwargs = kwargs

    def get_context_data(self, **kwargs):
        novel = Novels.objects.get(pk=self.kwargs["novel_id"])
        context = super().get_context_data(**kwargs)
        context['novel'] = novel
        context['novel_id'] = self.kwargs["novel_id"]
        context['novel_status'] = Novels.STATUS_CHOICES[novel.status][1]
        return context

    def get_initial(self):
        initial = super().get_initial()
        initial['novel_id'] = self.kwargs["novel_id"]
        initial['user_id'] = self.request.user.account_id
        print(initial)
        return initial


# myProfile画面
def myProfile(request):
    dummy_top_data = [
        {
            "title": "amazing storyadfjlakdjsfjaksdjfajdsfdsasdfasdkfjasdkflsdf",
            "image_url": "https://m.media-amazon.com/images/I/416l93denJL._AC_UF1000,1000_QL80_.jpg",
        },
        {
            "title": "WAWARA",
            "image_url": "https://m.media-amazon.com/images/I/71PRHp6lTXL._AC_UF1000,1000_QL80_.jpg",

        },
        {
            "title": "Users can do it",
            "image_url": "https://m.media-amazon.com/images/I/71EunwGQXML._AC_UF1000,1000_QL80_.jpg",
        },
        {
            "title": "awesome story",
            "image_url": "https://m.media-amazon.com/images/I/91B9Jfvrq4L._AC_UF1000,1000_QL80_.jpg",
        },
    ]
    # myProfile_info = []
    # context = {"myProfile_info" : myProfile_info}
    context = {"dummy_top_data": dummy_top_data}
    return render(request, "myProfile.html", context)

