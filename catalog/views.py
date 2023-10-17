from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.models import User,Group
# Create your views here.
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
    return render(req,'index.html' , context=data)


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


    # if id3 != 0:
    #     status = User.objects.get(id=id3)  # нашли юзера
    #     print(status)
    #     status = status.groups.all()  # нашли его подписки
    #     print(status)
    #     status = status[0].id  # нашли айди его подписки(она одна)
    #     print(status)
    # k3 = Group.objects.get(status)
    # k2 = Status.objects.get(id=id2).name
    # k4 = Kino.objects.get(id2).title
    # data = {'k4':k4,'k3':k3,'k2':k2}

    # print(id1, id2, id3)
    # if id3 != 0:
    #     status = User.objects.get(id=id3)  #  нашли юзера
    #     print(status)
    #     status = status.groups.all()  # нашли его подписки
    #     print(status)
    #     status = status[0].id  #  нашли айди его подписки(она одна)
    #     print(status)
    # else:
    #     if id3 == 0:
    #         status = 1
    # if status >= id2:
    #     print('ok')
    #     permission = True
    # else:
    #     print('nelzy')
    #     permission = False
    #
    # if status == id3:
    #     k4 = Status.objects.get(id=id3).name
    #     data = {'k4':k4}
    #     print(k4)
    # elif status == id2:
    #     k4 = Status.objects.get(id=id2).name
    #     data = {'k4': k4}
    #     print(k4)
    # else:
    #     k4 = Status.objects.get(id=id1).name
    #     data = {'k4': k4}
    #     print(k4)
    # k1 = Kino.objects.get(id=id1).title
    # k2 = Group.objects.get(id=status).name
    # k3 = Status.objects.get(id=id2).name


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
    paginate_by = 7

class DirectorDetail(generic.DetailView):
    model = Director

from django.http import HttpResponse
# def info(req,id):
#     film = Kino.objects.get(id=id)
#     return HttpResponse(film.title)
# def proactor(req):
#     name = Actor.objects.all()
#     # gim = ''
#     # for i in name:
#     #     gim = i.fname +'  ' +i.lname
#     #     # gam
#     #     print(gim)
#     data = {'k1':name}
#     return render(req,'new.html',context=data)
#



