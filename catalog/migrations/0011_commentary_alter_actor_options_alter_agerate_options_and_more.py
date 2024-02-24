# Generated by Django 4.2.6 on 2024-02-24 21:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('catalog', '0010_director_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Commentary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('like', models.IntegerField(blank=True, null=True, verbose_name='Количество лайков')),
                ('body', models.TextField(blank=True, max_length=1000, null=True, verbose_name='Текст')),
                ('time_created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Время создания')),
                ('publish', models.CharField(choices=[('draft', 'Draft'), ('published', 'Published')], default='draft', max_length=10, verbose_name='Видимость поста')),
            ],
            options={
                'verbose_name': 'Комментарий',
                'verbose_name_plural': 'Комментариев',
                'ordering': ['-time_created'],
            },
        ),
        migrations.AlterModelOptions(
            name='actor',
            options={'verbose_name': 'Актер', 'verbose_name_plural': 'Актеров'},
        ),
        migrations.AlterModelOptions(
            name='agerate',
            options={'verbose_name': 'Рейтинг', 'verbose_name_plural': 'Рейтингов'},
        ),
        migrations.AlterModelOptions(
            name='country',
            options={'verbose_name': 'Страна', 'verbose_name_plural': 'Страны'},
        ),
        migrations.AlterModelOptions(
            name='director',
            options={'verbose_name': 'Режиссер', 'verbose_name_plural': 'Режиссеров'},
        ),
        migrations.AlterModelOptions(
            name='genre',
            options={'verbose_name': 'Жанр', 'verbose_name_plural': 'Жанры'},
        ),
        migrations.AlterModelOptions(
            name='kino',
            options={'ordering': ['-year'], 'verbose_name': 'Фильм', 'verbose_name_plural': 'Фильмы'},
        ),
        migrations.AlterModelOptions(
            name='status',
            options={'verbose_name': 'Статус', 'verbose_name_plural': 'Статусы'},
        ),
        migrations.AddField(
            model_name='actor',
            name='image',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Картинка'),
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
        migrations.AddField(
            model_name='commentary',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='catalog.kino', verbose_name='Комментарий'),
        ),
        migrations.AddField(
            model_name='commentary',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
    ]
