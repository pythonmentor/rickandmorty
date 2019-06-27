

from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    """
        This views return the home page
    """
    return render(request, "app/index.html")

def content(request):
    """
        this views return the application content
    """
    context = {'key': 156835} # Context variable for html files
    return render(request, "app/content.html", context)