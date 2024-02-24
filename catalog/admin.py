from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Genre)
# admin.site.register(Director)
# admin.site.register(Actor)
admin.site.register(AgeRate)
# admin.site.register(Status)
# admin.site.register(Kino)
admin.site.register(Country)
# admin.site.register(Comment)


class Actoradmin(admin.ModelAdmin):
    list_display = ('fname','lname','born') #  столбики в панели админа
    list_display_links = ('fname','lname')  #   работают как ссылки
admin.site.register(Actor,Actoradmin)  #  регистрируем модель актер


class Directoradmin(admin.ModelAdmin):
    list_display = ('fname','lname') #  столбики в панели админа
    list_display_links = ('fname','lname')  #   работают как ссылки
admin.site.register(Director,Directoradmin)  #  регистрируем модель режисер

class Kinoadmin(admin.ModelAdmin):
    list_display = ('title','year','director','display_actors')
    list_filter = ('status','genre','rating')
    fieldsets = (('о фильме',{'fields':('title','summary','actor')}),
                ('Рейтинг',{'fields':('rating','ager','status')}),
                 ('Остальное',{'fields':('genre','country','director','year','image')}))
admin.site.register(Kino, Kinoadmin)

class Stinline(admin.TabularInline):
    model = Kino


class Statusadmin(admin.ModelAdmin):
    inlines = [Stinline]
admin.site.register(Status, Statusadmin)



# class CommentAdmin(admin.ModelAdmin):
#     list_display = ('name', 'email', 'post', 'publish', 'active')
#     list_filter = ('active', 'publish', 'name')
#     search_fields = ('name', 'email', 'body')
#     date_hierarchy = 'publish'
# admin.site.register(Comment, CommentAdmin)

# @admin.register(Comment)
# class CommentAdmin(admin.ModelAdmin):
#     list_display = ('name', 'body', 'post', 'created_on', 'active')
#     list_filter = ('active', 'created_on')
#     search_fields = ('name', 'email', 'body')
#     actions = ['approve_comments']
#
#     def approve_comments(self, request, queryset):
#         queryset.update(active=True)