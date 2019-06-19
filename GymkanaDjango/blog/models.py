import datetime

from django.db import models
from django.utils.translation import ugettext as _

# Create your models here.


class BaseItems(models.Model):
    title = models.CharField(_('Título'), max_length=200)
    subtitle = models.CharField(_('Subtítulo'), max_length=200)
    body = models.TextField(_('Cuerpo'))

    class Meta:
        abstract = True


class New (BaseItems):
    publish_date = models.DateField(_('Fecha de publicación'), default=datetime.date.today)
    image = models.ImageField(_('Imagen'), upload_to='media/%Y/%m/%d/', default='media/djangoworld.png')

    class Meta:
        verbose_name = 'Noticia'
        verbose_name_plural = 'Noticias'


class Event(BaseItems):
    start_date = models.DateField(_('Fecha de comienzo'), default=datetime.date.today)
    end_date = models.DateField(_('Fecha de finalización'))

    class Meta:
        verbose_name = 'Evento'
        verbose_name_plural = 'Eventos'
