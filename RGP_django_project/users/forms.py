# customizabe form instad of using django default form
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from.models import Profile

#form for when users register to the site
class UserRegisterForm(UserCreationForm):
	email = forms.EmailField() #default "field required" in place
	#v think metadata, this class is just a container
	class Meta: # nested namespace for configurations to keep it in one place 
		model = User # model affected is "User", form.save will go to User
		fields = ['username', 'email', 'password1', 'password2'] #fields we want, and in what order

#!! understand that the "user" and "profile" entities are separate. just connected
#form for when users try to update their USER info:
class UserUpdateForm(forms.ModelForm):
	email = forms.EmailField() 

	class Meta:
		model = User 
		fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields =['image']