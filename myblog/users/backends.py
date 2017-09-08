from .models import User


# 邮箱认证登录
class EmailBackend(object):
    def authenticate(self, **credentials):
        # 表单中用户输入的用户名或者邮箱 Field名都是username
        email = credentials.get('username')
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return None
        else:
            if user.check_password(credentials.get("password")):
                return user

    def get_user(self, user_id):

        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None