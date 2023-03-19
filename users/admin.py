from django.contrib import admin
from .models import UserExp

@admin.register(UserExp)
class UserExpAdmin(admin.ModelAdmin):
    pass