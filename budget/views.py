# Create your views here.
from django.http import HttpResponse, Http404, HttpResponseBadRequest
from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User

@login_required 
def index(request):
    return HttpResponse("Logged in")

def user_login(request):
    return render(request, 'login.html', {})

@csrf_exempt
@require_POST
def login_auth(request):
    data = request.POST
    user = authenticate(username=data['username'], password=data['password'])
    if user is None:
         raise Http404

    login(request, user)
    return redirect('/')

def new_user(request):
    return render(request, 'create_user.html', {})

@csrf_exempt
@require_POST
def create_user(request):
    data = request.POST
    print data
    try:
        user = User.objects.create_user(data['username'], data['email'], data['password'])
        user.save()
        
        user = authenticate(username=data['username'], password=data['password'])
        login(request, user)
    except:
        return HttpResponseBadRequest("username duplicate")

    return redirect('/')




