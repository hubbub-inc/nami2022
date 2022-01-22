from datetime import datetime, timedelta, date
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.urls import reverse
from django.utils.safestring import mark_safe
import calendar
import datetime

from .models import *
from .utils import Calendar




class CalendarView(generic.ListView):
    model = Meeting
    template_name = 'calendar.html'

    context = {}
    template = "landing.html"






    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        d = get_date(self.request.GET.get('month', None))
        cal = Calendar(d.year, d.month)
        html_cal = cal.formatmonth(withyear=True)
        context['calendar'] = mark_safe(html_cal)
        context['prev_month'] = prev_month(d)
        context['next_month'] = next_month(d)
        today = datetime.date.today()

        addweek = today + datetime.timedelta(days=20)

        upcoming = [i for i in Meeting.objects.all()]

        meetinglist = [
            {'title': meeting.program.name, 'programid': meeting.program.pk, 'day': str(meeting.start_time.day),
             'month': meeting.start_time.strftime("%B"), 'color': meeting.get_color} for meeting in upcoming]
        meetinglist.reverse()
        context['upcoming'] = meetinglist
        return context

def get_date(req_month):
    if req_month:
        year, month = (int(x) for x in req_month.split('-'))
        return date(year, month, day=1)
    return datetime.date.today()

def prev_month(d):
    first = d.replace(day=1)
    prev_month = first - timedelta(days=1)
    month = 'month=' + str(prev_month.year) + '-' + str(prev_month.month)
    return month

def next_month(d):
    days_in_month = calendar.monthrange(d.year, d.month)[1]
    last = d.replace(day=days_in_month)
    next_month = last + timedelta(days=1)
    month = 'month=' + str(next_month.year) + '-' + str(next_month.month)
    return month

def event(request, event_id=None):
    instance = Meeting()
    if event_id:
        instance = get_object_or_404(Meeting, pk=event_id)