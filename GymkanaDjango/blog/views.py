from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView
from blog.forms import NewsForm
from blog.models import New, Event


class PortadaList(ListView):
    template_name = 'portada_blog.html'

    def get_queryset(self):
        return {
            'event': Event.objects.order_by('start_date').reverse()[:3],
            'new': New.objects.order_by('publish_date').reverse()[:3],
        }


def newscreate(request):
    if request.method == 'POST':
        form = NewsForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()
        return redirect('blog:new_create')
    else:
        form = NewsForm()
    return render(request, 'news_form.html', {'form': form})


def newslist(request):
    news = New.objects.order_by('publish_date').all()
    return render(request, 'lists.html', {'objects': news})


def newsdetail(request, id=None):
    news = New.objects.get(id=id)
    return render(request, 'detail.html', {'object': news})


def newsupdate(request, id=None):
    news = New.objects.get(id=id)
    form = NewsForm(request.POST or None, request.FILES or None, instance=news)
    if form.is_valid():
        form.save()
    return render(request, 'news_form.html', {'news': news, 'form': form})


def newsdelete(request, id):
    news = New.objects.get(id=id)
    if request.method == 'POST':
        news.delete()
        return redirect('blog:new_list')
    return render(request, 'delete.html', {'object': news})

