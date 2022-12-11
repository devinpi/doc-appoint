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


# Create your views here.

def index(request):
    return render(request, "Doc_Appoint/index.html", {})
    # return HttpResponse("Hello, world!")

def login_view(request):
    return render(request, "Doc_Appoint/login.html", {})

def logout_view(request):
    return HttpResponseRedirect(reverse("index"))


def register(request):
    return render(request, "Doc_Appoint/register.html", {})
     