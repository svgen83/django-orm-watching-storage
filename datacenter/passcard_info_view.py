from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from time_tools import get_duration, format_duration


def if_visit_long(duration):
  if duration > 60:
    return 'Подозрителен'
  else:
    return 'Без подозрений'

      
def passcard_info_view(request, passcode):
    this_passcard_visits = []
    passcard = get_object_or_404(Passcard, passcode=passcode)
    visits = Visit.objects.filter(passcard=passcard)
    for visit in visits:
        duration = get_duration(visit)
        this_passcard_visit = {
          'entered_at': visit.entered_at,
          'duration': format_duration(duration),
          'is_strange': if_visit_long(duration)}
        this_passcard_visits.append(this_passcard_visit)
    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)
