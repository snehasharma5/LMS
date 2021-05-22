# Generated by Django 3.2 on 2021-05-15 07:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web_app', '0007_alter_student_qualification'),
    ]

    operations = [
        migrations.CreateModel(
            name='Expert',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='web_app.registermodel')),
                ('profile_pic', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('resume', models.FileField(blank=True, null=True, upload_to='resume/')),
                ('expertise_area', models.CharField(blank=True, max_length=255, null=True)),
                ('qualification', models.CharField(blank=True, max_length=255, null=True)),
                ('institute_name', models.CharField(blank=True, max_length=1000, null=True)),
                ('linkedIn_url', models.CharField(blank=True, max_length=255, null=True)),
                ('address', models.TextField(blank=True, null=True)),
                ('mobile', models.CharField(blank=True, max_length=10, null=True)),
            ],
        ),
    ]
