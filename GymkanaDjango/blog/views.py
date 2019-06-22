from django.shortcuts import render, redirect
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


def newsview(request):
    if request.method == 'POST':
        form = NewsForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()
        return redirect('new_create')
    else:
        form = NewsForm()
    return render(request, 'news_form.html', {'form': form})

