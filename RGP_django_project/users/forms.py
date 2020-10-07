# customizabe form instad of using django default form
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
	email = forms.EmailField() #default "field required" in place

	class Meta: # namespace for 
		model = User
		fields = ['username', 'email', 'password1', 'password2']