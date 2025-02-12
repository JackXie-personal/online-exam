from django.apps import AppConfig


class CourseConfig(AppConfig):
    # 设置默认的自动字段类型为 BigAutoField，这是一个64位的大整型自增字段，适用于需要存储大量数据的场景
    default_auto_field = 'django.db.models.BigAutoField'
    # 设置应用的名称为 'course'，这个名称将在Django项目的设置文件中被引用，用于标识这个应用
    name = 'course'
