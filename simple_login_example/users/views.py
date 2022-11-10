from django.shortcuts import render
from django.http import HttpResponse

# models
from users.models import User

# Create your views here.


def login(request):
    user = User.objects.get(id=1)
    return HttpResponse(f'username is {user.username}, password is {user.password}')
