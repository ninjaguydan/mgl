from django.http.response import HttpResponse
from django.shortcuts import render, redirect, HttpResponse

# Create your views here.
def index(request):
    return render(request,"base.html")