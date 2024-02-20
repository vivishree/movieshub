
from django.http import HttpResponse
from django.shortcuts import  render

from django.contrib.auth.models import User,auth


def ad(request):
    return render(request,'app1/index.html')

def  home(request):
    return render(request,'app1/homebtn.html')



def proo(request):
    return render(request,'app1/profile.html')
def ser(request):
    return render(request,'app1/search1.html')
def stream(request):
    return render(request,'app1/streaming.html')
def descp(request):
    return render(request,'app1/description.html')
def yaa(request):
    return render(request,'app1/yaararum.html')
def nadigayar(request):
    return render(request,'app1/nadigayar.html')

def kala(request):
    return render(request,'app1/kalakalappu.html')


def sark(request):
    return render(request,'app1/sarkar.html')

def About(request):
   
    return render(request,"app1/about.html")

