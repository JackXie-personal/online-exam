from django.urls import path
from .views import (
    CourseListView,
    CourseDetailView,
    CourseRegistrationView,
    RegistrationCheckView,
    PaymentStatusUpdateView,
    CreditAllocationView,
    SessionActiveView,
    # 新增考试关联视图
    CourseExamListView,
    AssignExamToCourseView
)

urlpatterns = [
    # RESTful 课程管理API
    path('', CourseListView.as_view(), name='course-list'),          # 获取课程清单/创建课程
    path('<int:pk>/', CourseDetailView.as_view(), name='course-detail'), # 课程详情操作
    
    # 注册管理路由
    path('registrations/', RegistrationCheckView.as_view(), name='registration-check'), 
    path('register/', CourseRegistrationView.as_view(), name='course-register'),
    
    # 缴费关联接口
    path('payment/status/', PaymentStatusUpdateView.as_view(), name='payment-status'),
    
    # 学分管理接口
    path('credits/allocation/', CreditAllocationView.as_view(), name='credit-allocation'),
    
    # 学期管理接口
    path('sessions/active/', SessionActiveView.as_view(), name='session-active'),
    
    # 新增考试关联路由
    path('<int:course_id>/exams/', CourseExamListView.as_view(), name='course-exam-list'), 
    path('assign-exam/', AssignExamToCourseView.as_view(), name='assign-exam')
]