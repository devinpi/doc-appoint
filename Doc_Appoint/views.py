import json
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from .models import *


def index(request):
    return render(request, "Doc_Appoint/index.html", {})
    # return HttpResponse("Hello, world!")

def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "Doc_Appoint/login.html", {
                "message": "Invalid username and/or password. Try Again!!"
            })
    else:
        return render(request, "Doc_Appoint/login.html", {})

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))

def register(request, user_selection):
    if user_selection == 'personal' or user_selection == "doctor":
        if request.method == "POST":
            username = request.POST['username']
            email = request.POST['email']
            password = request.POST['password']
            confirmation = request.POST['confirmation']
            user_type = user_selection
            if password != confirmation:
                return render(request, "Doc_Appoint/register.html", {
                    "message": "Passwords entered do not match"
                })
            try:
                user = User.objects.create_user(username, email, password)
                user.save()
                # fix this
                user.user_type = user_selection
            except IntegrityError:
                return render(request, "Doc_Appoint/register.html", {
                    "message": "Username already taken"
                })
            if user_selection == 'doctor':
                login(request, user, backend='django.contrib.auth.backends.ModelBackend')
                return HttpResponseRedirect(reverse('next'))
            else:
                return HttpResponseRedirect(reverse('index'))
        else:
            return render(request, "Doc_Appoint/register.html", {})
    else:
        return HttpResponse("error")

def select(request):
    return render(request, "Doc_Appoint/selection.html")


def next_steps(request):
    return render(request, "Doc_Appoint/doc_next_steps.html")