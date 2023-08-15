from django import template
from app_news.models import Post


register = template.Library()


@register.inclusion_tag('app_prof_dev/banner.html')
def show_news():
    news = Post.objects.all()[0:3]
    return {'news': news}
