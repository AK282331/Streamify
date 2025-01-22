from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class user_profile(models.Model):
  user = models.OneToOneField(User,on_delete=models.CASCADE)
  dob = models.DateField(blank=False, null=False)
  phone_number = models.BigIntegerField(null=False, blank=False,unique=True)
  city = models.CharField(max_length=100, blank=False, null=False)
  state = models.CharField(max_length=100, blank=False, null = False)
  pincode = models.BigIntegerField(null=False, blank=False)
  Genre_preference = models.CharField(max_length=100, blank=False, null=False)
  Gender = models.CharField(max_length=50, blank=False,null=False)

  def __str__(self):
    return self.user.__str__()
    
class movies(models.Model):
  movie_name = models.CharField(max_length=300, null=False, blank=False)
  duration = models.TimeField(null=False, blank=False)
  ratings = models.FloatField(null=False, blank=False)
  release_date = models.DateField(null=False, blank=False)
  type = models.IntegerField(blank=False, null=False)
  image = models.ImageField(upload_to="movie_images",null=False, blank=False)
  
  def __str__(self):
    return self.movie_name
    
class genre(models.Model):
  genre_name = models.CharField(max_length=100, blank=False, null=False)
  
  def __str__(self):
    return self.genre_name
  
class actor(models.Model):
  actor_name = models.CharField(max_length=100, blank=False, null=False)
  dob = models.DateField(null=False, blank=False)
  gender = models.CharField(max_length=50, blank=False,null=False)
  awards = models.IntegerField(null=False, blank=False)
  
  def __str__(self):
    return self.actor_name
    
class movie_genre(models.Model):
  movie = models.ForeignKey(movies, on_delete=models.CASCADE)
  genre = models.ForeignKey(genre, on_delete=models.CASCADE)
  
  def __str__(self):
    return self.movie
  
class movie_actor(models.Model):
  movie = models.ForeignKey(movies, on_delete=models.CASCADE)
  actor = models.ForeignKey(actor, on_delete=models.CASCADE)
  
  def __str__(self):
    return self.movie

class watchlist(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  movie = models.ForeignKey(movies, on_delete=models.CASCADE)
  start_time = models.DateTimeField(null=False, blank=False)
  end_time = models.DateTimeField(null=False, blank=False)
  
  def __str__(self):
    return self.user
  
class userlist(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  movie = models.ForeignKey(movies, on_delete=models.CASCADE)
    
    
  def __str__(self):
    return self.user.__str__()