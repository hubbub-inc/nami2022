from django.shortcuts import render
from .models import Program
from events.models import Meeting
from django.shortcuts import render
import datetime
from django.views.decorators.clickjacking import xframe_options_exempt
import io
import mammoth
import os

THIS_DIR = os.path.dirname(__file__)
filedir = THIS_DIR + '/specialevent.docx'



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
    subtitle = "By sharing your experiences in a safe and confidential setting, you can gain hope and feel a sense of connection. Support groups encourage empathy, productive discussion and a sense of community. You'll benefit from other's experiences, discover your inner strength and empower yourself by sharing your own experiences in a non-judgmental space."


    groups = [i for i in groups if i.isSupportGroup() == True]
    print(len(groups))
    context = {}
    context['programs'] = groups
    context['title'] = title
    context['subtitle'] = subtitle
    template = 'programList.html'
    return render(request, template, context)


def specialEvents(request):
    custom_css = """
           <style>
           .sectionHeading {

               font-size: 40px;
           }

           .sectionContent {
                   font-size: 30px;
                   }
            .subInfo {
                font-size: 15px;
                }
     

           </style>
           """

    custom_styles = """ b => h3.sectionHeading
                           i => p.sectionContent
                           u => p.subInfo

                           p[style-name='Heading 1'] => h1.red.underline"""
    with open(filedir, "rb") as docx_file:
        result = mammoth.convert_to_html(docx_file, style_map=custom_styles)
        text = custom_css + result.value


    title = "Special Events"
    subtitle = "Each month NAMI sponsors special presentations providing in-depth discussions on specific topics in mental health. NAMI also holds monthly business meetings where members come together for support and to organize activities."


    template = 'specialEvents.html'
    context = {}
    context['title'] = title
    context['subtitle'] = subtitle
    context['docx'] = f"{text}"
    return render(request, template, context)


def programDetail(request, pk=None):
    program = Program.objects.get(pk=pk)
    context = {}
    context['program'] = program

    return render(request, 'programDetail.html', context)