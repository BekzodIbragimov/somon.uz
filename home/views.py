from django.shortcuts import render
from .models import House
def home(request):
    houses = House.objects.all()
    return render(request, 'home.html', {'houses': houses})
    
def post(request, detail_id):
    postid = House.objects.get(pk=detail_id)
    return render(request, 'post_detail.html', 
    {"postid":postid}) 