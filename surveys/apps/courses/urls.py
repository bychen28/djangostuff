from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
	url(r'^$', views.index),     # This line has changed!
	url(r'^/(?P<ids>\d+)/destroy$', views.show),
	url(r'^/(?P<ids>\d+)/delete$', views.delete),
	url(r'^/add$', views.create)
]