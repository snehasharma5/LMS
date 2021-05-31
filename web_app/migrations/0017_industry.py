# Generated by Django 3.2 on 2021-05-28 14:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web_app', '0016_alter_coursemodel_enrolled_students'),
    ]

    operations = [
        migrations.CreateModel(
            name='Industry',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='web_app.registermodel')),
                ('icon', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('address', models.TextField(blank=True, null=True)),
                ('contact_no', models.IntegerField(blank=True, null=True)),
                ('mobile_no', models.IntegerField(blank=True, null=True)),
                ('website_url', models.CharField(blank=True, max_length=255, null=True)),
                ('linkedIn_url', models.CharField(blank=True, max_length=255, null=True)),
                ('facebook_url', models.CharField(blank=True, max_length=255, null=True)),
                ('industry_type', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
    ]
