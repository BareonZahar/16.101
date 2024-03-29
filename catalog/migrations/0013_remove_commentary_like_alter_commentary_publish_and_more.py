# Generated by Django 4.2.6 on 2024-03-03 10:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('catalog', '0012_alter_actor_options_alter_agerate_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='commentary',
            name='like',
        ),
        migrations.AlterField(
            model_name='commentary',
            name='publish',
            field=models.BooleanField(default=True, verbose_name='Видимость поста'),
        ),
        migrations.CreateModel(
            name='Likes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('like_comment', models.BooleanField(verbose_name='Оценка товара')),
                ('comit', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='catalog.kino', verbose_name='Комментарий фильма')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Лайк',
                'verbose_name_plural': 'Лайки',
            },
        ),
    ]
