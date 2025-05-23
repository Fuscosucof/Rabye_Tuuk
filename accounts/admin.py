from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from .forms import CustomUserCreationForm, CustomUserChangeForm
# Register your models here.

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = [
        "email", 
        "username", 
        "age", 
        "description", 
        "is_staff",
    ]
    fieldsets = UserAdmin.fieldsets + (("Skibidi", {"fields":("age", "description", )}),)
    add_fieldsets = UserAdmin.add_fieldsets + (("Skibidi", {"fields":("age", "description", )}),)

admin.site.register(CustomUser, CustomUserAdmin)