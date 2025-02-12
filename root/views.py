from django.shortcuts import render
from django.views.generic import TemplateView
from blogs.models import Blog
from services.models import Services
# Create your views here.

class Home(TemplateView): 
    template_name = "root/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['blogs'] = Blog.objects.filter(status = True)[:3]
        context['services'] = Blog.objects.filter(status = True)[:4]
        return context

def about(request):
    pass

def contactus(request):
    pass