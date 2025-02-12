from django.urls import path
from . import views

urlpatterns = [
    # 题库管理路由
    path('qbank/', views.QBankView.as_view(), name='qbank_home'),
    path('qbank/<int:course_id>/', views.CourseQBankView.as_view(), name='course_qbank'),
    
    # 试卷管理路由
    path('papers/', views.PaperListView.as_view(), name='paper_list'),
    path('papers/create/', views.PaperCreateView.as_view(), name='paper_create'),
    
    # 考试管理路由
    path('exams/', views.ExamListView.as_view(), name='exam_list'),
    
    # API路由
    path('api/questions/generate/', views.GeneratePaperAPI.as_view(), name='generate_paper'),
]