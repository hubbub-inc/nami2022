from datetime import datetime, timedelta, date
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.urls import reverse
import json
from django.utils.safestring import mark_safe
from django.core import serializers
import calendar
import datetime


import json
from .models import *
from .utils import Calendar
from programs.models import PROGRAM_CHOICES, Program
from django import forms
from django.forms import ModelChoiceField
from django.views.decorators.clickjacking import xframe_options_exempt


today = date.today()


class ProgramForm(forms.ModelForm):


    class Meta:
        model = Meeting
        fields = ('program',)

def cal_view(request):
    meetings = [i for i in Meeting.objects.all()]
    meetinglist = [{'title': i.program.name,  'instructions': i.program.instructions,  'time': i.start_time.strftime("%I:%M %p"), 'date': i.start_time.strftime("%Y-%m-%d"), 'color': i.get_color } for i in meetings]
    asJson = json.dumps(meetinglist)
    print(meetinglist)
    context = {}
    context['myevents'] = asJson
    template = "cal.html"
    return render(request, template, context)


class CalendarView(generic.ListView):
    model = Meeting
    template_name = 'calendar.html'

    context = {}
    template = "landing.html"

    def get_context_data(self, **kwargs):
        print('GETTING STANDARD')

        context = super().get_context_data(**kwargs)
        d = get_date(self.request.GET.get('month', None))
        cal = Calendar(d.year, d.month)
        html_cal = cal.formatmonth(withyear=True)
        context['calendar'] = mark_safe(html_cal)
        context['prev_month'] = prev_month(d)
        context['next_month'] = next_month(d)
        today = datetime.date.today()

        addweek = today + datetime.timedelta(days=20)
        upcoming = [i for i in Meeting.objects.filter(start_time__range=[today, "2023-12-01"])]



        meetinglist = [
            {'title': meeting.program.name, 'instructions': meeting.program.instructions, 'programid': meeting.program.pk, 'day': str(meeting.start_time.day),
             'month': meeting.start_time.strftime("%B"), 'time': meeting.start_time.strftime("%I:%M %p"), 'color': meeting.get_color} for meeting in upcoming]
        # meetinglist.reverse()
        context['upcoming'] = meetinglist
        jsonString = json.dumps(meetinglist)

        context['js_objects'] = jsonString
        choices = [i for i in Program.objects.all()]
        context['choices'] = choices
        print(choices)
        print('calendar view')

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






class filterEvents(generic.ListView):
    model = Meeting
    template_name = 'calendar.html'

    context = {}
    template = "landing.html"










    def get_context_data(self, **kwargs):
        print('GETTING FILTERED')
        try:
            print(self.kwargs['prg'])
        except:
            print("An exception occurred")

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
            {'title': meeting.program.name, 'instructions': meeting.program.instructions, 'programid': meeting.program.pk, 'day': str(meeting.start_time.day),
             'month': meeting.start_time.strftime("%B"), 'time': meeting.start_time.strftime("%I:%M %p"), 'color': meeting.get_color} for meeting in upcoming if meeting.program.pk==self.kwargs['prg']]
        # meetinglist.reverse()
        context['upcoming'] = meetinglist
        jsonString = json.dumps(meetinglist)

        context['js_objects'] = jsonString
        choices = [i for i in Program.objects.all()]
        context['choices'] = choices
        print(choices)

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