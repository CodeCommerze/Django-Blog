# Generated by Django 4.1.4 on 2023-01-15 17:46

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0004_blog_view'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='view',
            field=models.ManyToManyField(blank=True, related_name='user_view', to=settings.AUTH_USER_MODEL),
        ),
    ]