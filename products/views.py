from django.shortcuts import render
from django.http import HttpResponse
from .models import Phone  # Importing the Phone model from models.py

# Create your views here.



# /products
def index(request):

    phones = Phone.objects.all().order_by('price')  # Fetch all phone objects from the database
  
    return render(request, 'products/index.html', {'phones': phones})  # Render the index template