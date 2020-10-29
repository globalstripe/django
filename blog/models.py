from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)

    # on_delete=models.CASCASDE  // This deletes all posts by the user
    # if the user is deleted!
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs = {'pk': self.pk})

class Movie(models.Model):
    movieTitle = models.CharField(max_length=100)
    synopsis = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    imdbUrl = models.URLField(default='https://imdb.com')
    movieUrl = models.URLField(default='https://imdb.com')
    youtubeUrl = models.URLField(default='https://imdb.com')

    # on_delete=models.CASCASDE  // This deletes all posts by the user
    # if the user is deleted!
    createdBy = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.movieTitle

