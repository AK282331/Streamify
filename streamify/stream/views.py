from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import user_profile, movies, watchlist,userlist,genre,movie_genre
from datetime import datetime, timedelta

# Create your views here.

def landingpage(request):
    mov = movies.objects.all()
    context = {
        "mov":mov
    }
    return render(request,'stream/landingpage.html',context)


def homepage(request):
    movies_list = movies.objects.filter(type = 0)
    series_list = movies.objects.filter(type = 1)
    
    context={
        'movies':movies_list,
        'series':series_list
    }
    return render(request,'stream/homepage.html',context)

def stream_movies(request):
    return redirect("register")

def series(request):
    return redirect("register")

def genres(request):
    return redirect("register")

def mylistmovies(request,id):
    if userlist.objects.filter(movie_id=id).exists():
        return redirect("mylist")
    else:
        u = userlist(user_id = request.user.id, movie_id = id )
        u.save()
        return redirect('homepage')

def mylist(request):
    li = userlist.objects.filter(user_id = request.user.id)
    
    context = {
        "mylis":li
    }
    
    return render(request,'stream/mylist.html',context)

def profile(request):
    return render(request,'stream/profile.html')

def delete_user(request):
    user = request.user
    user.is_active = False
    user.save()
    return redirect('landingpage')

def update_profile(request):
    if request.method == 'POST':
        first_name = request.POST["FirstName"]
        last_name = request.POST["LastName"]
        dob = request.POST["birth"]
        phone = request.POST["contact"]
        city = request.POST["city"]
        state = request.POST["state"]
        pincode = request.POST["pincode"]
        genre = request.POST["genre"]
        email = request.POST["email"]
        if User.objects.filter(username = email).exists():
            u = User.objects.get(username = email)
            user_u = user_profile.objects.get(user_id = u.id)
            user_u.dob = dob
            user_u.phone_number = phone
            user_u.city = city
            user_u.state = state
            user_u.pincode = pincode
            user_u.Genre_preference = genre
            user_u.save()
            return redirect('profile')
        else:
            
            pass  

        
    else:
         
        return render (request,'stream/updateprofile.html')

def movies_prof(request):
    mo = movies.objects.filter(type = 0)
    context = {
        'mo':mo
    }
    return render(request,'stream/movies_prof.html',context)

def series_prof(request):
    se = movies.objects.filter(type = 1)
    context = {
        'se':se
    }
    return render(request,'stream/series_prof.html',context)

def genres_prof(request):
    action = movie_genre.objects.filter(genre_id = 1)
    adventure = movie_genre.objects.filter(genre_id = 2)
    sci = movie_genre.objects.filter(genre_id = 3)
    thriller = movie_genre.objects.filter(genre_id = 4)
    superhero = movie_genre.objects.filter(genre_id = 5)
    drama = movie_genre.objects.filter(genre_id = 6)
    horror = movie_genre.objects.filter(genre_id = 7)
    crime = movie_genre.objects.filter(genre_id = 8)    
    fantasy = movie_genre.objects.filter(genre_id = 9)
    context = {
        "action":action,
        "horror":horror,
        "adventure":adventure,
        "sci":sci,
        "thriller":thriller,
        "superhero":superhero,
        "drama":drama,
        "crime":crime,
        "fantasy":fantasy
    }
    
    return render(request,'stream/genre_prof.html',context)

def watch(request,id):
    movie_id = id
    user = request.user
    start_time = datetime.now()
    end_time = datetime.now() + timedelta(minutes=40)
    wat = watchlist(movie_id = movie_id, user_id = user.id, start_time = start_time, end_time = end_time)
    wat.save()
    return redirect('mylistmovies',id)
    
def dashboard(request):
    return render(request,'stream/dashboard.html')

