from django.urls import path
from . import views
from blog.views import PortadaList

urlpatterns = [

    path('', PortadaList.as_view(), name='news_list'),
    # path('new', NewList.as_view(), name='news_list'),
    # path('event', EventList.as_view(), name='events_list'),

]
