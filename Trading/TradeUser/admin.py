from django.contrib import admin

from .models import trader
from .forms import TraderUserCreationForm
from django.contrib.auth.admin import UserAdmin
# Register your models here.


class CustomUserAdmin(UserAdmin):
    model = trader
    add_form = TraderUserCreationForm


admin.site.register(trader)

# admin.site.register(trader, CustomUserAdmin)
