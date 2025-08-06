from django.urls import path
from . import views

urlpatterns = [
    path('GetPhones',views.api_get_phones)
]

app_name = 'products'


# mundotech/products/urls.py
# This file defines the URL patterns for the products app, mapping the root URL to the index view.
# The index view will handle requests to the products page and return a welcome message.