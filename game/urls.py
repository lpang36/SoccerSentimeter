from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'([A-Z]+)_([A-Z]+)/',views.game),
    ]
