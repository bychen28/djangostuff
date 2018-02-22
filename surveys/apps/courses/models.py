from __future__ import unicode_literals

from django.db import models

# Create your models here.
class CourseManager(models.Manager):
	def basic_validator(self, postData):
		errors = {}
		if len(postData['name']) < 6:
			errors['name'] = 'Name field should be more than 5 characters!'
		if len(postData['desc']) < 1:
			errors['desc'] = 'Description field should be more than 20 characters'

		return errors
class Course(models.Model):
	name = models.CharField(max_length = 255)
	desc = models.TextField()
	created_at = models.DateTimeField(auto_now_add = True)
	objects = CourseManager()
		