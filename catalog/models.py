
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Genre(models.Model):
    name = models.CharField(max_length=20, verbose_name='Жанр')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'


class Director(models.Model):
    fname = models.CharField(max_length=20, verbose_name='Имя')
    lname = models.CharField(max_length=20, verbose_name='Фамилия')
    image = models.CharField(max_length=100, blank=True, null=True, verbose_name='Картинка')

    def __str__(self):
        return f'{self.lname},{self.fname}'

    def get_absolute_url(self):
        return reverse('intdir', kwargs={'id': self.id})

    class Meta:
        verbose_name = 'Режиссер'
        verbose_name_plural = 'Режиссеров'


class Actor(models.Model):
    fname = models.CharField(max_length=20, verbose_name='Имя')
    lname = models.CharField(max_length=20, verbose_name='Фамилия')
    born = models.DateField(blank=True, null=True, verbose_name='Дата рождения')
    country = models.CharField(max_length=20, blank=True, null=True, verbose_name='Страна')
    image = models.CharField(max_length=100, blank=True, null=True, verbose_name='Картинка')

    def __str__(self):
        return self.lname

    def get_absolute_url(self):
        return reverse('infor', kwargs={'id': self.id})

    class Meta:
        verbose_name = 'Актер'
        verbose_name_plural = 'Актеров'


class Status(models.Model):
    VIBOR = (('бесплатно', 'бесплатно'), ('базовая', 'базовая'), ('супер', 'супер'))
    name = models.CharField(max_length=60, choices=VIBOR, verbose_name='Подписка')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы'


class Country(models.Model):
    name = models.CharField(max_length=20, verbose_name='Страна')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Страна'
        verbose_name_plural = 'Страны'


class AgeRate(models.Model):
    choise = (('G', 'G'), ('PG', 'PG'), ('PG-13', 'PG-13'), ('R', 'R'), ('NC-17', 'NC-17'))
    rate = models.CharField(max_length=20, choices=choise, verbose_name='Рейтинг')

    def __str__(self):
        return self.rate

    class Meta:
        verbose_name = 'Рейтинг'
        verbose_name_plural = 'Рейтингов'


class Kino(models.Model):
    title = models.CharField(max_length=30, verbose_name='Название')
    genre = models.ForeignKey(Genre, on_delete=models.SET_DEFAULT, default=1, verbose_name='Жанр')
    rating = models.FloatField(verbose_name='Оценка')
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True)
    director = models.ForeignKey(Director, on_delete=models.SET_NULL, null=True)
    summary = models.TextField(max_length=500, verbose_name='Описание')
    year = models.IntegerField(verbose_name='Год')
    ager = models.ForeignKey(AgeRate, on_delete=models.SET_NULL, null=True)
    actor = models.ManyToManyField(Actor, verbose_name='Актер')
    status = models.ForeignKey(Status, on_delete=models.SET_DEFAULT, default=1)
    image = models.CharField(max_length=100, blank=True, null=True, verbose_name='Картинка')

    def __str__(self):
        return self.title

    def display_actors(self):
        res = ''
        for a in self.actor.all():
            res += a.lname + ' ' + a.fname
        return res
    display_actors.short_description = 'Актеры'

    def get_absolute_url(self):
        return reverse('info', kwargs={'id': self.id})

    class Meta:
        verbose_name = 'Фильм'
        verbose_name_plural = 'Фильмы'
        ordering = ['-year']


class Commentary(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    post = models.ForeignKey(Kino, on_delete=models.CASCADE, related_name='comments', verbose_name='Комментарий')
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Пользователь')
    like = models.IntegerField(null=True, blank=True, verbose_name='Количество лайков')
    body = models.TextField(max_length=1000, null=True, blank=True, verbose_name='Текст')
    time_created = models.DateTimeField(auto_now_add=True, null=True, blank=True, verbose_name='Время создания')
    publish = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft', verbose_name='Видимость поста')

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментариев'
        ordering = ['-time_created']

    def get_absolute_url(self):
        return reverse('post', kwargs={'id': self.post.id})

    def __str__(self):
        return self.body
