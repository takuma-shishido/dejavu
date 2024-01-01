from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

# User をUsersに変更
from accounts.models import User

from django import forms
from .models.comments import Comments
from .models.novel_detail import NovelDetail




class SignUpForm(UserCreationForm):
    class Meta:
        model = User  # ここ
        fields = (
            "account_id",
            "email",
            "first_name",
            "last_name",
            "birth_date",
        )


class LoginFrom(AuthenticationForm):
    class Meta:
        model = User  # ここ

class Novel_detail_from(forms.ModelForm):
    class Meta:
        model = NovelDetail
        exclude = ('novel_master_id', 'user_id', 'novel_id', 'content')

class CommentCreateForm(forms.ModelForm):
    """コメントフォーム"""
    class Meta:
        model = Comments
        exclude = ('novel_id', 'created_at')

