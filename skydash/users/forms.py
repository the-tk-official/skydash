from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from users.models import Profile


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'last_name', 'first_name', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update(
                {
                    'class': 'form-control form-control-lg',
                    'placeholder': field.label,
                    'style': 'color: black'
                })


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        exclude = ['user', 'username']
        widgets = {
            'course': forms.CheckboxSelectMultiple(),
        }

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)

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

        self.fields['last_name'].widget.attrs.update(
            {
                'required': 'true',
            }
        )

        self.fields['first_name'].widget.attrs.update(
            {
                'required': 'true',
            }
        )

        self.fields['email'].widget.attrs.update(
            {
                'required': 'true',
            }
        )
