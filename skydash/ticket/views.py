from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from ticket.forms import TicketForm, updateStatus
from ticket.models import Ticket


# Create your views here.

@login_required(login_url='login')
def createTicket(request):
    if request.method == 'POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.save()
            form.save_m2m()
            form.save()
            return redirect('tickets')
    else:
        form = TicketForm()

    context = {
        'form': form,
    }

    return render(request=request, template_name='ticket/create.html', context=context)


@login_required(login_url='login')
def updateTicket(request, pk):
    ticket = Ticket.objects.get(id=pk)

    if request.method == 'POST':
        form = updateStatus(request.POST, instance=ticket)
        if form.is_valid():
            form.save()
            return redirect('tickets')
    else:
        form = updateStatus(instance=ticket)

    context = {
        'form': form,
        'pk': pk,
    }

    return render(request=request, template_name='ticket/update.html', context=context)


@login_required(login_url='login')
def deleteTicket(request, pk):
    ticket = Ticket.objects.get(id=pk)
    ticket.delete()

    return redirect('tickets')
