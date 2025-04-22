from django.contrib import admin
from .models import Product, Portfolio, PaymentDelivery, Contact

admin.site.register(Product)
admin.site.register(Portfolio)
admin.site.register(PaymentDelivery)
admin.site.register(Contact)
