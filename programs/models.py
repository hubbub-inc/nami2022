from django.db import models
from people.models import Person

DEF = 'DEF'
CARE = 'Caring and Sharing Meetings'
COD = 'COD'
CMT = 'Committees'
FTH = 'FaithNet'
FTF = 'Family-to-Family'
FND = 'Fundraising'
IOOV = 'In Our Own Voice'
P2P = 'Peer-to-Peer'
PSG = 'Peer Support Group'
WLK = 'WALK'
SPRT = 'Spirituality'
UNITES = 'UTS'
LGN = 'Legislative Night'
WFS = 'Whole Family Support'

PROGRAM_CHOICES = [
    (CARE, 'Caring and Sharing Meetings'),
    (CMT, 'Committees'),
    (FTH, 'FaithNet'),
    (FTF, 'Family-to-Family'),
    (FND, 'Fundraising'),
    (IOOV, 'In our Own Voice'),
    (SPRT, 'Support Groups'),
    (P2P, 'Peer-to-Peer'),
    (PSG, 'Peer Support Group'),
    (WLK , 'WALK'),
    (LGN, 'Legislative Night'),
    (WFS, 'Whole Family Support'),

]


class Program(models.Model):

    name = models.CharField(
        max_length=100,
        choices=PROGRAM_CHOICES,
        default=DEF,
    )

    description = models.TextField(blank=True)
    instructions = models.TextField(blank=True)
    members = models.ForeignKey(Person, blank=True,  null=True, on_delete=models.CASCADE, related_name="members")

    def isClass(self):
        if ((self.name) == P2P) or ((self.name) == FTF):
            return True
        else:
            return False

    def isSupportGroup(self):
        if ((self.name) == PSG) or ((self.name) == WFS):
            return True
        else:
            return False

    def __str__(self):
        return self.name