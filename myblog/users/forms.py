from django.contrib.auth.forms import UserCreationForm
from .models import User
from django.forms import ModelForm


# 用户注册表单
class RegisterForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        # 父类的默认表单控件只有 用户名、密码、确认密码这三个控件
        # （密码和确认密码在 UserCreationForm 的属性中指定）
        # 添加邮箱地址表单控件
        fields = ('username', 'email', 'nickname')


# 用户中心表单
class UserDetailForm(ModelForm):
    class Meta:
        model = User
        fields = ('nickname', 'email', 'avatar')

