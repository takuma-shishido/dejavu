from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

# User をUsersに変更
from accounts.models import User

from django import forms
from .models import Comments



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


class CommentCreateForm(forms.ModelForm):
    """コメントフォーム"""
    class Meta:
        model = Comments
        exclude = ('novel_id', 'created_at')

