from django.urls import path , include
from .views import *



app_name = "root"

urlpatterns = [
    path("", Home.as_view(), name="home"),
    path("contact", contactus, name="contact"),
    path("about", about, name="about"),
    
]