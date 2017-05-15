__author__ = 'chaga'
from django.conf.urls import url
from .views import (
    landing_home
)
urlpatterns = [

    url(r'^$', landing_home, name='home'),

]