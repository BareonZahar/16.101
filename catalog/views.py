from django.shortcuts import render,redirect
from django.template.defaultfilters import title

from .models import *
from django.contrib.auth.models import User,Group
# Create your views here.
# def comment(req):
#     return render(req,'registration/navbar.html')
from catalog import views

# from django.conf import settings
# from django.core.mail import send_mail
#
# # headers = {'To': '{} <{}>'.format(user.get_full_name(), 'zatst2000@yandex.ru')}
# # headers = headers
# send_mail('Тема', 'Тело письма', settings.EMAIL_HOST_USER, ['zatst2000@yandex.ru'])

def index(req):
    numkino = Kino.objects.all().count()
    numactor = Actor.objects.all().count()
    numfree = Kino.objects.filter(status__kino=1).count()
    # username = req.user.last_name if hasattr(req.user, 'last_name') else 'Гость'
    # username = req.user.first_name
    if req.user.username:
        username = req.user.first_name
        # print(req.user.first_name,'#',req.user.id)  #   Для проверки что выводит
    else:
        username = 'Гость'
        # print(req.user.id)   #  Для проверки что выводит
    data = {'k1':numkino,'k2':numactor,'k3':numfree,'username':username}
    # user = User.objects.create_user('user2','user2@mail.ru','useruser')
    # user.first_name = 'Vlad'  #  ------------Програмно регистрировали пользователя -------------
    # user.last_name = 'Petrov'
    # user.save()
    return render(req,'index.html', context=data)


def ganry(req):
    k2 = Genre.objects.all()
    print(k2, 'нет ничего')
    data = {'ganry':k2}
    return render(req,'new.html',data)

def pro_ganry(req,id):
    k1 = Genre.objects.get(id=id)
    k2 = k1.kino_set.all()
    data = {'k2':k2}
    return render(req, 'new.html', data)

def film(req):
    p1 = Kino.objects.all()
    # print(p1)
    # p2 = p1.get(id=1)
    # print(p2)
    # p3 = p2.title
    # print(p3)
    data = {'film':p1}
    return render(req,'film.html',data)
def film_film(req):
    p1 = Kino.objects.all()
    data ={'p1':p1}
    return render(req,'film_film.html',data)


def status(req):
    k1 = Status.objects.all()
    print(k1)
    data = {'podpiska':k1}
    return render(req,'podpiska.html',data)

def prosmotr(req,id1,id2,id3):
    print(id1,id2,id3)
    mas = ['бесплатно','базовая','супер']  #  kino id2
    mas2 = ['free','based','super']   #  user  id3  status
    if id3 != 0:
        status = User.objects.get(id=id3)  #  нашли юзера
        print(status)
        status = status.groups.all()  # нашли его подписки
        print(status)
        status = status[0].id  #  нашли айди его подписки(она одна)
        print(status)
    else:
        if id3 == 0:
            status = 1
    if status >= id2:
        print('ok')
        permission = True
    else:
        print('nelzy')
        permission = False
    k1 = Kino.objects.get(id=id1).title
    k2 = Group.objects.get(id=status).name
    k3 = Status.objects.get(id=id2).name
    data = {'kino':k1,'status':k2,'statuskino':k3,'prava':permission}
    return render(req,'prosmotr.html',data)


def kuppodpiska(req):
    k1 = Status.objects.get(id=1)
    k2 = k1.kino_set.all()
    free = k2.count()
    k = Status.objects.get(id=2)
    k3 = k.kino_set.all()
    based = k3.count()
    k5 = Status.objects.get(id=3)
    k4 = k5.kino_set.all()
    sup = k4.count()
    data = {'k2':k2,'k3':k3,'k4':k4,'k6':free,'k7':based,'k5':sup}
    return render(req, 'kuppodpiska.html',data)






def otsuper(req,type):
    usid = req.user.id  # находим номер текущего пользователя
    user123 = User.objects.get(id=usid)  # находим его в табличке юзер
    statusnow = user123.groups.all()[0].id  # находим номер его погдписке (группы)
    grold = Group.objects.get(id=statusnow)  # находим его подписку в таблице group
    grold.user_set.remove(user123)  # удаляем старую подписку
    grnew = Group.objects.get(id=type)  # находим новую подписку в таблице group
    grnew.user_set.add(user123)  # добовляем новую подписку
    k1 = grnew.name
    k2 = Status.objects.get(id=1)
    k3 = k2.kino_set.all()
    k9 = k3.count()
    k4 = Status.objects.get(id=2)
    k5 = k4.kino_set.all()
    k10 = k5.count()
    k6 = Status.objects.get(id=3)
    k7 = k6.kino_set.all()
    k8 = k7.count()
    data = {'otsuper':k1,'k2':k3,'k3':k5,'k4':k7,'k5':k8,'k6':k9,'k7':k10}
    return render(req,'kuppodpiska.html',data)


def buy(req,type):
    usid = req.user.id  # находим номер текущего пользователя
    user123 = User.objects.get(id=usid)  # находим его в табличке юзер
    statusnow = user123.groups.all()[0].id  # находим номер его погдписке (группы)
    grold = Group.objects.get(id=statusnow)  # находим его подписку в таблице group
    grold.user_set.remove(user123)  # удаляем старую подписку
    grnew = Group.objects.get(id=type)  # находим новую подписку в таблице group
    grnew.user_set.add(user123)  # добовляем новую подписку
    k1 = grnew.name
    k2 = Status.objects.get(id=1)
    print(k2)
    k3 = k2.kino_set.all()
    free = k3.count()
    k4 = Status.objects.get(id=2)
    k5 = k4.kino_set.all()
    based = k5.count()
    k6 = Status.objects.get(id=3)
    k7 = k6.kino_set.all()
    sup = k7.count()
    data = {'podpiska':k1,'k2':k3,'k3':k5,'k4':k7,'k5':sup,'k6':free,'k7':based}
    return render(req,'kuppodpiska.html',data)

