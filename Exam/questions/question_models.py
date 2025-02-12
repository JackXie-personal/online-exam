from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import User
from django import forms
import random
from course.models import Course  # 新增课程模型导入

class Question_DB(models.Model):
    QUESTION_CHOICES = [
        ('single', '单选题'),
        ('multiple', '多选题'),
        ('fill_blank', '填空题'),
        ('short', '简答题'),
    ]
    
    course = models.ForeignKey(  # 新增课程关联
        Course,
        on_delete=models.CASCADE,
        verbose_name="所属课程",
        null=True,
        blank=False
    )
    professor = models.ForeignKey(
        User, 
        limit_choices_to={'groups__name': "Professor"},
        on_delete=models.SET_NULL,
        null=True
    )
    qno = models.AutoField(primary_key=True)
    question = models.TextField("题干", max_length=1000)
    question_type = models.CharField(
        "题型",
        max_length=20, 
        choices=QUESTION_CHOICES, 
        default='single'
    )
    answer = models.JSONField("参考答案")

    class Meta:
        verbose_name = "题库"
        verbose_name_plural = "题库管理"
        ordering = ['course', 'qno']
        
    def __str__(self):
        return f"[{self.course.code if self.course else '未分类'}] {self.question[:50]}..."

    @classmethod
    def generate_random_paper(cls, course_id, question_types, counts):
        """升级版智能组卷方法"""
        course_filter = cls.objects.filter(course__id=course_id)
        
        selected = []
        # 按题型筛选
        for qtype, qcount in question_types.items():
            candidates = list(course_filter.filter(question_type=qtype))
            selected += random.sample(candidates, min(qcount, len(candidates)))
        
        # 补足余量
        remaining = counts - len(selected)
        if remaining > 0:
            candidates = list(course_filter.exclude(id__in=[q.id for q in selected]))
            selected += random.sample(candidates, remaining)
        
        return selected[:counts]

class QForm(ModelForm):
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('professor', None)
        super().__init__(*args, **kwargs)
        if user:  # 限制课程选择范围
            self.fields['course'].queryset = Course.objects.filter(professor=user)

    class Meta:
        model = Question_DB
        fields = ['course', 'question_type', 'question', 'answer']
        exclude = ['qno', 'professor']
        widgets = {
            'question': forms.Textarea(attrs={
                'class': 'form-control', 
                'rows': 4,
                'placeholder': '输入完整的题目描述...'
            }),
            'question_type': forms.Select(attrs={
                'class': 'form-control', 
                '@change': 'showOptions'
            }),
            'answer': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'JSON格式的参考答案'
            })
        }