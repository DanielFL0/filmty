from django.urls import path
from . import views

app_name = 'films'
urlpatterns = [
    path('', views.index, name='index'),
    path('catalog/', views.catalog, name='catalog'),
    path('movie/<int:movie_id>/', views.movie, name='movie'),
    path('login/', views.user_login, name='login'),
    path('register/', views.user_register, name='register'),
    path('logout/', views.user_logout, name='logout'),
    path('profile/<int:user_id>', views.user_profile, name='profile'),
    path('profile/<int:user_id>/add_movie', views.add_movie, name='add_movie'),
    path('movie/<int:movie_id>/add_review', views.add_review, name='add_review'),
]