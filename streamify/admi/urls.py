
from django.urls import path
from .views import addgenre,addactor,addmovie

urlpatterns = [
    path("addgenre",addgenre,name = 'addgenre'),
    path("addactor",addactor,name = 'addactor'),
    path("addmovie",addmovie,name = 'addmovie'),
    
]