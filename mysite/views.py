from django.shortcuts import render
from django.http import HttpResponse
from gallery.models import Gallery


def home(request):
    items=Gallery.objects
    return render(request,'home.html',{'items':items})