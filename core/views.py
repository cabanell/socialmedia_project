from django.shortcuts import render

def home(request):
    return render(request, 'core/home.html')

def portfolio(request):
    return render(request, 'core/portfolio.html')

def faq(request):
    return render(request, 'core/faq.html')

def prices(request):
    return render(request, 'core/prices.html')

def contact(request):
    return render(request, 'core/contact.html')
