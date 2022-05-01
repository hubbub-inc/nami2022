from django.db import models
from people.models import Person

DEF = 'DEF'
CARE = 'Caring and Sharing Meetings'
COD = 'COD'
CMT = 'Committees'
FTH = 'FaithNet'
FTF = 'Family-to-Family'
FSP = 'Family Support Group'
FND = 'Fundraising'
FML = 'Family Meeting'
IOOV = 'In Our Own Voice'
P2P = 'Peer-to-Peer'
PSG = 'Peer Support Group'
PSG2 = 'Peer Support Group2'
WLK = 'WALK'
SPRT = 'Spirituality Group'
UNITES = 'UTS'
LGN = 'Legislative Night'
WFS = 'Whole Family Support'
PRT = 'Partner/Spouse Support'
SBL = 'Sibling Support'
TNS = 'Teen Support'
FSS = 'Families Surviving Suicide Loss'

PROGRAM_CHOICES = [
    (CARE, 'Caring and Sharing Meetings'),
    (CMT, 'Committees'),
    (FTH, 'FaithNet'),
    (FTF, 'Family-to-Family'),
    (FSP, 'Family Support Group'),
    (FND, 'Fundraising'),
    (FML, 'Family Meeting'),
    (IOOV, 'In our Own Voice'),
    (SPRT, 'Spirituality Group'),
    (P2P, 'Peer-to-Peer'),
    (PSG, 'Peer Support Group'),
    (PSG2, 'Peer Support Group2'),
    (WLK , 'WALK'),
    (LGN, 'Legislative Night'),
    (WFS, 'Whole Family Support'),
    (PRT, 'Partner/Spouse Support'),
    (SBL, 'Sibling Support'),
    (TNS, 'Teen Support'),
    (FSS, 'Families Surviving Suicide Loss'),
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
        if ((self.name) == PSG) or ((self.name) == WFS) or ((self.name) == SBL) or ((self.name) == SPRT) or ((self.name) == PRT) or ((self.name) == TNS) or ((self.name) == FSP):
            return True
        else:
            return False

    def __str__(self):
        return self.name
