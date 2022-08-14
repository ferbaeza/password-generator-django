from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.
def test(request):
    return HttpResponse("Hello")

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, "about.html")


def password(request):

    lenght= int((request.GET.get('lenght', 10))) 
    print(lenght)

    characters = list('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    generate_password=''

    if request.GET.get('special'):
        characters.extend(list('!@#$%&*?/-_=+'))
    if request.GET.get('numbers'):
        characters.extend(list('0123456789'))

    for x in range(lenght):
        generate_password += random.choice(characters)

    return render(request, 'password.html', {'password':generate_password})