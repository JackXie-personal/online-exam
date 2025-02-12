from django import forms 
from .models import FacultyInfo
from django.contrib.auth.models import User

class FacultyForm(forms.ModelForm):
    # 定义一个表单类，继承自Django的ModelForm，用于创建基于模型的表单
    class Meta():
        # Meta类用于定义表单的一些元数据
        model = User
        # 指定表单关联的模型为User，这意味着表单将使用User模型的结构和字段
        fields = ['username', 'email', 'password']
        # 指定表单中包含的字段，这里包括用户名、电子邮件和密码
        widgets = {
            # widgets字典用于自定义表单字段的HTML控件
            'password': forms.PasswordInput(attrs = {'id':'passwordfield','class':'form-control'}),
            # 为密码字段指定PasswordInput控件，并设置HTML属性id和class
            'email' : forms.EmailInput(attrs = {'id':'emailfield','class':'form-control'}),
            # 为电子邮件字段指定EmailInput控件，并设置HTML属性id和class
            'username' : forms.TextInput(attrs = {'id':'usernamefield','class':'form-control'})
            # 为用户名字段指定TextInput控件，并设置HTML属性id和class
        }

class FacultyInfoForm(forms.ModelForm):
    # 定义一个表单类，继承自Django的ModelForm，用于生成基于模型的表单
    class Meta():
        # Meta类用于定义表单的一些元数据
        model = FacultyInfo
        # 指定这个表单关联的模型是FacultyInfo，即表单的数据将映射到FacultyInfo模型中
        fields = ['address','subject','picture']
        # 指定表单中包含的字段，这里包括地址(address)、科目(subject)和照片(picture)
        widgets = {
            # widgets字典用于为表单字段指定自定义的HTML控件
            'address': forms.Textarea(attrs = {'class':'form-control'}),
            # 为address字段指定使用Textarea控件，并添加一个CSS类'form-control'，用于样式控制
            'subject' : forms.TextInput(attrs = {'class':'form-control'})
            # 为subject字段指定使用TextInput控件，并添加一个CSS类'form-control'，用于样式控制
        }
