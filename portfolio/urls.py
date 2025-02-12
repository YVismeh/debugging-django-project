from django.urls import path
from .views import *

app_name = "portfolio"

urlpatterns = [
    path('', Portfolioes.as_view(), name="portfolios"),
    path('category/<str:cat>', Portfolioes.as_view(), name="portfolios-withcategory"),
    path('detail/<int:id>', portfolio_detail, name="portfolio_detail"),
]