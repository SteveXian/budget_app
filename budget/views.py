# Create your views here.
from django.http import HttpResponse, Http404, HttpResponseBadRequest
from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from budget.models import BudgetUser, BudgetPlanningData, BudgetTrackingData
from budget.aux import format_data_for_view, initiate_user_preset_data, get_limits
from decimal import *
import re

DATA_ID_RE = '(?P<category>[\/a-zA-Z_]*)_(?P<year>\d)(?P<term>.)'

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
    user.first_name = str(request.POST['first_name'])
    user.last_name = str(request.POST['last_name'])
    user.program = str(request.POST['program'])
    user.program_length = int(request.POST['program_length'])
    user.current_year = int(request.POST['current_year'])
    user.current_term = int(request.POST['current_term'])
    user.coop = request.POST['coop']
    user.sequence = str(request.POST['sequence'])

    user.save()

    for item in BudgetPlanningData.objects.filter(user_id=user_id):
        item.delete()

    initiate_user_preset_data('default', user)

    return redirect('/')

@login_required
def user(request):
    budget_user = BudgetUser.objects.get(user_id=request.user.id)
    data_set = BudgetPlanningData.objects.filter(user_id = request.user.id)

    data = format_data_for_view(budget_user, data_set)
    budget_user.remaining_years = range(budget_user.current_year, budget_user.program_length + 1)
    budget_user.remaining_terms = (budget_user.program_length - budget_user.current_year + 1) * 3
    return render(request, 'user.html', {
        'budget_user':budget_user,
        'data':data,
    })

@login_required 
@csrf_exempt
@require_POST
def planning_update(request):
    data_id = request.POST['id']
    result = re.match(DATA_ID_RE, data_id)
    data = BudgetPlanningData.objects.get(  user_id = request.user.id, 
                                            label = result.group('category'),
                                            year = result.group('year'),
                                            term = result.group('term'))
    data.amount = Decimal(request.POST['value'])
    data.save()
    return HttpResponse('%.2f' % data.amount)

@login_required 
def tracking(request):
    data = BudgetTrackingData.objects.filter(user_id=request.user.id).order_by('-created')

    limits = get_limits(request.user.id)    

    return render(request, 'tracking.html', {
        'data': data,
        'limits': limits,
    })

@login_required 
@csrf_exempt
@require_POST
def tracking_add(request):
    budget_user = BudgetUser.objects.get(user_id=request.user.id)

    data = BudgetTrackingData()
    data.user_id = request.user.id
    data.label = str(request.POST['category'])
    data.description = str(request.POST['description'])
    data.year = int(budget_user.current_year)
    data.term = int(budget_user.current_term)
    data.amount= Decimal(request.POST['amount'])
    data.save()
    return redirect('/tracking/')

@login_required 
def tracking_delete(request, id):
    BudgetTrackingData.objects.get(id=id).delete()
    return redirect('/tracking/')

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




