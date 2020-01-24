from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request,'home.html')

def send(request):
    #file=open('D:/message.txt','w')
    #file.write(request.GET['text'])
    #file.close()
    return HttpResponse('我会看到的')
