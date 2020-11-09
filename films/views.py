from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import ForumUser, Category, Movie, Review
from datetime import datetime

# Create your views here.
def index(request):
    logged_in = False
    user = None
    if request.user.is_authenticated:
        logged_in = True
        user = request.user
    latest_movies_list = Movie.objects.order_by('release_date')[:8]
    action = Category.objects.get(name='action')
    action_movies_list = Movie.objects.all().filter(category=action)
    context = {'latest_movies_list': latest_movies_list, 'action_movies_list': action_movies_list, 'logged_in': logged_in, 'user': user}
    return render(request, 'films/index.html', context)

def catalog(request):
    logged_in = False
    user = None
    if request.user.is_authenticated:
        logged_in = True
        user = request.user
    latest_movies_list = Movie.objects.order_by('name')[:30]
    categories = Category.objects.all()
    context = {'latest_movies_list': latest_movies_list, 'categories': categories, 'logged_in': logged_in, 'user': user}
    if request.method == 'POST':
        selected_category = Category.objects.get(name=request.POST['category'])
        movie_results = Movie.objects.all().filter(category=selected_category)
        context['latest_movies_list'] =  movie_results
    return render(request, 'films/catalog.html', context)

@login_required(login_url='/films/login/')
def movie(request, movie_id):
    user = request.user
    movie_result = Movie.objects.get(pk=movie_id)
    categories = movie_result.category.all()
    reviews = Review.objects.all().filter(movie=movie_result)
    context = {'movie': movie_result, 'categories': categories, 'reviews': reviews, 'user': user}
    return render(request, 'films/movie.html', context)

# @login_required(login_url='/films/login/')
# def add_review(request, movie_id):


@login_required(login_url='/films/login/')
def add_movie(request, user_id):
    if request.method == 'POST':
        name = request.POST['name']
        description = request.POST['description']
        category = request.POST['category']
        thumbnail = request.FILES['thumbnail']
        video = request.FILES['video']
        cat = Category.objects.get(name=category)
        user = User.objects.get(pk=user_id)
        release_date = datetime.now()
        movie = Movie(name=name, description=description, release_date=release_date, user=user, thumbnail=thumbnail, video=video)
        movie.save()
        movie.category.add(cat)
    return render(request, 'films/add_movie.html')
    
def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/films/')
    return render(request, 'films/login.html')

def user_register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        user = User.objects.create_user(username=username, email=email, password=password)
        return HttpResponseRedirect('/films/')
    return render(request, 'films/register.html')

def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/films/')

@login_required(login_url='/films/login/')
def user_profile(request, user_id):
    is_own_profile = False
    user = request.user
    requested_user = User.objects.get(pk=user_id)
    movies = Movie.objects.all().filter(user=requested_user)
    context = {'user': user, 'movies': movies, 'requested_user': requested_user, 'is_own_profile': is_own_profile}
    if user.username == requested_user.username:
        is_own_profile = True
        context['is_own_profile'] = is_own_profile
    return render(request, 'films/profile.html', context)