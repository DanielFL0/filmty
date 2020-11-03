from django.shortcuts import render
from .models import User, Movie, Review

# Create your views here.
def index(request):
    latest_movies_list = Movie.objects.order_by('release_date')[:5]
    context = {'latest_movies_list': latest_movies_list}
    return render(request, 'films/index.html', context)