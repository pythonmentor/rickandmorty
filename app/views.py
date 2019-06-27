from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    """
    """
    return render(request, "app/index.html")

def content(request):
    """
    """
    context = {'key': 156835} # Context variable for html files
    return render(request, "app/content.html", context)