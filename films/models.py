from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class ForumUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.FileField(upload_to='profile_pictures')

    def __str__(self):
        return self.username

class Movie(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    release_date = models.DateTimeField('release date')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    thumbnail = models.FileField(upload_to='thumbnails')
    video = models.FileField(upload_to='videos')

    def __str__(self):
        return self.name

class Review(models.Model):
    content = models.CharField(max_length=1200)
    date_published = models.DateTimeField('date published')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

    def __str__(self):
        return self.content