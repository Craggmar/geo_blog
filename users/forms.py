from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class CreateUserForm(UserCreationForm):
  username = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"Nazwa użytkownika"}))
  email = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"Email"}))
  password1 = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder":"Hasło"}))
  password2 = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder":"Potwierdź hasło"}))
  choice_list = [('regular_users', 'Zwykły użytkownik'),('extended_users', 'Użytkownik+ (dodawanie treści)')]
  permissions = forms.ChoiceField(choices= choice_list, widget=forms.RadioSelect)

  class Meta:
    model = User
    fields = ["username", "email", "password1", "password2",]

