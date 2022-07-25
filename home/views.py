from django.shortcuts import render
from .models import House


def home(request):
    houses = House.objects.all()
    return render(request, 'home.html', {'houses': houses})
    
<<<<<<< HEAD
def search_house(request):
    
    if request.method == 'POST':
    
        searched = request.POST['searched']
        return render(request, 'search.html', {'searched':searched})
    else:
        return render(request, 'search.html')
=======
def post(request, detail_id):
    postid = House.objects.get(pk=detail_id)
    return render(request, 'post_detail.html', 
    {"postid":postid}) 
>>>>>>> 1d4d21a8b8a50eebdb0b5b3d659410afd9d68b40
