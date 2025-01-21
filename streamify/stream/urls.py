from django.contrib import admin
from django.urls import path
from .views import landingpage, homepage, stream_movies, series, genres, mylist1, profile, delete_user,update_profile, movies_prof, series_prof, genres_prof,watch,dashboard, mylist2

urlpatterns = [
 path("", landingpage,name = "landingpage"),
 path("homepage", homepage,name = "homepage"),
 path("movies", stream_movies, name = "movies"),
 path("series", series, name = "series"),
 path("genres", genres, name = "genres"),
 path("mylist<int:id>", mylist1, name = "mylist"),
 path("mylist2", mylist2, name = "mylist2"),
 path("profile",profile, name="profile"),
 path("delete_user", delete_user, name="delete_user"),
 path("update_profile",update_profile, name="update_profile"),
 path("movies_prof", movies_prof, name="movies_prof"),
 path("series_prof",series_prof, name="series_prof"),
 path("genres_prof",genres_prof, name="genres_prof"),
 path("watch/<int:id>",watch,name="watch"),
 path("dashboard",dashboard, name="dashboard"),
 
]