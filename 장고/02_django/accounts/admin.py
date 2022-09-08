from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User        #등록한 User를 admin 사이트에서 보고 싶다면
# Register your models here.

admin.site.register(User, UserAdmin)