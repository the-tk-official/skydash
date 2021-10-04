from django.db import models


# Create your models here.

class Course(models.Model):
    title = models.CharField(max_length=256)
    duration = models.PositiveIntegerField(default=0)
    price = models.DecimalField(max_digits=6, decimal_places=2, default=0)

    def __str__(self):
        return f'{self.title}'
