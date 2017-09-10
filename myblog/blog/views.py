from django.shortcuts import render, get_object_or_404
from blog.models import Post, Category, Tag
import markdown
from django.views.generic import ListView
from utils.pagination import pagination_data

# Create your views here.

# ==========================首页=========================================

# def index(request):
#     post_list = Post.objects.all().order_by('-created_time')
#     post_list = [post_list[i:i+2] for i in range(0, len(post_list), 2)]
#     return render(request, 'blog/index.html', {'post_list': post_list})


class IndexView(ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'post_list'
    paginate_by = 4

    def get_queryset(self):
        post = super(IndexView, self).get_queryset().order_by('-created_time')
        post = [post[i:i+2] for i in range(0, len(post), 2)]
        return post

    def get_context_data(self, **kwargs):
        # 获取父类生成的传递给模板的字典
        context = super(IndexView, self).get_context_data()
        paginator = context.get('paginator')
        page = context.get('page_obj')
        is_paginated = context.get('is_paginated')

        # 获取显示分页范围page_range，并加入到字典
        data = pagination_data(paginator, page, is_paginated)
        context.update(data)

        return context


class PostView(ListView):
    model = Post
    template_name = 'blog/post.html'
    context_object_name = 'post_list'
    paginate_by = 10

    def get_queryset(self):
        post = super(PostView, self).get_queryset().order_by('-created_time')
        return post

    def get_context_data(self, **kwargs):
        # 获取父类生成的传递给模板的字典
        context = super(PostView, self).get_context_data()
        paginator = context.get('paginator')
        page = context.get('page_obj')
        is_paginated = context.get('is_paginated')

        # 获取显示分页范围page_range，并加入到字典
        data = pagination_data(paginator, page, is_paginated)
        context.update(data)

        return context

# ===================详情页==================================================


def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.increase_views()
    post.body = markdown.markdown(post.body, extensions=[
                                     'markdown.extensions.extra',
                                     'markdown.extensions.codehilite',
                                     'markdown.extensions.toc',
                                 ])

    return render(request, 'blog/detail.html', {'post': post})


# =========================归档==================================================
# def archives(request, year, month):
#     post_list = Post.objects.filter(created_time__year=year, created_time__month=month).order_by('-created_time')
#     return render(request, 'blog/post.html', {'post_list': post_list})
class ArchivesView(ListView):
    model = Post
    template_name = 'blog/post.html'
    context_object_name = 'post_list'
    paginate_by = 10

    def get_queryset(self):
        year = self.kwargs.get('year')
        month = self.kwargs.get('month')
        return super(ArchivesView, self).get_queryset().filter(created_time__year=year, created_time__month=month).\
            order_by('-created_time')

    def get_context_data(self, **kwargs):
        # 获取父类传递给模板的字典
        context = super(ArchivesView, self).get_context_data()
        paginator = context.get('paginator')
        page = context.get('page_obj')
        is_paginated = context.get('is_paginated')

        # 获取显示分页范围pag_range，更新入字典
        data = pagination_data(paginator, page, is_paginated)
        context.update(data)

        # 获取当前页类型，更新入字典
        year = self.kwargs.get('year')
        month = self.kwargs.get('month')
        page_name = {'page_name': year+'年'+month+'月'}
        context.update(page_name)
        return context

# =================================分类======================================
# def category(request, pk):
#     cate = get_object_or_404(Category, pk=pk)
#     post_list = Post.objects.filter(category=cate).order_by('-created_time')
#     return render(request, 'blog/post.html', {'post_list': post_list})


class CategoryView(ListView):
    model = Post
    template_name = 'blog/post.html'
    context_object_name = 'post_list'
    paginate_by = 10

    def get_queryset(self):
        cate = get_object_or_404(Category, pk=self.kwargs.get('pk'))
        return super(CategoryView, self).get_queryset().filter(category=cate).order_by('-created_time')

    def get_context_data(self, **kwargs):
        # 获取父类传递给模板的字典
        context = super(CategoryView, self).get_context_data()
        paginator = context.get('paginator')
        page = context.get('page_obj')
        is_paginated = context.get('is_paginated')

        # 获取显示分页范围page_range，更新入字典
        data = pagination_data(paginator, page, is_paginated)
        context.update(data)

        # 获取当前页类型，更新入字典
        cate = get_object_or_404(Category, pk=self.kwargs.get('pk'))
        page_name = {'page_name': cate.name}
        context.update(page_name)
        return context


# ================================标签===========================================


class TagView(ListView):
    model = Post
    template_name = 'blog/post.html'
    context_object_name = 'post_list'
    paginate_by = 10

    def get_queryset(self):
        tag = get_object_or_404(Tag, pk=self.kwargs.get('pk'))
        return super(TagView, self).get_queryset().filter(tag=tag).order_by('-created_time')

    def get_context_data(self, **kwargs):
        # 获取父类传递给模板的字典
        context = super(TagView, self).get_context_data()
        paginator = context.get('paginator')
        page = context.get('page_obj')
        is_paginated = context.get('is_paginated')

        # 获取显示分页范围page_range,更新入字典
        data = pagination_data(paginator, page, is_paginated)
        context.update(data)

        # 获取当前页类型，更新入字典
        tag = get_object_or_404(Tag, pk=self.kwargs.get('pk'))
        page_name = tag.name
        context.update({'page_name': page_name})
        return context


# ==========================404 500 403=====================
def page_not_found(request):
    return render(request, '404.html')


def page_error(request):
    return render(request, '500.html')