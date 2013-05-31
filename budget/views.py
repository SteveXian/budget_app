# Create your views here.
from django.http import HttpResponse, Http404, HttpResponseBadRequest
from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from budget.models import BudgetUser, BudgetPlanningData
from budget.aux import format_data_for_view, initiate_user_preset_data
import re

DATA_ID_RE = '(?P<category>[a-zA-Z_]*)_(?P<year>\d)(?P<term>.)'

def user_login(request):
    return render(request, 'login.html', {})

def user_logout(request):
    logout(request)
    return redirect('/')

@login_required 
def user_edit(request):
    return render(request, 'user_edit.html', {})

@login_required 
@csrf_exempt
@require_POST
def user_update(request):
    user_id = request.user.id

    if BudgetUser.objects.filter(user_id=user_id).count() != 0:
        user = BudgetUser.objects.get(user_id = user_id)
    else:
        user = BudgetUser()

    user.user_id = user_id
    user.first_name = request.POST['first_name']
    user.last_name = request.POST['last_name']
    user.program = request.POST['program']
    user.program_length = request.POST['program_length']
    user.current_year = request.POST['current_year']
    user.current_term = request.POST['current_term']
    user.coop = request.POST['coop']
    user.sequence = request.POST['sequence']

    user.save()

    return redirect('/')

@login_required
def user(request):
    user = BudgetUser.objects.get(user_id=request.user.id)
    data_set = BudgetPlanningData.objects.filter(user_id = request.user.id)

    parsed_data = parse_data_for_view(user, data_set)

    return render(request, 'user.html', {
        'user':user,
        'data':parsed_data,
    })

@login_required 
@csrf_exempt
@require_POST
def planning_update(request):
    data_id = request.POST['id']

    return HttpResponse(request.POST['value'])

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
def check_username(request):
    data = request.POST
    num_results = User.objects.filter(username = data['username']).count()
    if num_results != 0:
        return HttpResponseBadRequest("username duplicate")
    return HttpResponse("Okay")

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




