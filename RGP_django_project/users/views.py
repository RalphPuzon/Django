from django.shortcuts import render, redirect
#from django.contrib.auth.forms import UserCreationForm 
# ^ django's premade user creation form, we dont need it since we're using UserRegisterForm
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required

def register(request):
	if request.method == 'POST':
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			form.save() #saves the info and crates the user
			username = form.cleaned_data.get('username')
			messages.success(request, f"Your account has been successfully created!")
			return redirect('login')
	else:	
		form = UserRegisterForm()

	return render(request, 'users/register.html', {'form': form})

@login_required #this is to ensure profile security
def profile(request):
	return render(request, 'users/profile.html')