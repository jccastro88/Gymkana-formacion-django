from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView

from blog.models import New, Event


class PortadaList(ListView):
    template_name = 'portada_blog.html'

    def get_queryset(self):
        return {
            'event': Event.objects.order_by('start_date').reverse()[:3],
            'new': New.objects.order_by('publish_date').reverse()[:3],
        }

"""
class NewList(ListView):
    model = New
    template_name = 'portada_blog.html'
    paginate_by = 3
    # context_object_name = 'news_list'


class EventList(ListView):
    model = Event
    template_name = 'portada_blog.html'
    paginate_by = 3
    context_object_name = 'events_list'
"""
