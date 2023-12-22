from django.contrib import admin
from django.contrib.auth.models import Group

from accounts.models import User
from .models import Novels
admin.site.register(Novels)