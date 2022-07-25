from django.shortcuts import render
from .models import House


def home(request):
    houses = House.objects.all()
    return render(request, 'home.html', {'houses': houses})
    
def search_house(request):
    
    if request.method == 'POST':
    
        searched = request.POST['searched']
        return render(request, 'search.html', {'searched':searched})
    else:
        return render(request, 'search.html')