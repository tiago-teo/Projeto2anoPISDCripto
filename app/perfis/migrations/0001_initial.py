# Generated by Django 3.2.25 on 2024-06-10 18:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import perfis.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Perfil',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(default='', max_length=100)),
                ('foto', models.ImageField(blank=True, null=True, upload_to=perfis.models.upload_place_pics)),
                ('intelx_api', models.CharField(default='', max_length=5000)),
                ('hunter_api', models.CharField(default='', max_length=5000)),
                ('shodan_api', models.CharField(default='', max_length=5000)),
                ('user', models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
