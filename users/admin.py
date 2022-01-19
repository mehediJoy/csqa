from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('is_teacher',)}),
    )

CustomUserAdmin.list_display += ('points', 'is_teacher')


admin.site.register(User, CustomUserAdmin)