from django.db import models
from django.contrib.auth.models import User
from PIL import Image
# Create your models here.

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	#image field:
	image = models.ImageField(default="default.jpg", upload_to='profile_pics')

	def __str__(self):
		return f"{self.user.username} Profile"

	def save(self): #overwrite class save to add pfp rescaling
		super().save()

		img = Image.open(self.image.path)

		if img.height > 300 or img.width > 300: #force resize, need to make better
			output_size = (300,300)
			img.thumbnail(output_size)
			img.save(self.image.path)