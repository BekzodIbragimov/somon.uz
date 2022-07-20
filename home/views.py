from django.shortcuts import render
from .models import House
def home(request):
    houses = House.objects.all()
    return render(request, 'home.html', {'houses': houses})
    
