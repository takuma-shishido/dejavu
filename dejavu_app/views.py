from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from django.views.generic import TemplateView, CreateView, DetailView
from django.contrib.auth.views import LoginView as BaseLoginView,  LogoutView as BaseLogoutView
from django.urls import reverse, reverse_lazy
from .forms import SignUpForm, LoginFrom, CommentCreateForm, Novel_detail_from
from django.contrib.auth.decorators import login_required
from .models.comments import Comments
from .models.novel_detail import NovelDetail
from django import forms

from django.views.generic.edit import CreateView


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
    success_url = reverse_lazy("dejavu_app:index")

class IndexView(TemplateView):
    template_name = "index.html"

# create_novel画面
def create_novel(request):
    create_novel_info = ["title", "imag"]
    context = {"create_novel_info" : create_novel_info}
    return render(request, "create_novel.html", context)
  
# write_continue画面（仮置き）
def write_continue(request):
    sample_book_info = ["title", "img", "description", "story"]

    context = {"sample_book_info" : sample_book_info}
    return render(request, "write_continue.html", context)


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
        context['post'] = get_object_or_404(NovelDetail, pk=self.kwargs['pk'])
        return context