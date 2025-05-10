from django.shortcuts import render, redirect
import json
import os
from django.contrib import messages
from django.conf import settings
from .models import Product, Contact

def home(request):
    return render(request, 'home.html')

def products(request):
    products = Product.objects.all()
    return render(request, 'products.html', {'products': products})

def portfolio(request):
    json_path = os.path.join(settings.BASE_DIR, 'reviews.json')
    reviews = []
    if os.path.exists(json_path):
        try:
            with open(json_path, 'r', encoding='utf-8') as f:
                reviews = json.load(f)
        except (json.JSONDecodeError, IOError) as e:
            print(f"Ошибка загрузки JSON-файла: {e}")
    return render(request, 'portfolio.html', {'reviews': reviews})

def payment_delivery(request):
    return render(request, 'payment_delivery.html')

def contacts(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        phone = request.POST['phone']
        message = request.POST['message']
        Contact.objects.create(first_name=first_name, last_name=last_name, phone=phone, message=message)
        messages.success(request, "Спасибо! Ваша заявка принята.")
        return redirect('contacts')
    return render(request, 'contacts.html')

def urgent_print(request):
    return render(request, 'urgent_print.html')

def offset_print(request):
    return render(request, 'offset_print.html')

def wide_format(request):
    return render(request, 'wide_format.html')

def interior_print(request):
    return render(request, 'interior_print.html')

def canvas_print(request):
    return render(request, 'canvas_print.html')

def format_print(request):
    return render(request, 'format_print.html')