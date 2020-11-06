from django.urls import path
from . import views

app_name = 'films'
urlpatterns = [
    path('', views.index, name='index'),
    path('catalog/', views.catalog, name='catalog'),
    path('movie/<int:movie_id>/', views.movie, name='movie'),
    path('login/', views.user_login, name='login'),
    path('register/', views.user_register, name='register'),
]