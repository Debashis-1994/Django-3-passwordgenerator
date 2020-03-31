from django.shortcuts import render
from django.http import HttpResponse
import random


# Create your views here.
def home(request):
    return render(request,'generator/home.html')
def aboutme(request):
    return render(request,'generator/aboutme.html')

def password(request):
    thepassword=''
    characters=list('abcdefghijklmnopqrstuvwxyz')
    length=int(request.GET.get('length',12))

    if request.GET.get('uppercase') :
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))


    if request.GET.get('Special') :
        characters.extend(list('!@#$%^&*_'))

    if request.GET.get('Numbers') :
        characters.extend(list('!@#$%^&*_'))



    for x in range(length):
        thepassword+=random.choice(characters)
    return render (request,'generator/password.html',{'password':thepassword})
