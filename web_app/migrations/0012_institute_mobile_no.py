# Generated by Django 3.2 on 2021-05-22 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_app', '0011_institute'),
    ]

    operations = [
        migrations.AddField(
            model_name='institute',
            name='mobile_no',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
