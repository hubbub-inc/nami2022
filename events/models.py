

from django.db import models
from django.urls import reverse
from programs.models import Program

class Meeting(models.Model):
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    program = models.ForeignKey(Program, default=1, on_delete=models.CASCADE)

    class Meta:
        ordering = ('start_time',)



    @property
    def get_color(self):
        name = self.program.name
        if (name=="Peer-to-Peer") or (name=="Peer Support Group"):
            return "blue"
        if (name=="Family-to-Family") or (name=="Whole Family Support") or (name=="Sibling Support") or (name=="Partner/Spouse Support"):
            return "green"
        if (name=="FaithNet") or (name=="Spirituality"):
            return "purple"
        else:
            return "red"

    @property
    def get_html_url(self):
        switcher = {0: "pink", 1: "red", 2: "yellow"}
        color = switcher.get(self.program.pk, "orange")
        url = reverse('programs:program', args=(self.program.pk,))

        return f'<a  style="color:black;text-align:center;font-size:20px;" href="{url}"> <div style="background-color:{color};height:60px;">{self.program.name}</div> </a>'

    def __str__(self):
        time = self.start_time.strftime("%m/%d/%Y")
        name = self.program.name
        entry = name + " " + time
        return entry

