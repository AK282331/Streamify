from django.shortcuts import render, redirect
from stream.models import genre, actor, movies, movie_genre, movie_actor

# Create your views here.

def addgenre(request):
    if request.method == 'POST':
        genre_name = request.POST['genrenew']
        gen = genre(genre_name = genre_name)
        gen.save()
        return redirect("addgenre")
    else:
        return render(request,"admin/addgenre.html")


def addactor(request):
    if request.method == 'POST':
        actorname = request.POST['actorname']
        dob = request.POST['dob']
        awards = request.POST['awards']
        gender = request.POST['gender']
        act = actor(actor_name = actorname, dob = dob, gender = gender, awards= awards)
        act.save()
        return redirect("addactor")
    else:
        return render(request,"admin/addactor.html")
        
def addmovie(request):
    if request.method == "POST":
        movie_name = request.POST['moviename']
        duration = request.POST['duration']
        ratings =   request.POST['ratings']
        release_date = request.POST['release']
        type = request.POST['ms']
        image = request.FILES['image']
        if movies.objects.filter(movie_name=movie_name).exists():
            return redirect('addmovie')
        else:
            movie = movies(movie_name = movie_name, duration = duration, ratings = ratings, release_date = release_date, type = type, image = image)
            movie.save()
        
        genre1 = request.POST['genre1']
        genre2 = request.POST['genre2']
        genre3 = request.POST['genre3']
        genre4 = request.POST['genre4']
        
        if genre.objects.filter(genre_name = genre1).exists():
            g1 = genre.objects.get(genre_name = genre1)
            mg1 =  movie_genre(movie_id = movie.id, genre_id = g1.id)
            mg1.save()
        else:
            pass
            
        if genre.objects.filter(genre_name = genre2).exists():
            g2 = genre.objects.get(genre_name = genre2)
            mg2 =  movie_genre(movie_id = movie.id, genre_id = g2.id)
            mg2.save()
        else:
            pass
        
        if genre.objects.filter(genre_name = genre3).exists():
            g3 = genre.objects.get(genre_name = genre3)
            mg3 =  movie_genre(movie_id = movie.id, genre_id = g3.id)
            mg3.save()
        else:
            pass
        
        if genre.objects.filter(genre_name = genre4).exists():
            g4 = genre.objects.get(genre_name = genre4)
            mg4 =  movie_genre(movie_id = movie.id, genre_id = g4.id)
            mg4.save()
        else:
            pass

        actor1 = request.POST['actor1']
        actor2 = request.POST['actor2']
        actor3 = request.POST['actor3']
        actor4 = request.POST['actor4']
        
        if actor.objects.filter(actor_name = actor1).exists():
            a1 = actor.objects.get(actor_name = actor1)
            ma1 = movie_actor(movie_id = movie.id, actor_id = a1.id)
            ma1.save()
        else:
            pass
        
        if actor.objects.filter(actor_name = actor2).exists():
            a2 = actor.objects.get(actor_name = actor2)
            ma2 = movie_actor(movie_id = movie.id, actor_id = a2.id)
            ma2.save()
        else:
            pass
        
        if actor.objects.filter(actor_name = actor3).exists():
            a3 = actor.objects.get(actor_name = actor3)
            ma3 = movie_actor(movie_id = movie.id, actor_id = a3.id)
            ma3.save()
        else:
            pass
        
        if actor.objects.filter(actor_name = actor4).exists():
            a4 = actor.objects.get(actor_name = actor4)
            ma4 = movie_actor(movie_id = movie.id, actor_id = a4.id)
            ma4.save()
        else:
            pass
        return redirect('addmovie')
    else:
        return render(request,"admin/addmovie.html")
        
        