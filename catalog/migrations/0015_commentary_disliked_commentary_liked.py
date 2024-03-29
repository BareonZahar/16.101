# Generated by Django 4.2.6 on 2024-03-05 17:14

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('catalog', '0014_commentary_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='commentary',
            name='disliked',
            field=models.ManyToManyField(related_name='disliked_commentaries', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='commentary',
            name='liked',
            field=models.ManyToManyField(related_name='liked_commentaries', to=settings.AUTH_USER_MODEL),
        ),
    ]
