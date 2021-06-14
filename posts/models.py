from django.db import models

# Create your models here.

class Post(models.Model): #we've created a new database model called post , with the field text database and specified the stored content using ,TextField().
	text = models.TextField()
	
	def __str__(self):
		return self.text[:50] # this will present the first 50 characters of the text field.
