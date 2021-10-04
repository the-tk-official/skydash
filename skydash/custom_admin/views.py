from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from custom_admin.utils import filterForAccount, filterForCourses
from ticket.models import Ticket
from courses.models import Course


# Create your views here.

@login_required(login_url='login')
def accounts(request):
    accounts, search_query = filterForAccount(request=request)

    context = {
        'accounts': accounts,
        'search_query': search_query
    }

    return render(request=request, template_name='custom_admin/accounts.html', context=context)


@login_required(login_url='login')
def courses(request):
    courses, search_query = filterForCourses(request=request)

    context = {
        'courses': courses,
        'search_query': search_query
    }

    return render(request=request, template_name='custom_admin/courses.html', context=context)


@login_required(login_url='login')
def tickets(request):
    tickets = Ticket.objects.all()

    context = {
        'tickets': tickets
    }

    return render(request=request, template_name='custom_admin/tickets.html', context=context)
