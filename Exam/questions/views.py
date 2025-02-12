from django.views.generic import ListView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.decorators import method_decorator
from django.views.decorators.http import require_http_methods
from course.models import Course
from .models import Question_DB, Question_Paper, Exam_Model

@method_decorator([login_required, professor_required], name='dispatch')
class QBankView(LoginRequiredMixin, ListView):
    """教师题库总览"""
    template_name = 'questions/qbank_home.html'
    context_object_name = 'courses'

    def get_queryset(self):
        # 获取教师负责的课程包含题目统计
        return Course.objects.filter(
            professor=self.request.user
        ).prefetch_related(
            Prefetch('questions', queryset=Question_DB.objects.all())
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_questions'] = sum(
            c.questions.count() for c in context['courses']
        )
        return context

class CourseQBankView(QBankView):
    """指定课程的题库管理"""
    template_name = 'questions/course_qbank.html'

    def get_queryset(self):
        course = get_object_or_404(
            Course, 
            id=self.kwargs['course_id'],
            professor=self.request.user
        )
        return Question_DB.objects.filter(course=course)

@method_decorator([login_required, professor_required], name='dispatch')
class PaperCreateView(CreateView):
    """试卷创建视图"""
    model = Question_Paper
    form_class = QuestionPaperForm  # 需添加对应的Form
    template_name = 'questions/paper_create.html'

    def form_valid(self, form):
        form.instance.professor = self.request.user
        form.instance.course = get_object_or_404(
            Course,
            id=self.kwargs['course_id'],
            professor=self.request.user
        )
        return super().form_valid(form)