# Generated by Django 3.2.8 on 2022-04-01 15:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Containers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_name', models.CharField(default=None, max_length=200, null=True)),
                ('container_name', models.CharField(default=None, max_length=200, null=True)),
                ('container_port', models.CharField(default=None, max_length=200, null=True)),
                ('container_vnc_user', models.CharField(default=None, max_length=200, null=True)),
                ('container_vnc_password', models.CharField(default=None, max_length=200, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('container_user', models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='container_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Instances',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('instance_name', models.CharField(default=None, max_length=200, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('container', models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='container', to='main.containers')),
            ],
        ),
    ]
