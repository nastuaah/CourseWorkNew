"""
URL configuration for coursework project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('home/', views.home, name='home'),
    path('products/', views.products, name='products'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('payment-delivery/', views.payment_delivery, name='payment_delivery'),
    path('contacts/', views.contacts, name='contacts'),
    path('urgent-print/', views.urgent_print, name='urgent_print'),
    path('offset-print/', views.offset_print, name='offset_print'),
    path('wide-format/', views.wide_format, name='wide_format'),
    path('interior-print/', views.interior_print, name='interior_print'),
    path('canvas-print/', views.canvas_print, name='canvas_print'),
    path('format-print/', views.format_print, name='format_print'),
]
