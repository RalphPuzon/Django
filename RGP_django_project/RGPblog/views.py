from django.shortcuts import render
from django.http import HttpResponse # <- we added this in

# Create your views here. a view == a function below

# we map URL patters to these functions.
# to map: create a new module in RGPblog directory called "urls.py"
#		  where we will map the URLs to each view(function)

#FUNCTIONS:
# home:
"""* handles traffic from blog homepage, takes in HTTP request
   * return what we want user to see when they're sent to this route
   * where the logic goes for how we want to handle certain routes"""

def home(request):
	return HttpResponse('<h1>RGP blog Home</h1>')

def about(request):
	return HttpResponse('<h1>RGP blog About</h1>')