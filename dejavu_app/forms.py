from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from .models import Novels
# User をUsersに変更
from accounts.models import User


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

class NovelCreateForm(forms.ModelForm):
    class Meta:
        model = Novels
        fields = ('title', 'synopsis', 'introduction',)
