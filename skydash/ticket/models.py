from django.db import models
from django.db.models.signals import pre_save

import uuid

from users.models import Profile
from courses.models import Course


# Create your models here.

class Ticket(models.Model):
    STATUS_CHOICES = (
        ('New', 'New'),
        ('In Process', 'In process'),
        ('Finished', 'Finished')
    )

    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, unique=True)
    mentor = models.ForeignKey(Profile, on_delete=models.CASCADE, limit_choices_to={'prof': 'Mentor'},
                               related_name='related_to_mentor')
    student = models.ForeignKey(Profile, on_delete=models.CASCADE, limit_choices_to={'prof': 'Student'},
                                related_name='related_to_student')
    created = models.DateTimeField(auto_now_add=True)
    location = models.CharField(max_length=200, blank=True, null=True)
    course = models.ManyToManyField(Course, blank=True)
    status = models.CharField(max_length=16, choices=STATUS_CHOICES, default='New')
    price = models.DecimalField(max_digits=6, decimal_places=2, editable=False, blank=True, null=True)
    salary = models.DecimalField(max_digits=6, decimal_places=2, editable=False, blank=True, null=True)

    def __str__(self):
        return f"{self.student.username}'s ticket | Status - {self.status}"
