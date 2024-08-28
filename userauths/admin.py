from django.contrib import admin

from userauths.models import User
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser



admin.site.register(User)





class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('email', 'first_name', 'last_name', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_active')
    ordering = ('email',)
    
    # Remove these lines to avoid the error
    # filter_horizontal = ('groups', 'user_permissions',)

admin.site.register(CustomUser, CustomUserAdmin)
