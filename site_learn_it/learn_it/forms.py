from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = CustomUser
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',
            'role',
        )


class EditProfileForm(UserChangeForm):
    template_name = '/user/edit/'

    class Meta:
        model = CustomUser
        fields = (
            'first_name',
            'last_name',
            'email',
            'password'
            )


class ContactForm(forms.Form):
    name = forms.CharField(label='Имя', widget=forms.TextInput)
    email = forms.EmailField(widget=forms.EmailInput)
    message = forms.CharField(label='сообщение', widget=forms.Textarea)
