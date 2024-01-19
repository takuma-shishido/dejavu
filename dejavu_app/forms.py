from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from .models import Novels, NovelDetail
# User をUsersに変更
from accounts.models import User
from .models.comments import Comments
from .models.novel_detail import NovelDetail


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = (
            "email",
            "first_name",
            "last_name",
            "birth_date",
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
    
class Novel_detail_from(forms.ModelForm):
    class Meta:
        model = NovelDetail
        exclude = ('novel_master_id', 'user_id', 'novel_id', 'content')

class CommentCreateForm(forms.ModelForm):
    """コメントフォーム"""
    class Meta:
        model = Comments
        exclude = ('novel_id', 'created_at')