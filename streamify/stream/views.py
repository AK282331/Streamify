from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import user_profile, movies, watchlist
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

def mylist1(request,id):
    myl = movies.objects.filter(id = id)
    context = {
        "mylis":myl
    }
    return render(request,'stream/mylist.html',context)

def mylist2(request):
    return render(request,'stream/mylist.html')

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
    
    return render(request,'stream/genre_prof.html')

def watch(request,id):
    movie_id = id
    user = request.user
    start_time = datetime.now()
    end_time = datetime.now() + timedelta(minutes=40)
    wat = watchlist(movie_id = movie_id, user_id = user.id, start_time = start_time, end_time = end_time)
    wat.save()
    return redirect('mylist2')
    
def dashboard(request):
    return render(request,'stream/dashboard.html')

