from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'([A-Z]+)/',views.team,name='team'),
    ]
