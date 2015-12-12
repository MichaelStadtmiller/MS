from django.conf.urls import url
from partysource.views import *
from . import views

urlpatterns = [
    # ex: /partysource/
    url(r'^$', views.BottlesClass.as_view(), name='index'),

    # ex: /partysource/123/details
    url(r'^(?P<PSID>[0-9]+)/details$', BottleDetailsView.as_view(), name='bottle-details'),
]
