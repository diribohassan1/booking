from django.shortcuts import render, redirect
from .models import Gowns
from .models import Page_inf
from django.contrib.auth.models import User, auth
from django.contrib import messages

# Create your views here.

def index(request):
    gowns = Gowns.objects.all()
    return render(request, "index.html", {'gowns': gowns})


def aboutus(request):
    page_inf = Page_inf.objects.get(pk=1)
    context = {'page_inf': page_inf}
    return render(request, "aboutus.html", context )


