from django.db import models
from django.contrib.auth.models import AbstractUser
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFit
# Create your models here.


class User(AbstractUser):
    # 用户昵称(唯一）
    nickname = models.CharField(max_length=50, verbose_name='昵称')
    avatar = ProcessedImageField(upload_to='avatar',
                                 default='avatar/default.jpg',
                                 processors=[ResizeToFit(80, 80)], verbose_name='用户头像')

    def __str__(self):
        return self.username

    # 用户上传图片放入以账户命名的文件夹下
    def save(self, *args, **kwargs):
        # 用户上传的avatar.name为： '文件名'
        # print(self.avatar.name+'===1===')
        # 拼接出'username/文件名’，调用父类save
        # 便可变为‘upload_to/username/avatar.name
        # 其余情况直接save便可
        if len(self.avatar.name.split('/')) == 1:
            self.avatar.name = self.username+'/' + self.avatar.name
            # print(self.avatar.name+'===2===')

        super(User, self).save()

    class Meta(AbstractUser.Meta):
        pass