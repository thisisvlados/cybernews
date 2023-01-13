from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect, get_object_or_404


from .models import News, Comments
from .forms import NewsForm, CommentForm
from django.views.generic import UpdateView, DeleteView
from django.http import Http404


def news(request):
    news_sorting = News.objects.filter(category__name='News').order_by('-date')
    return render(request, 'cyber_news/news.html', {'news': news_sorting})


def NewsDetailView(request, pk):
    new = get_object_or_404(News, id=pk)
    comment = Comments.objects.filter(new=pk, moderation=True)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.new = new
            form.save()
            return redirect(NewsDetailView, pk)
    else:
        form = CommentForm()
    return render(request, "cyber_news/details_view.html",
                  {"new": new,
                   "comments": comment,
                   "form": form})


class NewsUpdateView(UpdateView):
    model = News
    template_name = 'cyber_news/create_news.html'

    form_class = NewsForm


class NewsDeleteView(DeleteView):
    model = News
    success_url = '/news/'
    template_name = 'cyber_news/delete_news.html'


def AddLike(request, pk):
    try:
        news = News.objects.get(pk=pk)
        news.likes += 1
        news.save()
    except ObjectDoesNotExist:
        raise Http404
    return redirect(request.META.get('HTTP_REFERER'))


def news_create(request):
    error = ''
    if request.method == 'POST':
        form = NewsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('news')
        else:
            error = 'Форма была неверной'

    form = NewsForm()

    data = {
        'form': form,
        'error': error
    }

    return render(request, 'cyber_news/create_news.html', data)


def news_dota(request):
    news_sorting = News.objects.filter(category__name='Dota').order_by('-date')
    return render(request, 'cyber_news/news_dota.html', {'news_dota': news_sorting})


def news_csgo(request):
    news_sorting = News.objects.filter(category__name='CSGO').order_by('-date')
    return render(request, 'cyber_news/news_csgo.html', {'news_csgo': news_sorting})


def news_pubg(request):
    news_sorting = News.objects.filter(category__name='PUBG').order_by('-date')
    return render(request, 'cyber_news/news_pubg.html', {'news_pubg': news_sorting})


def news_valorant(request):
    news_sorting = News.objects.filter(category__name='Valorant').order_by('-date')
    return render(request, 'cyber_news/news_valorant.html', {'news_valorant': news_sorting})


