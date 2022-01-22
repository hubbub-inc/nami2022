from django.shortcuts import render
from .models import Program
from events.models import Meeting
from django.shortcuts import render
import datetime


def landing(request):
    context = {}
    template = "landing.html"

    context = {}

    today = datetime.datetime.today().date()

    addweek = today + datetime.timedelta(days=20)

    upcoming = [i for i in Meeting.objects.filter(start_time__range=(today, addweek))]

    meetinglist = [{'title': meeting.program.name, 'programid': meeting.program.pk, 'day': str(meeting.start_time.day),
                    'month': meeting.start_time.strftime("%B"), 'color': meeting.get_color} for meeting in upcoming]
    meetinglist.reverse()
    context['upcoming'] = meetinglist

    print('done')
    return render(request, template, context)


def classList(request):
    classes = [i for i in Program.objects.all()]
    classes = [i for i in classes if i.isSupportGroup() == False]
    title = "Classes"
    subtitle = "NAMI's education programs provide information and strategies for those suffering from mental illness and their families. Through a combination of presentations, discussions and interactive exercises, participants develop skills and habits that research has proven effective in maintaining good mental health and healthy relationships."
    context = {}
    context['programs'] = classes
    context['title'] = title
    context['subtitle'] = subtitle
    template = 'programList.html'
    return render(request, template, context)


def supportList(request):
    print('GETTING SUPPORT')
    groups = [i for i in Program.objects.all()]
    title = "Support Groups"
    subtitle = "Whether you've been affected directly or indirectly by mental illness,  your healing begins when you are able to acknowledge and  to share what you've been through. Support groups offer an opportunity to tell your story, learn from others, and give and receive loving encouragement from others at different stages in the recovery process."

    groups = [i for i in groups if i.isSupportGroup() == True]
    print(len(groups))
    context = {}
    context['programs'] = groups
    context['title'] = title
    context['subtitle'] = subtitle
    template = 'programList.html'
    return render(request, template, context)


def programDetail(request, pk=None):
    program = Program.objects.get(pk=pk)
    context = {}
    context['program'] = program

    return render(request, 'programDetail.html', context)