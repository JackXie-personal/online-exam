
from django.shortcuts import render, redirect
from django.views.generic import ListView
from .models import Course, CourseRegistration, Student, Grade

def course_registration(request):
    # 检查请求的方法是否为POST
    if request.method == 'POST':
        # 如果是POST请求，调用内部函数处理请求
        return _extracted_from_course_registration_(request)
    # 获取所有课程对象
    courses = Course.objects.all()
    # 获取所有已支付接受费和学费的学生对象
    students = Student.objects.filter(has_paid_acceptance_fee=True, has_paid_school_fees=True)
    # 获取所有会话（学期）对象
    sessions = Session.objects.all()
    # 渲染课程注册页面，并传递课程、学生和会话数据
    return render(request, 'course_registration.html', {'courses': courses, 'students': students, 'sessions': sessions})


# TODO Rename this here and in `course_registration`
def _extracted_from_course_registration_(request):
    # 从请求的POST数据中获取学生ID
    student_id = request.POST.get('student_id')
    # 从请求的POST数据中获取课程ID
    course_id = request.POST.get('course_id')
    # 从请求的POST数据中获取学期ID
    session_id = request.POST.get('session_id')
    # 根据学生ID从数据库中获取学生对象
    student = Student.objects.get(id=student_id)
    # 根据课程ID从数据库中获取课程对象
    course = Course.objects.get(id=course_id)
    # 根据学期ID从数据库中获取学期对象
    session = Session.objects.get(id=session_id)

    # 检查学生是否已支付接受费和学费
    if not student.has_paid_acceptance_fee or not student.has_paid_school_fees:
        # 如果学生未支付接受费或学费，则返回错误页面
        return render(request, 'error.html', {'message': 'Student not eligible for course registration.'})
    # 检查学生的学分限制是否足够
    if student.credit_units_limit < course.credit_units:
        # 如果学生的学分限制不足，则返回错误页面
        return render(request, 'error.html', {'message': 'Credit units limit exceeded.'})
    # 创建一个新的课程注册记录
    CourseRegistration.objects.create(student=student, course=course, session=session)
    # 重定向到课程列表页面
    return redirect('course_list')

