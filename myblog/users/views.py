from django.shortcuts import render, redirect
from .forms import RegisterForm, UserDetailForm
from django.views.decorators.http import require_GET, require_POST, require_http_methods
from django.contrib.auth.decorators import login_required
# Create your views here.


@require_http_methods(['GET', 'POST'])
def register(request):
    # 获取传递来的next
    # 若为get请求，获取传入来的next 若直接访问，无next，注册成功之后跳转到首页
    # 当注册成功发出post请求时，获取之前get的next
    redirect_to = request.POST.get('next', request.GET.get('next', ))

    # 若用户已登录 跳转到首页
    if request.user.is_authenticated:
        return redirect('/')

    # 请求为POST 表面用户提交了注册信息
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        # 验证数据是否合法
        if form.is_valid():
            # 若合法调用表单save方法将用户数据保存到数据库
            form.save()

            if redirect_to:
                # 注册成功，跳转回之前页面
                return redirect(redirect_to)
    else:
        # 请求不是POST，显示注册页面
        form = RegisterForm()
    # 将get请求传来的next继续传递给模板
    return render(request, 'users/register.html', {'form': form, 'next': redirect_to})


@login_required
def user_detail(request):
    information = ''
    # 若为POST请求，代表用户修改数据
    if request.method == 'POST':

        form = UserDetailForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            information = '修改成功！'

    # 若为GET请求, 显示表单即可
    form = UserDetailForm(instance=request.user)
    return render(request, 'users/user_detail.html', {'form': form, 'information': information})


