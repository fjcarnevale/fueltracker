from django.conf.urls import url

from . import views

urlpatterns = [
  url(r'^$', views.index, name='index'),
  url(r'^model/(?P<model_name>[a-zA-Z0-9]+)$', views.model, name='model'),
  url(r'^make/(?P<make_name>[a-zA-Z]+)$', views.make, name='make'),
  url(r'^vehicle/(?P<vehicle_id>[0-9]+)$', views.vehicle, name='vehicle'),
  url(r'^login_user$', views.login_user, name='login_user'),
  url(r'^register$', views.register, name='register'),
  url(r'^addMake$', views.addMake, name='addMake'),
]
