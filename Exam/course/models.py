from django.db import models
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError

User = get_user_model()

class Session(models.Model):
    """学期/学年管理模型"""
    name = models.CharField('学期名称', max_length=250, unique=True)
    start_date = models.DateField('开始日期')
    end_date = models.DateField('结束日期')
    is_active = models.BooleanField('是否激活', default=True)

    class Meta:
        verbose_name = '学期管理'
        verbose_name_plural = verbose_name
        ordering = ['-start_date']

    def __str__(self):
        return f"{self.name} ({self.start_date.year})"

class Grade(models.Model):
    """成绩等级体系模型"""
    GRADE_CHOICES = [
        ('A', '优秀'),
        ('B', '良好'),
        ('C', '合格'),
        ('D', '不合格'),
    ]
    letter_grade = models.CharField('等级', max_length=2, choices=GRADE_CHOICES, unique=True)
    min_score = models.FloatField('最低分数')
    max_score = models.FloatField('最高分数')
    grade_points = models.FloatField('绩点')
    
    class Meta:
        verbose_name = '成绩等级'
        verbose_name_plural = verbose_name
        ordering = ['min_score']

    def clean(self):
        if self.min_score >= self.max_score:
            raise ValidationError('最低分数必须小于最高分数')
            
    def __str__(self):
        return f"{self.letter_grade} ({self.min_score}-{self.max_score})"

class StudentProfile(models.Model):
    """学生扩展档案"""
    STUDENT_TYPES = [
        ('freshman', '新生'),
        ('transfer', '转学生'),
        ('returning', '返校生'),
    ]
    
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='student_profile')
    admission_status = models.CharField('录取状态', max_length=20, default='pending')
    has_paid_acceptance = models.BooleanField('已付入学费', default=False)
    has_paid_tuition = models.BooleanField('已付学费', default=False)
    student_type = models.CharField('学生类型', max_length=20, choices=STUDENT_TYPES)
    max_credits = models.PositiveIntegerField('最大学分额度', default=24)
    current_credits = models.PositiveIntegerField('当前学分', default=0)
    
    # 审计字段
    created_at = models.DateTimeField('创建时间', auto_now_add=True)
    updated_at = models.DateTimeField('最后更新', auto_now=True)

    class Meta:
        verbose_name = '学生档案'
        verbose_name_plural = verbose_name

    def can_register_course(self):
        """判断是否具备选课资格"""
        return all([
            self.admission_status == 'accepted',
            self.has_paid_acceptance,
            self.has_paid_tuition
        ])

class Course(models.Model):
    """课程核心模型"""
    COURSE_LEVELS = [
        ('intro', '基础课'),
        ('intermediate', '中级课'),
        ('advanced', '高级课'),
    ]
    
    code = models.CharField('课程代码', max_length=10, unique=True)
    name = models.CharField('课程名称', max_length=250)
    description = models.TextField('课程描述')
    credit_units = models.PositiveIntegerField('学分')
    level = models.CharField('难度等级', max_length=20, choices=COURSE_LEVELS)
    professors = models.ManyToManyField(
        User,
        limit_choices_to={'groups__name': 'Professor'},
        related_name='taught_courses',
        verbose_name='授课'
    )