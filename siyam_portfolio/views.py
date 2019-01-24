from django.shortcuts import render


def siyam_portfolio_view(request):
    template = 'siyam_portfolio_info/portfolio.html'
    return render(request, template)
