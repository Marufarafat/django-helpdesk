# Generated by Django 2.0.7 on 2018-07-17 15:22

from django.db import migrations, models
import ico_portal.utils.datetime


class Migration(migrations.Migration):

    dependencies = [
        ('helpdesk', '0018_ticket_reporter'),
    ]

    operations = [
        migrations.AlterField(
            model_name='followup',
            name='date',
            field=models.DateTimeField(default=ico_portal.utils.datetime.datetime.utcnow, verbose_name='Date'),
        ),
    ]
