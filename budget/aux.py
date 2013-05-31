from budget.models import SPRING, FALL, WINTER
from budget.models import BudgetUser, BudgetPlanningData, BudgetPresetData
from datetime import datetime
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
            amount=data['amount'],
        ))
    BudgetPresetData.objects.bulk_create(inserts)

def initiate_user_preset_data(program, user):
    inserts = []
    data_set = BudgetPresetData.objects.filter(program=program)
    cnt = ((user.current_year - 1) * 3)
    for year in range(user.current_year, user.program_length+1):
        for term in [FALL, WINTER, SPRING]:
            coop = True if user.sequence[cnt] == 'W' else False
            program_data  = data_set.filter(year=year, coop=coop)
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