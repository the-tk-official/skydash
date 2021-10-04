from django.forms import ModelForm
from django import forms

from ticket.models import Ticket


class TicketForm(ModelForm):
    class Meta:
        model = Ticket
        fields = ['mentor', 'student', 'location', 'course']
        widgets = {
            'course': forms.CheckboxSelectMultiple(),
        }

    def __init__(self, *args, **kwargs):
        super(TicketForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update(
                {
                    'class': 'form-control form-control-lg',
                    'placeholder': field.label,
                    'style': 'color: black'
                })

        self.fields['course'].widget.attrs.update(
            {
                'class': '',
            }
        )


class updateStatus(ModelForm):
    class Meta:
        model = Ticket
        fields = ['status']

    def __init__(self, *args, **kwargs):
        super(updateStatus, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update(
                {
                    'class': 'form-control form-control-lg',
                    'placeholder': field.label,
                    'style': 'color: black'
                })
