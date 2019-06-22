from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from blog.views import PortadaList, newsview

urlpatterns = [

    path('', PortadaList.as_view(), name='portada_List'),
    path('v1/news/create', newsview, name='new_create'),
    # path('event', EventList.as_view(), name='events_list'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
