from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail

DEF = 'DEF'
CARE = 'Caring and Sharing Meetings'
COD = 'COD'
CMT = 'Committees'
FTH = 'FaithNet'
FTF = 'Family-to-Family'
FND = 'Fundraising'
FML = 'Family Meeting'
IOOV = 'In Our Own Voice'
P2P = 'Peer-to-Peer'
PSG = 'Peer Support Group'
PSG2 = 'Peer Support Group2'
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
    (FML, 'Family Meeting'),
    (IOOV, 'In our Own Voice'),
    (SPRT, 'Support Groups'),
    (P2P, 'Peer-to-Peer'),
    (PSG, 'Peer Support Group'),
    (PSG2, 'Peer Support Group2'),
    (WLK , 'WALK'),
    (LGN, 'Legislative Night'),
    (WFS, 'Whole Family Support'),

]


class Member(models.Model):
    program = models.CharField(
        max_length=100,
        choices=PROGRAM_CHOICES,
        default=DEF,
    )
    name = models.CharField(max_length=250)
    phone = models.CharField(max_length=10)
    email = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Person(models.Model):
    name = models.CharField(max_length=250)
    phone = models.CharField(max_length=10)
    email = models.TextField(blank=True)

    def __str__(self):
        return self.name


@receiver(post_save, sender=Member)
def send_mail_to_subs(sender, instance, created, **kwargs):

    if created:
        print("created")
        send_mail(
            subject='nami registration request',
            message=f'{instance.name} --- {instance.email} -- {instance.phone} -- {instance.program}',
            from_email='namiweb@yahoo.com',
            recipient_list=['matthew.carrella@gmail.com'],
            fail_silently=False,
        )