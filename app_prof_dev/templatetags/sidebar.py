from django import template
from app_news.models import Post


register = template.Library()


@register.inclusion_tag('app_prof_dev/sidebar.html')
def show_ads():
    ad = Post.objects.filter(category__title='ads')[0]
    return {'ad': ad}
