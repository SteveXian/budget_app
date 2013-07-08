from budget.models import SPRING, FALL, WINTER
from budget.models import BudgetUser, BudgetPlanningData, BudgetPresetData, BudgetTrackingData
from datetime import timedelta, datetime
from django.utils import timezone

EXAMPLE = [
    { 'income': True, 'program': 'default', 'label': 'Salary', 'year': 1, 'coop': False, 'amount': 0},
    { 'income': True, 'program': 'default', 'label': 'Salary', 'year': 1, 'coop': True, 'amount': 12000},
    { 'income': True, 'program': 'default', 'label': 'Salary', 'year': 2, 'coop': False, 'amount': 0},
    { 'income': True, 'program': 'default', 'label': 'Salary', 'year': 2, 'coop': True, 'amount': 13000},
    { 'income': True, 'program': 'default', 'label': 'Salary', 'year': 3, 'coop': False, 'amount': 0},
    { 'income': True, 'program': 'default', 'label': 'Salary', 'year': 3, 'coop': True, 'amount': 14000},
    { 'income': True, 'program': 'default', 'label': 'Salary', 'year': 4, 'coop': False, 'amount': 0},
    { 'income': True, 'program': 'default', 'label': 'Salary', 'year': 4, 'coop': True, 'amount': 15000},
    { 'income': True, 'program': 'default', 'label': 'Salary', 'year': 5, 'coop': False, 'amount': 0},
    { 'income': True, 'program': 'default', 'label': 'Salary', 'year': 5, 'coop': True, 'amount': 16000},
]

def sanitize_decimal(amount):
    for char in ['$', ',', ' ']:
        amount = amount.replace(char, "")
    return amount


# []
#
def parse_preset_data(data_set):
    inserts = []
    for data in data_set:
        inserts.append(BudgetPresetData(
            program=data['program'],
            label=data['label'],
            year=data['year'],
            coop=data['coop'],
            income=data['income'],
            amount=data['amount'],
        ))
    BudgetPresetData.objects.bulk_create(inserts)

def initiate_user_preset_data(program, user):
    inserts = []
    data_set = BudgetPresetData.objects.filter(program=program)
    cnt = 0
    for year in range(user.current_year, user.program_length+1):
        for term in [FALL, WINTER, SPRING]:
            coop = True if user.sequence[cnt] == 'W' else False
            program_data  = data_set.filter(year=year, coop=coop)
            if user.sequence[cnt] == 'O':
                for data in program_data:
                    inserts.append(BudgetPlanningData(
                        user_id = user.user_id,
                        label = data.label,
                        year = year,
                        term = term,
                        income = data.income,
                        amount = 0,
                        created = datetime.today(),
                        modified = datetime.today(),
                    ))
            else:
                for data in program_data:
                    inserts.append(BudgetPlanningData(
                        user_id = user.user_id,
                        label = data.label,
                        year = year,
                        term = term,
                        income = data.income,
                        amount = data.amount,
                        created = datetime.today(),
                        modified = datetime.today(),
                    ))
            cnt += 1
    BudgetPlanningData.objects.bulk_create(inserts)

def format_data_for_view(user, data_set):
    res = {}
    for income in [True, False]:
        set_income = data_set.filter(income=income)
        dict_income = []
        categories = set()
        for item in set_income:
            categories.add(item.label)
        for label in categories:
            set_label = set_income.filter(label=label)
            label_item = {}
            label_item['label'] = label
            label_item['data'] = []
            for year in range(user.current_year, user.program_length+1):
                set_year = set_label.filter(year=year)
                for term in [FALL, WINTER, SPRING]:
                    data = set_year.get(term=term)
                    formatted = {}
                    formatted['class'] = str(year)+term
                    formatted['id'] = label + '_' + str(year)+term
                    formatted['amount'] = data.amount
                    label_item['data'].append(formatted)
            dict_income.append(label_item)
        if income:
            res['income'] = dict_income
        else:
            res['expense'] = dict_income
    return res

TERM = {}
TERM[1]='F'
TERM[2]='W'
TERM[3]='S'

def get_limits(user_id):
    user = BudgetUser.objects.get(user_id=user_id)
    labels = BudgetPlanningData.objects.filter(income=False).values('label').distinct()
    plan_data = BudgetPlanningData.objects.filter(user_id=user_id, year=user.current_year, term=TERM[user.current_term])
    current_data = BudgetTrackingData.objects.filter(user_id=user_id, year=user.current_year, term=user.current_term)
    
    limits = {}
    for term in ['weekly', 'monthly', 'term']:
        limits[term] = []
        for label in labels:
            plan = plan_data.get(label=label['label']).amount
            label_data = {}
            label_data['current'] = 0
            label_data['label'] = label['label']
            if term == 'weekly':
                label_data['limit'] = (((plan/4)/30)*7)
                monday_of_this_week = timezone.now().date() - timedelta(days=(timezone.now().date().isocalendar()[2] - 1))
                for item in current_data.filter(created__gte=monday_of_this_week, label=label['label']):
                    label_data['current'] += item.amount

            elif term == "monthly":
                label_data['limit'] = (plan/4)
                last_month = timezone.now().date() - timedelta(days=30)
                for item in current_data.filter(created__gte=last_month, label=label['label']):
                    label_data['current'] += item.amount

            elif term == 'term':
                label_data['limit'] = plan
                for item in current_data.filter(label=label['label']):
                    label_data['current'] += item.amount

            if label_data['current'] > label_data['limit']:
                label_data['over'] = True
            else:
                label_data['over'] = False

            label_data['limit'] = '%.2f' % label_data['limit']
            limits[term].append(label_data)

    print limits
    return limits
