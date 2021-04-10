from django.shortcuts import render
import os

def index(request):
    print(os.getcwd())
    return render(request, "index.html")
