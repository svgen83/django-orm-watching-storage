import datetime
from django.utils.timezone import localtime

def get_duration(visit):
    delta_time = localtime(visit.leaved_at) - localtime(visit.entered_at)
    return int(delta_time.total_seconds()/60)


def format_duration(duration):
    return f'В хранилище пробыл {duration} минут'