from .form import SignUpform
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login
def registr(req):
    # anketa = SignUpform
    if req.POST:
        anketa = SignUpform(req.POST)
        if anketa.is_valid():
            anketa.save()
            k1 = anketa.cleaned_data.get('username')
            k2 = anketa.cleaned_data.get('password1')
            k3 = anketa.cleaned_data.get('first_name')
            k4 = anketa.cleaned_data.get('last_name')
            k5 = anketa.cleaned_data.get('email')
            user = authenticate(username=k1, password=k2)  # строчка регистрирует сохраняет пользователя
            man = User.objects.get(username=k1)  # найдем нового юзера
            #  заполним поля за него
            man.email = k5
            man.first_name = k3
            man.last_name = k4
            man.save()
            login(req,user)          #    вход на сайт
            group = Group.objects.get(id=1)   #   находим бесплатную подписку
            group.user_set.add(man)       #   записываем юзера в подписку
            return redirect('home')
    else:
        anketa = SignUpform()
    data = {'regform':anketa}
    return render(req,'registration/registration.html',data)


from django.views import generic


class Kinolist123(generic.ListView):
    model = Kino
    paginate_by = 5


class KinoDetail(generic.DetailView):
    model = Kino

class Actorlist(generic.ListView):
    model =Actor
    paginate_by = 4

class ActorDetail(generic.DetailView):
    model = Actor

class Directorlist(generic.ListView):
    model = Director
    paginate_by = 5

class DirectorDetail(generic.DetailView):
    model = Director


# class Commentlist(generic.ListView):
#     model = Comment
#
#
# class CommentDetail(generic.DetailView):
#     model = Comment


from django.shortcuts import render, get_object_or_404


# def comment_list(request):
#     posts = Comment.objects.all()
#     formy = CommentForm()
#     data = {'posts': posts,'formy':formy}
#     return render(request, 'blog/post/list.html', data)



# def comment_detail(request):
#     if request.method == 'POST':
#         form = CommentForm(request.POST)
#         if form.is_valid():     Новая итерпритация вывода
#             comm = form.save(commit=False)
#             comm.name = form.cleaned_data.get('name')
#             comm.body = form.cleaned_data.get('body')
#             comm.save()
#         else:
#             form = CommentForm
#         data = {'form':form}
#         return render(request,  'blog/post/detail.html', data)




from django.shortcuts import get_object_or_404
# def post_share(request, post_id):
#     # Retrieve post by id
#     post = get_object_or_404(Kino, id=post_id, status='published')
#     if request.method == 'POST':
#         # Form was submitted
#         form = EmailPostForm(request.POST)
#         if form.is_valid():
#             # Form fields passed validation
#             cd = form.cleaned_data
#             # ... send email
#     else:
#         form = EmailPostForm()
#     return render(request, 'blog/post/share.html', {'post': post,'form': form})


from .models import *
# from .form import CommentForm
# def comment_detail(request, year, month, day):
#     post = get_object_or_404(Kino,
#                                    status='published',
#                                    publish__year=year,
#                                    publish__month=month,
#                                    publish__day=day)
#     # List of active comments for this post
#     comments = post.comments.filter(active=True)
#
#     if request.method == 'POST':
#         # A comment was posted
#         comment_form = CommentForm(data=request.POST)
#         if comment_form.is_valid():
#             # Create Comment object but don't save to database yet
#             new_comment = comment_form.save(commit=False)
#             # Assign the current post to the comment
#             new_comment.post = post
#             # Save the comment to the database
#             new_comment.save()
#     else:
#         comment_form = CommentForm()
#     data = {'post': post, 'comments': comments,'comment_form': comment_form}
#     return render(request, 'blog/post/detail.html', data)


# def comment_detail(request, year, month, day):
#     post = get_object_or_404(Comment, status == 'published', publish_year=year, publish_month=month, publish_day=day)
#     data = {'post': post}
#     return render(request, 'blog/post/detail.html', data)


# def comment_detail(request, slug, year, month, day):
#     post = get_object_or_404(Comment, slug=slug, status='published', publish_year=year, publish_month=month,
#                              publish_day=day)
#     data = {'post': post}
#     return render(request, 'blog/post/detail.html', data)




# def post_share(request, post_id):
#     # Retrieve post by id
#     post = get_object_or_404(Kino, id=post_id, status='published')
#     cd = ''
#     if request.method == 'POST':
#         # Form was submitted
#         form = EmailPostForm(request.POST)
#         if form.is_valid():
#             # Form fields passed validation
#             cd = form.cleaned_data
#             # ... send email
#     else:
#         form = EmailPostForm()
#     data = {'post': post, 'form': form, 'cd': cd}
#     return render(request, 'blog/post/share.html', data)


from .models import Kino
# from .form import CommentForm
from django.shortcuts import render, get_object_or_404

# def comment_detail(request, slug):
#     template_name = 'post_detail.html'
#     post = get_object_or_404(Kino, slug=slug)
#     comments = post.comments.filter(active=True)
#     new_comment = None    # Comment posted
#     if request.method == 'POST':
#         comment_form = CommentForm(data=request.POST)
#         if comment_form.is_valid():
#             # Create Comment object but don't save to database yet
#             new_comment = comment_form.save(commit=False)
#             # Assign the current post to the comment
#             new_comment.post = post
#             # Save the comment to the database
#             new_comment.save()
#     else:
#         comment_form = CommentForm()
#     return render(request, template_name, {'post': post,
#                                            'comments': comments,
#                                            'new_comment': new_comment,
#                                            'comment_form': comment_form})



