from django.urls import path
from siyam_portfolio.views import siyam_portfolio_view

urlpatterns = [

    path('siyam/', siyam_portfolio_view, name='siyam'),
]