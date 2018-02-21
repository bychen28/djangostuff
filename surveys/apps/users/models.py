from __future__ import unicode_literals

from django.db import models

# Create your models here.

class UserManager(models.Manager):
	def basic_validator(self, postData):
		errors = {}
		if len(postData['name']) < 1:
			errors['name'] = 'Name field left blank!'
		if len(postData['email']) < 1:
			errors['email'] = 'Email field left blank'
		return errors

class User(models.Model):
	"""docstring fos User"""
	name = models.CharField(max_length = 255)
	email = models.CharField(max_length = 255)
	created_at = models.DateTimeField(auto_now_add = True)
	objects = UserManager()