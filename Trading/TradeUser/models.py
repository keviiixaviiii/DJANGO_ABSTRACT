from django.db import models
from django.contrib.auth.models import AbstractUser
from sqlalchemy import false


class trader(AbstractUser):
    gender_choice = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('NP', 'Not Specified'),
    ]
    gender = models.CharField(choices=gender_choice, max_length=20)
    is_customer = models.BooleanField('customer status', default=False)
    is_vendor = models.BooleanField('vendor status', default=False)
    email_id = models.EmailField(unique=True)
    mobile_number = models.CharField(max_length=10, unique=True)
    is_mobile_verified = models.BooleanField(default=False)
    date_of_birth = models.DateField(blank=True, null=True)
    city = models.CharField(max_length=1024, blank=True, null=True)
    # pan_no = models.CharField(unique=True, null=False, max_length=4)
    zip_code = models.CharField(
        max_length=12, blank=True, null=True)
