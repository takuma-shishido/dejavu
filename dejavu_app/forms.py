from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from .models import Novels, NovelDetail
# User をUsersに変更
from accounts.models import User


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = (
            "email",
            "first_name",
            "last_name",
        )


class LoginFrom(AuthenticationForm):
    class Meta:
        model = User

class NovelCreateForm(forms.ModelForm):
    title = forms.CharField(required=True)
    synopsis = forms.CharField(widget=forms.Textarea, required=True)
    introduction = forms.CharField(widget=forms.Textarea, required=True)
    class Meta:
        model = Novels
        fields = ('title', 'synopsis', 'introduction')

class NovelDetailCreateForm(forms.ModelForm):
    class Meta:
        model = NovelDetail
        fields = "__all__"
    def save(self, commit=True):
        article = super().save(commit)
        print(self.cleaned_data)
        if commit:
            novel = Novels.objects.get(id=self.cleaned_data["novel_id"])
            novel.status += 1
            novel.save()
        return article