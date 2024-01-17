from django.forms.models import BaseModelForm
from django.http import HttpResponse, HttpResponseNotFound

from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from django.views.generic import TemplateView, CreateView
from django.contrib.auth.views import LoginView as BaseLoginView,  LogoutView as BaseLogoutView
from django.urls import reverse_lazy, reverse
from .forms import SignUpForm, LoginFrom, NovelCreateForm, NovelDetailCreateForm, CommentCreateForm, Novel_detail_from

from django.contrib.auth.decorators import login_required
from django.views import generic
from .models import Novels, NovelDetail
from django.utils.decorators import method_decorator
from .models.comments import Comments
from .models.novel_detail import NovelDetail




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
        initial['user_id'] = self.request.user.id
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

class Detail_view(CreateView):
    template_name = 'comments/novel_detail.html'
    model = NovelDetail
    form_class = Novel_detail_from
    
    def get_success_url(self):
        return reverse('comments', kwargs={'pk': self.object.id})
    
    def get_context_data(self,  **kwargs):
        context = super().get_context_data( **kwargs)
        context['comments'] = Comments.objects.all()
        print(context)
        print("aa")
        return context
    #Test_blog.objects.create(content="コンテンツ")
    # def get_object(self, queryset=None):
    #     return get_object_or_404(Test_blog, pk=self.kwargs['pk'])
    
    # sample = Comments(user_id="11",comment="コメント")
    # sample.save()
    # print("a")
    # print(sample)

    # sample_comment = "サンプルコメントです"
    # context = {"sample_comment" : sample_comment}
    # return render(request, "comments/novel_detail.html", context)

class Create_comments(CreateView):
    template_name = "comments/comments.html"
    model = Comments
    form_class = CommentCreateForm
    success_url = reverse_lazy("novel_detail")

    def form_valid(self, form):
        post_pk = self.kwargs['pk']
        print(post_pk)
        post = get_object_or_404(NovelDetail, pk=post_pk)
        comment = form.save(commit=False)
        comment.novel_id = post
        comment.save()
        return redirect('dejavu_app:novel_detail', pk=post_pk)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post'] = get_object_or_404(NovelDetail, pk=self.kwargs['novel_id'])
        return context
