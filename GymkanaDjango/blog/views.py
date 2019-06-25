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
        return redirect('new_create')
    else:
        form = NewsForm()
    return render(request, 'news_form.html', {'form': form})


def newslist(request):
    news = New.objects.order_by('publish_date').all()
    context = {'objects': news}
    return render(request, 'lists.html', context)


def newsdetail(request, id=None):
    news = New.objects.get(id=id)
    context = {'object': news}
    return render(request, 'detail.html', context)


def newsupdate(request, id=None):
    news = New.objects.get(id=id)
    form = NewsForm(request.POST or None, request.FILES or None, instance=news)
    # import ipdb; ipdb.set_trace()
    if form.is_valid():
        form.save()
    # return redirect('new_update')
    return render(request, 'news_form.html', {'news': news, 'form': form})


