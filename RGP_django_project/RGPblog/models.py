from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
#EACH CLASS IS ITS OWN TABLE IN THE DB
#make the posts DB:
class Post(models.Model):
	title = models.CharField(max_length=100)
	content = models.TextField() #unrestriced vs charfield
	date_posted = models.DateTimeField(default = timezone.now)  # auto_now=True (updates date whenever post is updated)	
															    # auto__now_add=True (auto add creation date, immutable)
																# default (custom specifier)
	author = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return self.title
