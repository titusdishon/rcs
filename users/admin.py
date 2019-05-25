from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import UserCreationForm, ProfileUpdateForm
from .models import User, UserStatus, UserType


class UserAdmin(UserAdmin):
    add_form = UserCreationForm
    form = ProfileUpdateForm
    model = User
    list_display = ['username', 'first_name', 'last_name','email', 'mobile', 'user_type', 'organization', 'role_center', 'agent', 'citizen_st',
                    'user_status']
    list_editable = ['email', 'first_name', 'last_name', 'mobile', 'user_type', 'organization', 'role_center', 'agent', 'citizen_st', 'user_status']


admin.site.register(User, UserAdmin)
admin.site.register(UserStatus)
admin.site.register(UserType)
