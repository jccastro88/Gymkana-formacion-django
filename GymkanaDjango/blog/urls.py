from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from blog.views import PortadaList, newscreate, newslist, newsdetail

app_name = 'blog'

urlpatterns = [

    path('', PortadaList.as_view(), name='portada_List'),
    path('v1/news/create', newscreate, name='new_create'),
    path('v1/news/list', newslist, name='new_list'),
    path('v1/news/<id>', newsdetail, name='new_detail'),

    # path('v1/news/(?P<id>\d+)/$', newslist, name='new_detail'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
