# Generated by Django 3.2 on 2021-05-14 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_app', '0002_student_institute_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='expert',
            name='institute_name',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]