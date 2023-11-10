from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def kohli(request):
    return render(request,'kohli.html')

def abd(request):
    return HttpResponse("<h1> MR. 360 </h1>")
