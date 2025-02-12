from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import User
from datetime import datetime
from .questionpaper_models import Question_Paper
from django import forms
from course.models import Course  # 新增导入

class Exam_Model(models.Model):
    professor = models.ForeignKey(
        User, 
        limit_choices_to={'groups__name': "Professor"}, 
        on_delete=models.CASCADE
    )
    course = models.ForeignKey(  # 新增课程关联字段
        Course,
        on_delete=models.CASCADE,
        verbose_name="关联课程",
        null=True
    )
    name = models.CharField("考试名称", max_length=50)
    total_marks = models.IntegerField("总分值")
    question_paper = models.ForeignKey(
        Question_Paper,
        on_delete=models.CASCADE,
        related_name='exams',
        verbose_name="试卷"
    )
    start_time = models.DateTimeField("开始时间", default=datetime.now)
    end_time = models.DateTimeField("结束时间", default=datetime.now)

    def __str__(self):
        return f"{self.course.name} - {self.name}"

class ExamForm(ModelForm):
    def __init__(self, professor, *args, **kwargs):
        super(ExamForm, self).__init__(*args, **kwargs)
        # 仅显示当前教师的课程试卷
        self.fields['question_paper'].queryset = Question_Paper.objects.filter(
            professor=professor
        )
        # 课程选择下拉框
        self.fields['course'] = forms.ModelChoiceField(
            queryset=Course.objects.filter(professor=professor),
            label="所属课程",
            widget=forms.Select(attrs={'class': 'form-control'})
        )

    class Meta:
        model = Exam_Model
        fields = '__all__'
        exclude = ['professor']
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'total_marks' : forms.NumberInput(attrs={'class':'form-control'}),
            'start_time': forms.DateTimeInput(attrs={'class':'form-control', 'type':'datetime-local'}),
            'end_time': forms.DateTimeInput(attrs={'class':'form-control', 'type':'datetime-local'})
        }