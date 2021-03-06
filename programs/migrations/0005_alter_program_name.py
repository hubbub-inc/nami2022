# Generated by Django 4.0.1 on 2022-05-01 23:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('programs', '0004_alter_program_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='program',
            name='name',
            field=models.CharField(choices=[('Caring and Sharing Meetings', 'Caring and Sharing Meetings'), ('Committees', 'Committees'), ('FaithNet', 'FaithNet'), ('Family-to-Family', 'Family-to-Family'), ('Family Support Group', 'Family Support Group'), ('Fundraising', 'Fundraising'), ('Family Meeting', 'Family Meeting'), ('In Our Own Voice', 'In our Own Voice'), ('Spirituality Group', 'Spirituality Group'), ('Peer-to-Peer', 'Peer-to-Peer'), ('Peer Support Group', 'Peer Support Group'), ('Peer Support Group2', 'Peer Support Group2'), ('WALK', 'WALK'), ('Legislative Night', 'Legislative Night'), ('Whole Family Support', 'Whole Family Support'), ('Partner/Spouse Support', 'Partner/Spouse Support'), ('Sibling Support', 'Sibling Support'), ('Teen Support', 'Teen Support'), ('Families Surviving Suicide Loss', 'Families Surviving Suicide Loss')], default='DEF', max_length=100),
        ),
    ]
