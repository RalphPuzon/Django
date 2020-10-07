from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm #django's premade user creation form
from django.contrib import messages

def register(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save() #saves the info and crates the user
			username = form.cleaned_data.get('username')
			messages.success(request, f"Account created for {username}!")
			return redirect('blog-home')
	else:	
		form = UserCreationForm()

	return render(request, 'users/register.html', {'form': form})