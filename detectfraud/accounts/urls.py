
from django.conf.urls import url
from . import views
from django import forms
from django.contrib.auth.views import login

urlpatterns = [
    url(r'^$', views.home),
    url(r'^login/$', login, {'template_name': 'accounts/login.html'}),
    url(r'^register/$', views.register, name='register'),
    ]