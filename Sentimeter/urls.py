"""Sentimeter URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include,url
from django.contrib import admin
from team.views import team
from game.views import game
from base.views import home
from base.views import compare

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^team/([A-Z]+)/', team, name='team'),
    url(r'^game/([A-Z]+)_([A-Z]+)/', game, name='game'),
	url(r'^about/', include('base.urls'), name='about'),
	url(r'^$', home, name='home'),
	url(r'^compare/', compare, name='compare'),
]
