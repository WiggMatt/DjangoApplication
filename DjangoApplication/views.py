from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone

from DjangoApplication.models import News
from DjangoApplication.forms import NewsForm


# Create your views here.

def news(request):
    news_list = News.objects.all()
    return render(request, 'DjangoApplication/news.html', {'news_list': news_list, 'title': 'Новости'})


def news_detail(request, news_id):
    news = get_object_or_404(News, pk=news_id)
    return render(request, 'DjangoApplication/news_detail.html', {'news': news})


def create_news(request):
    if request.method == 'POST':
        form = NewsForm(request.POST)
        if form.is_valid():
            news = form.save(commit=False)
            news.create_at = timezone.now()
            news.save()
            return redirect('news_detail', news.id)
    else:
        form = NewsForm()
    data = {'form': form}
    return render(request, 'DjangoApplication/create_news.html', data)


def more(request):
    return render(request, 'DjangoApplication/more.html', {"title": "More page"})


def navbar():
    return redirect("https://getbootstrap.com/docs/5.3/components/navbar/#how-it-works")
