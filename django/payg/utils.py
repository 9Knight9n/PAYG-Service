from datetime import datetime
from authentication.models import User
from payg.config import API_COST
from payg.models import Record


def calculate_user_cost_per_month(user: User, year: int, month: int):
    return sum([
        API_COST[item['api']] * item['count'] for item in
        list(Record.objects.filter(user=user, year=year, month=month).values('api', 'count'))
    ])


def calculate_user_cost_current_month(user: User):
    date = datetime.now()
    return calculate_user_cost_per_month(user, date.year, date.month)
