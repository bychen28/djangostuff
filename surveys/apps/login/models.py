from __future__ import unicode_literals
import re
from django.db import models

name_regex = re.compile(r'^[a-zA-Z]+$')
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
# Create your models here.
class Uzer(object):
	"""docstring for User"""
	fname = models.CharField(max_length = 255)
	lname = models.CharField(max_length = 255)
	email = models.CharField(max_length = 255)
	pword = models.CharField(max_length = 255)
	created_at = models.DateTimeField(auto_now_add = True)


