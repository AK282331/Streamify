from django.shortcuts import render, redirect
from stream.models import user_profile
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout
# Create your views here.

def register(request):
    if request.method == 'POST':
        firstname = request.POST['FirstName']
        lastname = request.POST['LastName']
        dob = request.POST['birth']
        email = request.POST['email']
        password = request.POST['password']
        contact = request.POST['contact']
        city = request.POST['city']
        state = request.POST['state']
        pincode = request.POST['pincode']
        genre_preference = request.POST['genre']
        gender = request.POST['gender']
        user = User.objects.create_user(username=email, first_name = firstname, last_name = lastname)
        user.set_password(password)
        user.save()
        user_p = user_profile(user=user,dob = dob,phone_number = contact, city = city, state = state, 
                            pincode=pincode, Genre_preference=genre_preference, Gender = gender)
        user_p.save()
        return redirect("login")
    else:
        return render(request, 'authenticate/register.html')

def login_user(request):
    if request.method == 'POST':
        username = request.POST['email']
        password = request.POST['password']
        authenticated_user = authenticate(request,username = username, password = password)
        if authenticated_user is not None:
            login(request, authenticated_user)
            return redirect("homepage")
        else:
            return render(request,"authenticate/login.html")
        
    return render(request,'authenticate/login.html')