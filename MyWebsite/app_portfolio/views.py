from django.shortcuts import render
from .models import Category, Portfolio


def portfolio_page(request):
    portfolio_category = Category.objects.filter(is_draft=False)
    portfolio = Portfolio.objects.filter(is_draft=False)

    return render(request, 'paginas/portfolio.html', {'portfolio_category': portfolio_category, 'portfolio': portfolio})


def portfolio_details(request, portfolio_id):
    item = Portfolio.objects.get(id=portfolio_id)
    context = {
        'item': item
    }
    return render(request, 'portfolio/portfolio-details.html', context)


def pizzeria_page(request):

    return render(request, 'portfolio/pizzeria/PaginaWEB.html', {})

