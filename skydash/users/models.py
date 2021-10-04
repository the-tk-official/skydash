from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator

import uuid

from courses.models import Course


# Create your models here.

class Profile(models.Model):
    GENDERS_CHOICES = (
        (None, 'Choose your gender'),
        ('Male', 'Male'),
        ('Female', 'Female')
    )

    PAYMENT_CHOICE = (
        ('Yes', 'Yes'),
        ('No', 'No')
    )

    PROF_CHOICE = (
        (None, 'New user'),
        ('Mentor', 'Mentor'),
        ('Student', 'Student'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=16, blank=True, null=True)
    email = models.CharField(max_length=16, unique=True, blank=True, null=True)
    first_name = models.CharField(max_length=16, blank=True, null=True)
    last_name = models.CharField(max_length=16, blank=True, null=True)
    age = models.PositiveIntegerField(blank=True, null=True)
    phone_regex = RegexValidator(regex=r'\+998\s\d{2}\s\d{3}\s\d{2}\s\d{2}',
                                 message='Phone number must be entered in the format: "+998 99 999 99 99".'
                                         'Up to the 12 digits allowed.')
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True, null=True)
    email = models.EmailField(max_length=32, blank=True, null=True)
    gender = models.CharField(max_length=8, choices=GENDERS_CHOICES, blank=True, null=True)
    prof = models.CharField(max_length=16, choices=PROF_CHOICE, default=None, blank=True, null=True)
    payment = models.CharField(max_length=8, choices=PAYMENT_CHOICE, default='No', blank=True, null=True)
    course = models.ManyToManyField(Course, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return f'{self.user} | {self.prof}'
