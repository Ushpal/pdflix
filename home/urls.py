from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("", views.index, name='home'),
    path("about", views.about, name='about'),
    path("services", views.services, name='services'),
    path("contact", views.contact, name='contact'), 
    path("pdfengine", views.pdfengine, name='contact'), 
    path("drive_link", views.drive_link, name='drivelink'), 
    path("youtube_link", views.youtube_link, name='youtube_link'), 
]