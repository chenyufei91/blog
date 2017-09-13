from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.html import strip_tags
from myblog.settings import AUTH_USER_MODEL
import markdown
from markdownx.models import MarkdownxField
# Create your models here.


# =========================分---类====================================
class Category(models.Model):

    name = models.CharField(max_length=100, help_text='类别')

    def __str__(self):
        return self.name


class Tag(models.Model):

    name = models.CharField(max_length=100, help_text='标签名')

    def __str__(self):
        return self.name

# ===============================文---章====================================


class Post(models.Model):

    title = models.CharField(max_length=100, help_text='文章名')
    # body = models.TextField(help_text='文章内容')
    body = MarkdownxField(help_text='文章内容')
    created_time = models.DateTimeField(help_text='创建时间')
    modified_time = models.DateTimeField(auto_now=True, help_text='修改/更新时间')
    excerpt = models.CharField(max_length=200, blank=True, help_text='摘要')
    is_delete = models.BooleanField(default=False, help_text='删除标记')
    title_img = models.ImageField(upload_to='title_img/', default='title_img/default.jpg', help_text='标题图片')

    views = models.PositiveIntegerField(default=0, help_text='文章阅读量')

    category = models.ForeignKey(Category, help_text='类别')
    tag = models.ManyToManyField(Tag, help_text='标签')
    author = models.ForeignKey(AUTH_USER_MODEL, help_text='作者')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'pk': self.pk})

    # 增加阅读量
    def increase_views(self):
        self.views += 1
        self.save(update_fields=['views'])

    def save(self, *args, **kwargs):
        md = markdown.Markdown(extensions=[
            'markdown.extensions.extra',
            'markdown.extensions.codehilite',

        ])

        self.excerpt = strip_tags(md.convert(self.body))[:150]+'...'
        '''
        # print(self.title_img.name+'11111=============')
        # 上传图片时判断，上传时name为'文件名' split后长度为1
        # 此时加上title拼接成'title/文件名'
        # 当调用父类的save时 会生成'upload_to/title/文件名/'
        # 此后当访问页面时 调用到此save方法会在原有基础上不断加title
        # 因此当split ！= 1 时，直接调用原来的save便可
        if len(self.title_img.name.split('/')) == 1:
            # 将上传的文章标题图片保存到其id的文件夹下
            self.title_img.name = str(self.pk)+'/'+self.title_img.name
        # print(self.title_img.name)
        '''

        super(Post, self).save()