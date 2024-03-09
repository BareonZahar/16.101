
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Genre(models.Model):
    name = models.CharField(max_length=20, verbose_name='Жанр')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('pro_ganry', args=[str(self.id)])

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
        return reverse('intdir', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = 'Режиссеров'
        verbose_name_plural = 'Режиссеры'


class Actor(models.Model):
    fname = models.CharField(max_length=20, verbose_name='Имя')
    lname = models.CharField(max_length=20, verbose_name='Фамилия')
    born = models.DateField(blank=True, null=True, verbose_name='Дата рождения')
    country = models.CharField(max_length=20, blank=True, null=True, verbose_name='Страна')
    image = models.CharField(max_length=100, blank=True, null=True, verbose_name='Картинка')

    def __str__(self):
        return self.lname

    # def get_absolute_url(self):
    #     return reverse('infor', kwargs={'pk': self.pk})

    def get_absolute_url(self):
        return reverse('infor', kwargs={'pk': self.pk, 'lname': self.lname})

    class Meta:
        verbose_name = 'Актеров'
        verbose_name_plural = 'Актеры'


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
        verbose_name = 'Страну'
        verbose_name_plural = 'Страны'


class AgeRate(models.Model):
    choise = (('G', 'G'), ('PG', 'PG'), ('PG-13', 'PG-13'), ('R', 'R'), ('NC-17', 'NC-17'))
    rate = models.CharField(max_length=20, choices=choise, verbose_name='Рейтинг')

    def __str__(self):
        return self.rate

    class Meta:
        verbose_name = 'Рейтинг'
        verbose_name_plural = 'Рейтинги'


class Kino(models.Model):
    title = models.CharField(max_length=30, verbose_name='Название')
    genre = models.ForeignKey(Genre, on_delete=models.SET_DEFAULT, default=1, verbose_name='Жанр')
    rating = models.FloatField(verbose_name='Оценка')
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True, verbose_name='Страна')
    director = models.ForeignKey(Director, on_delete=models.SET_NULL, null=True, verbose_name='Режисер')
    summary = models.TextField(max_length=500, verbose_name='Описание')
    year = models.IntegerField(verbose_name='Год')
    ager = models.ForeignKey(AgeRate, on_delete=models.SET_NULL, null=True, verbose_name='Рейтинг')
    actor = models.ManyToManyField(Actor, verbose_name='Актер')
    status = models.ForeignKey(Status, on_delete=models.SET_DEFAULT, default=1, verbose_name='Подписка')
    image = models.CharField(max_length=100, blank=True, null=True, verbose_name='Картинка')
    link = models.URLField(max_length=200, blank=True, null=True, verbose_name='Ссылка фильма')

    def __str__(self):
        return self.title

    def display_actors(self):
        res = ''
        for a in self.actor.all():
            res += a.lname + ' ' + a.fname
        return res
    display_actors.short_description = 'Актеры'

    def get_absolute_url(self):
        # return reverse('info', kwargs={'pk': self.pk, 'title': self.title})
        return reverse('info', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = 'Фильм'
        verbose_name_plural = 'Фильмы'
        ordering = ['-year']


class Commentary(models.Model):
    post = models.ForeignKey(Kino, on_delete=models.CASCADE, related_name='comments', verbose_name='Комментарий')
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Пользователь')
    body = models.TextField(max_length=1000, null=True, blank=True, verbose_name='Текст')
    time_created = models.DateTimeField(auto_now_add=True, null=True, blank=True, verbose_name='Время создания')
    publish = models.BooleanField(default=True, verbose_name='Видимость поста')
    #  --------------  Теперь добавим лайки --------------------------
    likes = models.ManyToManyField(User, related_name="meep_like", blank=True, verbose_name='Лайки')
    liked = models.ManyToManyField(User, related_name='liked_commentaries')
    disliked = models.ManyToManyField(User, related_name='disliked_commentaries')

    # ---------------   Отслеживаем количество лайков -------------------
    # def number_of_likes(self):
    #     return self.likes.count()

    # ---------------   Отслеживаем количество лайков -------------------
    def number_of_liked(self):
        return self.liked.count()

    def number_of_disliked(self):
        return self.disliked.count()

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
        ordering = ['-time_created']

    def get_absolute_url(self):
        return reverse('commentar', kwargs={'pk': self.pk})

    # def get_absolute_url(self):
    #     if self.pk:
    #         return reverse('commentar', kwargs={'pk': self.post.pk})
    #     # Если pk пусто или None, можете вернуть другой URL или None
    #     return None
    # def get_absolute_url(self):
    #     if self.pk and self.post.pk:
    #         print(f'pk value: {self.pk}', 'opopop')
    #         return reverse('commentar', kwargs={'pk': self.post.pk})
    #     return None
    # def get_absolute_url(self):
    #     if self.pk and self.post.pk:
    #         print(f'pk value: {self.pk}', 'opopop')
    #         try:
    #             comment = Commentary.objects.get(pk=1)
    #             url = comment.get_absolute_url()
    #             print(url)
    #             return reverse('commentar', kwargs={'pk': self.post.pk})
    #         except Commentary.DoesNotExist:
    #             print("Commentary object with pk=1 does not exist")
    #     return None

    def __str__(self):
        return self.body

class Likes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Пользователь')
    comit = models.ForeignKey(Kino, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Комментарий фильма')
    like_comment = models.BooleanField(verbose_name='Оценка товара')  # True - лайк, False - дизлайк

    # def __str__(self):
    #     return self.like_comment
    def __str__(self):
        return f'{self.user} - {self.comit}: {"Лайк" if self.like_comment else "Дизлайк"}'

    def get_absolute_url(self):
        return reverse('like', kwargs={'id': self.id})

    class Meta:
        verbose_name = 'Лайк'
        verbose_name_plural = 'Лайки'

class VisitsCounter(models.Model):
    url = models.CharField(max_length=200, null=True, blank=True, verbose_name='Адресс сайта')
    count = models.IntegerField(default=0, null=True, blank=True, verbose_name='Счетчик посещений')

    def __str__(self):
        return f"{self.url} - {self.count} visits"


# # ------------  Пробуем создать лайки  вот с лайки с твитера  -----------------
# class Meep(models.Model):
#     user = models.ForeignKey(User, related_name="meeps", on_delete=models.DO_NOTHING)
#     body = models.CharField(max_length=200)
#     create_at = models.DateTimeField(auto_now_add=True)
# #  --------------  Теперь добавим лайки --------------------------
#     likes = models.ManyToManyField(User, related_name="meep_like", blank=True)
#
# # ---------------   Отслеживаем количество лайков -------------------
#     def number_of_likes(self):
#         return self.likes.count()



#  #  -----  Можно попробывать такой вариант лайк дизлайк -------------
# class Commentary(models.Model):
#     post = models.ForeignKey(Kino, on_delete=models.CASCADE, related_name='comments', verbose_name='Комментарий')
#     user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Пользователь')
#     body = models.TextField(max_length=1000, null=True, blank=True, verbose_name='Текст')
#     time_created = models.DateTimeField(auto_now_add=True, null=True, blank=True, verbose_name='Время создания')
#     publish = models.BooleanField(default=True, verbose_name='Видимость поста')
#     hot = models.ManyToManyField(User, related_name='forhot', verbose_name='Добавить лайк')
#     n_not = models.ManyToManyField(User, related_name='forhot', verbose_name='Удалить лайк')
#
#  #  ----------  Во views пишем  ---------------------
#
# def hot(request, id):
#     currentComit = Commentary.objects.get(id=id)
#     currentUser = request.user
#     # ----------------------   Логика дабовления горячего  --------------------
#     for i in currentComit.hot.all():
#         if i == currentUser:
#             currentComit.hot.remove(currentUser)
#             break
#         else:
#             for i in currentComit.n_not.all():
#                 if i == currentUser:
#                     currentComit.n_not.remove(currentUser)
#                     break
#                 else:
#                     currentComit.hot.add(currentUser)
#     return redirect('info')
#
#
# def n_not(request, id):
#     currentComit = Commentary.objects.get(id=id)
#     currentUser = request.user
#     # ----------------------   Логика дабовления горячего  --------------------
#     for i in currentComit.n_not.all():
#         if i == currentUser:
#             currentComit.n_not.remove(currentUser)
#             break
#         else:
#             for i in currentComit.hot.all():
#                 if i == currentUser:
#                     currentComit.hot.remove(currentUser)
#                     break
#                 else:
#                     currentComit.n_not.add(currentUser)
#     return redirect('info')

