from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from ticket.models import Ticket


@receiver(pre_save, sender=Ticket)
def updateTicket(sender, instance, **kwargs):
    instance.price = sum(course.price for course in instance.course.all())
    instance.salary = (instance.price * 30 / 100)
