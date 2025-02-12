from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView , TemplateView
from .models import Portfolio , Category
from team.models import Team
from django.core.paginator import Paginator

# Create your views here.

# class Portfolioes(TemplateView):
#     template_name = "portfolio/portfolio.html"




class Portfolioes(ListView):
    model = Portfolio
    template_name = 'portfolio/portfolio.html'
    context_object_name = "portfolios"
    paginate_by = 1

    def get_queryset(self):
        if self.kwargs.get("cat"):
            portfolios = self.model.objects.filter(category__title=self.kwargs.get("cat"), status=True)
        elif self.kwargs.get("search"):
            portfolios = self.model.objects.filter()
        elif self.request.GET.get("search"):
            search = self.request.GET.get("search")
            portfolios = self.model.objects.filter(title=search, status=True)
        else:
            portfolios = self.model.objects.filter(status=True)
        return portfolios
    


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["category"] = Category.objects.filter(status = True)
        context["agents"] = Team.objects.filter(status = True)[:3]
        first = 1
        service_paginate = Paginator(self.get_queryset(), 1)
        last = service_paginate.num_pages
        context ['first'] = first
        context ['last'] = last
        return context



def portfolio_detail(request):
    pass