from django.shortcuts import render, redirect
from .models import Gowns
from django.contrib.auth.models import User, auth
from django.contrib import messages

# Create your views here.

def index(request):
    gowns = Gowns.objects.all()
    return render(request, "index.html", {'gowns': gowns})



