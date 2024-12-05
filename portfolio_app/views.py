# views.py
from django.shortcuts import render

def portfolio(request):
    return render(request, 'portfolio_app/portfolio.html')  # Рендерим шаблон
