from django.shortcuts import render, redirect
#from django.contrib.auth.forms import UserCreationForm 
# ^ django's premade user creation form, we dont need it since we're using UserRegisterForm
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
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
	if request.method == 'POST': #to check if we're passing in new data
		#the instance arguments are to auto populate current username and email
		#user form:
		u_form = UserUpdateForm(request.POST, instance=request.user)
		#profile form:
		p_form = ProfileUpdateForm(request.POST, request.FILES, #files for img
			                       instance=request.user.profile)
		if u_form.is_valid() and p_form.is_valid():
			u_form.save()
			p_form.save()
			messages.success(request, f"Your account has been updated!")
			return redirect('profile') #redirect from here to avoid "POST-GET redirect pattern"

	else: #else we don't save the data
		u_form = UserUpdateForm(instance=request.user)
		p_form = ProfileUpdateForm(instance=request.user.profile)

	#context ∴ for views
	context = {
		'u_form': u_form,
		'p_form': p_form
	}

	return render(request, 'users/profile.html', context)