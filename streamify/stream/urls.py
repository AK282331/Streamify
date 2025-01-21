from django.contrib import admin
from django.urls import path
from .views import landingpage, homepage, stream_movies, series, genres, mylist, profile, delete_user,update_profile, movies_prof, series_prof, genres_prof,watch,dashboard, mylistmovies

urlpatterns = [
 path("", landingpage,name = "landingpage"),
 path("homepage", homepage,name = "homepage"),
 path("movies", stream_movies, name = "movies"),
 path("series", series, name = "series"),
 path("genres", genres, name = "genres"),
 path("mylist", mylist, name = "mylist"),
 path("mylistmovies/<int:id>", mylistmovies, name = "mylistmovies"),
 path("profile",profile, name="profile"),
 path("delete_user", delete_user, name="delete_user"),
 path("update_profile",update_profile, name="update_profile"),
 path("movies_prof", movies_prof, name="movies_prof"),
 path("series_prof",series_prof, name="series_prof"),
 path("genres_prof",genres_prof, name="genres_prof"),
 path("watch/<int:id>",watch,name="watch"),
 path("dashboard",dashboard, name="dashboard"),
 
]