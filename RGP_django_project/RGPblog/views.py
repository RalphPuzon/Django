from django.shortcuts import render  #for importing templates
from .models import Post #import models file from same directory
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
	ListView,
	DetailView,
	CreateView,
	UpdateView,
	DeleteView
)

# Create your views here. a view == a function below

# we map URL patters to these functions.
# to map: create a new module in RGPblog directory called "urls.py"
#		  where we will map the URLs to each view(function)

#FUNCTIONS:
# home:
"""* handles traffic from blog homepage, takes in HTTP request
   * return what we want user to see when they're sent to this route
   * where the logic goes for how we want to handle certain routes"""

"""
since this is a blog, let's add a few blog 'posts' using static pages
as a list of dictionaries:
"""

#function based view of home page:

def home(request):
	context = {
		'posts': Post.objects.all() #per the ORM query schema
	}
	return render(request, 'RGPblog/home.html', context)

# class based view of home:
class PostListView(ListView):
	# this sets the model type inherited to be a "Post" type:
	model = Post

	# the class defaults to looking for the template in 
	# <app>/<model>_<viewtype>.html. to change:
	template_name = "RGPblog/home.html" 

	# our posts are called posts' objects, 
	# we want the created views to have this property.
	context_object_name='posts'
	ordering = ['-date_posted'] #this will order posts from new to old


def about(request): #if context is short, pass in function ok
	return render(request, 'RGPblog/about.html', {'title': "About:"})

class PostDetailView(DetailView):
	#view the individual blog post
	model = Post
	 
class PostCreateView(LoginRequiredMixin,CreateView): #THE ARG ORDER IS IMPORTANT!
	#create a new post
	model = Post
	fields = ['title', 'content']
	def form_valid(self, form):
		#set currently logged in user as author
		form.instance.author = self.request.user
		return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView): #THE ARG ORDER IS IMPORTANT!
	#securely update a post
	model = Post
	fields = ['title', 'content']
	def form_valid(self, form):
		#set currently logged in user as author
		form.instance.author = self.request.user
		return super().form_valid(form)

	def test_func(self):
		post = self.get_object()
		#if logged in is also author:
		if self.request.user == post.author:
			return True
		return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	#delete the blog post
	model = Post
	success_url='/'


	def test_func(self):
		post = self.get_object()
		#if logged in is also author:
		if self.request.user == post.author:
			return True
		return False