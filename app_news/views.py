from django.core.paginator import Paginator
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404

from app_news.forms import CommentForm
from app_news.models import PostNews


def news_list_view(request):
    news = PostNews.objects.all().select_related('category')
    paginator = Paginator(news, 8)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'news_templates/news_grid.html', context={'news': news, 'page_obj': page_obj,})


def news_detail_view(request: HttpRequest, slug) -> HttpResponse:
    post = get_object_or_404(PostNews, slug=slug)
    comments = post.comments.all()
    new_comment = False
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
    else:
        comment_form = CommentForm()
    context = {
        'post': post,
        'comments': comments,
        'new_comment': new_comment,
        'comment_form': comment_form,
    }
    return render(request, 'news_templates/news_detail.html', context=context)
