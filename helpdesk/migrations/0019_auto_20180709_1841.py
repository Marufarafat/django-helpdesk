# Generated by Django 2.0.6 on 2018-07-09 18:41

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
