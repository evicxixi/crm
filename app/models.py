from django.db import models
from rbac.models import UserInfo as RbacUserInfo
# Create your models here.


class Department(models.Model):
    """
    科室表
    """
    title = models.CharField(verbose_name='科室名称', max_length=16)
    intro = models.CharField(verbose_name='科室简介', max_length=64, null=True)

    def __str__(self):
        return self.title


class UserInfo(RbacUserInfo):
    # class UserInfo(models.Model):
    """
    员工表
    """
    name = models.CharField(verbose_name='真实姓名', max_length=16)
    phone = models.CharField(verbose_name='手机号', max_length=32)
    # username = models.CharField(verbose_name='用户名', max_length=32)
    # password = models.CharField(verbose_name='密码', max_length=64)

    gender_choices = (
        (1, '男'),
        (2, '女'),
    )
    gender = models.IntegerField(
        verbose_name='性别', choices=gender_choices, default=1)

    depart = models.ForeignKey(verbose_name='部门', to="Department")

    def __str__(self):
        return self.name


class Doctor(models.Model):
    # class UserInfo(models.Model):
    """
    医生表
    """
    name = models.CharField(verbose_name='医生姓名', max_length=16)

    level_choices = (
        (1, '主任医师'),
        (2, '副主任医师'),
        (3, '教授'),
    )
    level = models.IntegerField(
        verbose_name='职称', choices=level_choices, default=1)
    # phone = models.CharField(verbose_name='手机号', max_length=32)
    # username = models.CharField(verbose_name='用户名', max_length=32)
    # password = models.CharField(verbose_name='密码', max_length=64)

    gender_choices = (
        (1, '男'),
        (2, '女'),
    )
    gender = models.IntegerField(
        verbose_name='性别', choices=gender_choices, default=1)

    depart = models.ForeignKey(verbose_name='科室', to="Department")
    intro = models.CharField(
        verbose_name='医生简介', max_length=64, null=True, blank=True)
    price = models.IntegerField(verbose_name='挂号费', default=1)

    def __str__(self):
        return self.name


class Customer(models.Model):
    # class UserInfo(models.Model):
    """
    患者表
    """
    name = models.CharField(verbose_name='患者姓名', max_length=16)
    phone = models.CharField(verbose_name='手机号', max_length=32)

    gender_choices = (
        (1, '男'),
        (2, '女'),
    )
    gender = models.IntegerField(
        verbose_name='性别', choices=gender_choices, default=1)

    disease_choices = (
        (1, '痤疮'),
        (2, '湿疹'),
        (3, '白癜风'),
        (4, '银屑病'),
        (5, '医学美容'),

    )
    disease = models.IntegerField(
        verbose_name='病种', choices=disease_choices, null=True, blank=True)

    count = models.IntegerField(verbose_name='就诊次数', default=0)
    intro = models.CharField(
        verbose_name='病情描述', max_length=64, null=True, blank=True)

    def __str__(self):
        return self.name

# class Course(models.Model):
#     """
#     课程表
#     如：
#         Linux基础
#         Linux架构师
#         Python自动化
#         Python全栈
#     """
#     name = models.CharField(verbose_name='课程名称', max_length=32)

#     def __str__(self):
#         return self.name


# class School(models.Model):
#     """
#     校区表
#     如：
#         北京昌平校区
#         上海浦东校区
#         深圳南山校区
#     """
#     title = models.CharField(verbose_name='校区名称', max_length=32)

#     def __str__(self):
#         return self.title


# class ClassList(models.Model):
#     """
#     班级表
#     如：
#         Python全栈  面授班  5期  10000  2017-11-11  2018-5-11
#     """
#     school = models.ForeignKey(verbose_name='校区', to='School')
#     course = models.ForeignKey(verbose_name='课程名称', to='Course')
#     semester = models.IntegerField(verbose_name="班级(期)")  # 11
#     price = models.IntegerField(verbose_name="学费")
#     start_date = models.DateField(verbose_name="开班日期")
#     graduate_date = models.DateField(
#         verbose_name="结业日期", null=True, blank=True)
#     # tutor = models.ForeignKey(verbose_name='班主任', to='UserInfo', related_name='classes',limit_choices_to={'depart__title':'教质部'})
#     # teachers = models.ManyToManyField(verbose_name='任课老师', to='UserInfo', related_name='teach_classes',limit_choices_to={'depart_id__in':[6,7]})
#     memo = models.CharField(
#         verbose_name='说明', max_length=256, blank=True, null=True)

#     def __str__(self):
#         return "{0}({1}期)".format(self.course.name, self.semester)
