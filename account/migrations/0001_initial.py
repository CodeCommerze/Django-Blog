# Generated by Django 4.1.4 on 2023-01-13 15:22

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
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='user/profile', verbose_name='Profile Picture')),
                ('first_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='First Name')),
                ('last_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Last Name')),
                ('phone_number', models.CharField(blank=True, max_length=255, null=True, verbose_name='Phone Number')),
                ('verify_token', models.CharField(blank=True, max_length=255, null=True, verbose_name=' Id Verify Token')),
                ('reset_token', models.CharField(blank=True, max_length=255, null=True, verbose_name='Password Reset Token')),
                ('is_active', models.BooleanField(default=False, verbose_name='Id Activated')),
                ('joined', models.DateTimeField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='profile_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
