from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
	url(r'^$', views.index),     # This line has changed!
	url(r'^/(?P<ids>\d+)$', views.show),
	url(r'^/new$', views.new),
	url(r'^/create$', views.create),
	url(r'^/(?P<ids>\d+)/edit$', views.edit),
	url(r'^/(?P<ids>\d+)/update$', views.update),
	url(r'^/(?P<ids>\d+)/destroy$', views.delete)

	]