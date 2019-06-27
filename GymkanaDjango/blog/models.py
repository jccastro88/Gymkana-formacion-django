import datetime

from django.core.validators import FileExtensionValidator
from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext as _

from blog.validators import validate_file_size


class BaseItems(models.Model):
    title = models.CharField(_('Título'), max_length=200)
    subtitle = models.CharField(_('Subtítulo'), max_length=200)
    body = models.TextField(_('Cuerpo'))

    class Meta:
        abstract = True


class New (BaseItems):
    publish_date = models.DateField(_('Fecha de publicación'), auto_now=True)
    image = models.ImageField(_('Imagen'), upload_to='media', default='media/djangoworld.png', null=True, blank=True,
                              validators=[validate_file_size, FileExtensionValidator(['jpg', 'png']), ])

    def get_absolute_url(self):
        return reverse('blog:new_detail2', kwargs={'pk':self.id})

    class Meta:
        verbose_name = 'Noticia'
        verbose_name_plural = 'Noticias'


class Event(BaseItems):
    start_date = models.DateField(_('Fecha de comienzo'), default=datetime.date.today)
    end_date = models.DateField(_('Fecha de finalización'))

    class Meta:
        verbose_name = 'Evento'
        verbose_name_plural = 'Eventos'
