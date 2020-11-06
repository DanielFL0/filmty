from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import ForumUser, Movie, Review

# Create your views here.
def index(request):
    latest_movies_list = Movie.objects.order_by('release_date')[:8]
    context = {'latest_movies_list': latest_movies_list}
    return render(request, 'films/index.html', context)

def catalog(request):
    latest_movies_list = Movie.objects.order_by('name')[:30]
    context = {'latest_movies_list': latest_movies_list}
    return render(request, 'films/catalog.html', context)

@login_required
def movie(request, movie_id):
    movie_result = Movie.objects.get(pk=movie_id)
    reviews = Review.objects.all().filter(movie=movie_result)
    context = {'movie': movie_result, 'reviews': reviews}
    return render(request, 'films/movie.html', context)

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
    return render(request, 'films/login.html')

def user_register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        user = User.objects.create_user(username=username, email=email, password=password)
    return render(request, 'films/register.html')