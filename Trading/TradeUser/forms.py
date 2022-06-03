from dataclasses import fields
from pyexpat import model
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import trader


class TraderUserCreationForm(UserCreationForm):
    class Meta:
        model = trader
        # fields = "__all__"
        fields = ('is_customer', 'is_vendor', 'mobile_number',
                  'date_of_birth', 'city', 'email_id')
