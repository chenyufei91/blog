from django.contrib.syndication.views import Feed
from .models import Post


class AllPostRessFeed(Feed):
    title = 'fly的博客'
    link = '/'
    description = 'fly的博客'

    # 需要显示的内容条目
    def items(self):
        return Post.objects.all()

    # 聚合器中显示的内容条目的标题
    def item_title(self, item):
        return '[%s] %s' % (item.category, item.title)

    def item_description(self, item):
        return item.body
