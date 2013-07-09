# Create your views here.
from django.http import HttpResponse, Http404, HttpResponseBadRequest
from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from budget.models import BudgetUser, BudgetPlanningData, BudgetTrackingData
from budget.aux import format_data_for_view, initiate_user_preset_data, get_limits, sanitize_decimal
from decimal import *
from datetime import datetime
import re

DATA_ID_RE = '(?P<category>[\/a-zA-Z_ ]*)_(?P<year>\d)(?P<term>.)'

@login_required 
def index(request):
    try:
        budget_user = BudgetUser.objects.get(user_id = request.user.id)
        return redirect('/planning/')
    except:
        return redirect('/intro/')

def user_login(request):
    return render(request, 'login.html', {})

def user_logout(request):
    logout(request)
    return redirect('/')

def intro(request):
    try:
        budget_user = BudgetUser.objects.get(user_id = request.user.id)
        return render(request, 'intro.html', {})
    except:
        return render(request, 'intro.html', {'new_user': True})

@login_required 
def user_edit(request):
    budget_user = {}
    try:
        budget_user = BudgetUser.objects.get(user_id=request.user.id)
    except:
        pass
    return render(request, 'user_edit.html', {
        'budget_user': budget_user,
    })

@login_required 
@csrf_exempt
@require_POST
def user_update(request):
    user_id = request.user.id

    print request.POST

    if BudgetUser.objects.filter(user_id=user_id).count() != 0:
        user = BudgetUser.objects.get(user_id = user_id)
    else:
        user = BudgetUser()

    user.user_id = user_id
    if datetime.now().month >= 9:
        user.current_term = 1
    elif datetime.now().month >=5 :
        user.current_term = 3
    else:
        user.current_term = 2
    user.start_year = int(request.POST['start_year'])
    user.end_year = int(request.POST['end_year'])
    user.tuition = Decimal(sanitize_decimal(request.POST['tuition']))
    user.saved = Decimal(sanitize_decimal(request.POST['saved']))
    user.part_time = 0
    user.program_length = user.end_year - user.start_year
    user.current_year = datetime.now().year - user.start_year + 1
    if user.current_term == 1: #in case that the current term is the fall term
        user.current_year += 1
    if user.current_year > user.program_length: #handle the case where the student is in their last two semesters
        user.current_year = user.program_length

    user.coop = request.POST['coop']
    user.sequence = request.POST['sequence']

    user.save()

    for item in BudgetPlanningData.objects.filter(user_id=user_id):
        item.delete()

    initiate_user_preset_data('default', user)

    return redirect('/planning/')

@login_required
def planning(request):
    #try:
    budget_user = BudgetUser.objects.get(user_id=request.user.id)
    data_set = BudgetPlanningData.objects.filter(user_id = request.user.id)

    data = format_data_for_view(budget_user, data_set)
    budget_user.remaining_years = range(budget_user.current_year, budget_user.program_length + 1)
    budget_user.remaining_terms = []
    for i in range(budget_user.current_year-1, budget_user.program_length):
        budget_user.remaining_terms.append("Fall(" + budget_user.sequence[(i*3)+0] +")")
        budget_user.remaining_terms.append("Winter(" + budget_user.sequence[(i*3)+1] +")")
        budget_user.remaining_terms.append("Spring(" + budget_user.sequence[(i*3)+2] +")")
    return render(request, 'planning.html', {
        'budget_user':budget_user,
        'data':data,
    })
    #except:
    #   return render(request, 'intro.html', {'new_user': True, 'error': True})

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
    data.amount = Decimal(sanitize_decimal(request.POST['value']))
    data.save()
    return HttpResponse('%.2f' % data.amount)

@login_required 
def tracking(request):
    try:
        data = BudgetTrackingData.objects.filter(user_id=request.user.id).order_by('-created')

        limits = get_limits(request.user.id)    

        return render(request, 'tracking.html', {
            'data': data,
            'limits': limits,
        })
    except:
        return render(request, 'intro.html', {'new_user': True, 'error': True})

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
    data.amount= Decimal(sanitize_decimal(request.POST['amount']))
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
        return render(request, 'login.html', {
            'error': 'The username or password you entered was incorrect.',
        })
    else:
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




