from audioop import reverse
from email import message
import imp
from django.db import IntegrityError
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from . models import Dairy

# Create your views here.


def index(request):
    if not request.user.is_authenticated:
        return render(request, "data/login.html")
    return render(request, "data/home.html",{
        'dairy': Dairy.objects.all()
    })


def register(request):
    if request.method == "POST":
        try:
            username = request.POST['username']
            password = request.POST['password']
            user = User.objects.create_user(
                username=username, password=password
            )

            return render(request, "data/login.html", {
                "message": 'Registered Successfully'
            })

        except ValueError:
            return render(request, "data/register.html", {
                "message": "Username and password can't be empty.!"
            })

        except IntegrityError:
            return render(request,'data/register.html',{
                "message":"Username already taken try other username."
            })
            
    return render(request, "data/register.html")


def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request,user)
            return render(request,"data/home.html",{
                'dairy':Dairy.objects.all()
            })
        else:
            return render(request,"data/login.html",{
                "message":"Invalid Credentials"
            })
    return render(request,"data/login.html")

