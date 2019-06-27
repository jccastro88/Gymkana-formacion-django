from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from blog.views import PortadaList, newscreate, newslist, newsdetail, newsupdate, newsdelete, NewsCreate, NewsList, \
    NewsDetail, NewsUpdate

app_name = 'blog'

urlpatterns = [

    path('', PortadaList.as_view(), name='portada_List'),
    path('v1/news/create', newscreate, name='new_create'),
    path('v1/news/list', newslist, name='new_list'),
    path('v1/news/<id>', newsdetail, name='new_detail'),
    path('v1/news/update/<id>', newsupdate, name='new_update'),
    path('v1/news/delete/<id>', newsdelete, name='new_delete'),
    path('v2/news/create', NewsCreate.as_view(), name='new_create2'),
    path('v2/news/list', NewsList.as_view(), name='new_list2'),
    path('v2/news/<pk>', NewsDetail.as_view(), name='new_detail2'),
    path('v2/news/update/<pk>', NewsUpdate.as_view(), name='new_upload2'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
