# Generated by Django 3.2.25 on 2024-06-10 18:33

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
            name='Search',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_emp', models.CharField(blank=True, max_length=200, null=True)),
                ('nome_colab', models.CharField(blank=True, max_length=500, null=True)),
                ('emails', models.CharField(blank=True, max_length=200, null=True)),
                ('passwd', models.CharField(blank=True, max_length=200, null=True)),
                ('domain', models.CharField(blank=True, max_length=200, null=True)),
                ('ipadd', models.CharField(blank=True, max_length=200, null=True)),
                ('urls', models.CharField(blank=True, max_length=200, null=True)),
                ('shodan_search', models.CharField(blank=True, max_length=200, null=True)),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email_leak', models.TextField(blank=True, max_length=200, null=True)),
                ('domain_leak', models.TextField(blank=True, max_length=200, null=True)),
                ('spf', models.TextField(blank=True, max_length=200, null=True)),
                ('emp', models.TextField(blank=True, max_length=200, null=True)),
                ('shodan', models.TextField(blank=True, max_length=200, null=True)),
                ('search', models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='osint.search')),
            ],
        ),
    ]