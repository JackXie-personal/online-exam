from django.shortcuts import render, redirect
from django.views import View
from .forms import FacultyForm, FacultyInfoForm
from .models import FacultyInfo
from django.contrib import auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMessage
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from questions.views import has_group
from course.models import Course  # Ensure this import is present

@login_required(login_url='faculty-login')
def index(request):
    """ 教授主页：展示教授的所有课程及其试卷 """
    professor_courses = Course.objects.filter(professor=request.user).prefetch_related('exam_papers')
    return render(request, 'faculty/index.html', {'professor_courses': professor_courses})

class Register(View):
    def get(self, request):
        # 创建一个空的FacultyForm实例
        faculty_form = FacultyForm()
        # 创建一个空的FacultyInfoForm实例
        faculty_info_form = FacultyInfoForm()
        # 渲染并返回注册页面，同时传递两个表单实例作为上下文
        return render(request, 'faculty/register.html', {'faculty_form': faculty_form, 'faculty_info_form': faculty_info_form})

    def post(self, request):
        # 创建FacultyForm实例，并传入POST请求数据
        faculty_form = FacultyForm(data=request.POST)
        # 创建FacultyInfoForm实例，并传入POST请求数据
        faculty_info_form = FacultyInfoForm(data=request.POST)
        # 从POST请求数据中获取email字段
        email = request.POST['email']

        # 检查两个表单是否都有效
        if faculty_form.is_valid() and faculty_info_form.is_valid():
            # 保存FacultyForm数据到数据库
            faculty = faculty_form.save()
            # 设置用户的密码
            faculty.set_password(faculty.password)
            # 设置用户为激活状态
            faculty.is_active = True
            # 设置用户为工作人员
            faculty.is_staff = True
            # 保存用户数据
            faculty.save()

            # 获取当前网站的域名
            domain = get_current_site(request).domain
            # 设置邮件主题
            email_subject = 'Activate your Exam Portal Faculty account'
            # 设置邮件内容
            email_body = f"Hi. Please contact the admin team of {domain} to register yourself as a professor.\n\n"
            email_body += f"You are receiving this message because you registered on {domain}. If you didn't register, please contact the support team on {domain}."

            # 设置发件人邮箱
            fromEmail = 'noreply@exam.com'
            # 创建EmailMessage实例
            email_message = EmailMessage(email_subject, email_body, fromEmail, [email])
            # 创建FacultyInfo实例，但不立即保存到数据库
            faculty_info = faculty_info_form.save(commit=False)
            # 设置外键user为刚刚保存的faculty用户
            faculty_info.user = faculty

            # 检查是否有上传的图片
            if 'picture' in request.FILES:
                # 设置图片字段为上传的图片
                faculty_info.picture = request.FILES['picture']
            # 保存FacultyInfo数据到数据库
            faculty_info.save()

            # 显示成功消息
            messages.success(request, "Registered Successfully. Check Email for confirmation")
            email_message.send(fail_silently=False)
            return redirect('faculty-login')
        else:
            print(faculty_form.errors, faculty_info_form.errors)
            return render(request, 'faculty/register.html', {'faculty_form': faculty_form, 'faculty_info_form': faculty_info_form})

class LoginView(View):
    # 处理GET请求，返回登录页面
    def get(self, request):
        return render(request, 'faculty/login.html')

    # 处理POST请求，进行用户登录验证
    def post(self, request):
        # 从POST请求中获取用户名和密码
        username = request.POST['username']
        password = request.POST['password']
        # 初始化用户是否在教授组的标志
        has_grp = False

        # 检查用户名和密码是否都已填写
        if username and password:
            # 使用Django内置的认证系统验证用户
            user = auth.authenticate(username=username, password=password)
            # 检查数据库中是否存在该用户名
            exis = User.objects.filter(username=username).exists()

            # 如果用户存在，检查用户是否在"Professor"组中
            if exis:
                user_ch = User.objects.get(username=username)
                has_grp = has_group(user_ch, "Professor")

            # 如果用户验证通过，用户是活跃状态，用户存在，且用户在教授组中
            if user and user.is_active and exis and has_grp:
                # 登录用户
                auth.login(request, user)
                # 显示欢迎消息
                messages.success(request, f"Welcome, {user.username}. You are now logged in.")
                # 重定向到教职员工首页
                return redirect('faculty-index')

            # 如果用户不在教授组但用户存在
            elif not has_grp and exis:
                # 显示错误消息
                messages.error(request, 'You do not have permission to login as faculty. If you think this is a mistake, please contact admin')
                # 返回登录页面
                return render(request, 'faculty/login.html')

            # 其他情况，例如用户名或密码错误
            else:
                # 显示错误消息
                messages.error(request, 'Invalid credentials')
                # 返回登录页面
                return render(request, 'faculty/login.html')

        # 如果用户名或密码未填写
        messages.error(request, 'Please fill all fields')
        # 返回登录页面
        return render(request, 'faculty/login.html')

class LogoutView(View):
    # 定义一个名为LogoutView的类，继承自View类，用于处理用户登出请求
    def post(self, request):
        # 定义post方法，用于处理HTTP POST请求
        auth.logout(request)
        # 调用Django的auth模块的logout方法，执行用户登出操作，参数为当前的request对象
        messages.success(request, 'Logged Out')
        # 使用Django的messages框架，向用户显示一个成功消息，内容为'Logged Out'
        return redirect('faculty-login')
