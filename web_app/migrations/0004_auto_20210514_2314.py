# Generated by Django 3.2 on 2021-05-14 17:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web_app', '0003_expert_institute_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='registermodel',
            name='is_expert',
        ),
        migrations.RemoveField(
            model_name='registermodel',
            name='is_industry',
        ),
        migrations.RemoveField(
            model_name='registermodel',
            name='is_institute',
        ),
        migrations.RemoveField(
            model_name='registermodel',
            name='is_student',
        ),
        migrations.DeleteModel(
            name='Expert',
        ),
    ]
