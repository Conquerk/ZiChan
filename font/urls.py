from django.conf.urls import url, include
from django.contrib import admin
from font import views

urlpatterns = [
    url(r'check/',views.Check,name='check'),
]