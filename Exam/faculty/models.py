from django.db import models
from django.contrib.auth.models import User


class FacultyInfo(models.Model):
    # 定义一个与User模型一对一关联的外键，当关联的User被删除时，该记录也会被删除
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # 定义一个字符字段，用于存储地址信息，最大长度为200，可以为空
    address = models.CharField(max_length=200, blank=True)
    # 定义一个字符字段，用于存储科目信息，最大长度为50，可以为空
    subject = models.CharField(max_length=50, blank=True)
    # 定义一个图片字段，用于存储教职员工的头像，上传路径为'faculty_profile_pics'，可以为空
    picture = models.ImageField(upload_to = 'faculty_profile_pics', blank=True)

    # 定义对象的字符串表示方法，返回关联的User的用户名
    def __str__(self):
        return self.user.username
    
    # 定义模型的元数据
    class Meta:
        # 设置模型在后台显示的复数名称为'Faculty Info'
        verbose_name_plural = 'Faculty Info'