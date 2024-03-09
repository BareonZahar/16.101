"""
URL configuration for django09 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from catalog import views
urlpatterns = (
    path('admin/', admin.site.urls),
    path('', views.index, name='home'),
    path('kino/', views.Kinolist123.as_view(), name='allkino'),
    path('kino/<int:pk>/', views.KinoDetail.as_view(), name='info'),
    # path('kino/<int:pk>/<str:title>/', views.KinoDetail.as_view(), name='info'),

    # path('kino/(?P<pk>[0-9]+)/(?P<title>[^/]+)/\Z', views.KinoDetail.as_view(), name='info'),
    # path('commentar/<int:pk>/', views.commentar, name='commentar'),
    path('user/', include('django.contrib.auth.urls')),
    path('actor/', views.Actorlist.as_view(), name='actor'),
    path('actor/<int:pk>/<str:lname>/', views.ActorDetail.as_view(), name='infor'),
    path('director/', views.Directorlist.as_view(), name='director'),
    path('director/<int:pk>/', views.DirectorDetail.as_view(), name='intdir'),
    path('ganry/', views.ganry, name='ganry'),
    path('ganry/pro_ganry/<int:id>/', views.pro_ganry, name='pro_ganry'),
    path('status/', views.status, name='status'),
    path('status/prosmotr/<int:id1>/<int:id2>/<int:id3>/', views.prosmotr, name='prosmotr'),
    path('status/buy/<int:type>/', views.buy, name='buystatus'),
    path('kuppodpiska/', views.kuppodpiska, name='kuppodpiska'),
    path('otsuper/<int:type>/', views.otsuper, name='otsuper'),
    path('user/registr', views.registr, name='registr'),
#  ------------  Для лайков из твитера  -----------------------
    path('meep_like/<int:pk>/', views.meep_like, name="meep_like"),
    path('like_commentary/<int:pk>/', views.like_commentary, name="like_commentary"),
    path('dislike_commentary/<int:pk>/', views.dislike_commentary, name="dislike_commentary"),

  #  ------  url для новых лайков ---------------
  #   path('hot/<int:id', views.hot, name='hot'),
  #   path('n_not/<int:id', views.n_not, name='n_not')
)
