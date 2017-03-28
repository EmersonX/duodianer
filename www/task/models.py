# encoding:utf-8
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from multiselectfield import MultiSelectField

from www.settings.const import CMBC_TASK_EDUCATION, CMBC_TASK_TITLE

# 历史原因，重复代码块
# 开始 ------------>

class CMBCTaskModel(models.Model):
    user = models.CharField(verbose_name="姓名", max_length=64)
    province = models.CharField(verbose_name="单位所在省/直辖市", max_length=64)
    city = models.CharField(verbose_name="单位所在市/地区", max_length=64)
    district = models.CharField(verbose_name="单位所在区", max_length=64)
    identity = models.CharField(verbose_name="身份证号", max_length=20)
    phone_number = models.CharField(verbose_name="手机号", max_length=16)
    address = models.CharField(verbose_name="单位详细地址", max_length=256)
    company_name =models.CharField(verbose_name="单位名称", max_length=256)
    education = models.CharField(verbose_name="学历", default=None, choices=CMBC_TASK_EDUCATION.iteritems(), max_length=64, blank=True)
    title = models.CharField(verbose_name="职务", default=None, choices=CMBC_TASK_TITLE.iteritems(), max_length=64, blank=True)

    ip = models.CharField(verbose_name="来源IP", editable=False, max_length=32, blank=True)
    created = models.DateTimeField(verbose_name="添加时间", editable=False)

    def __unicode__(self):
        return self.user

    def save(self, *args, **kwargs):
        if not self.created:
            self.created = timezone.now()
        self.updated = timezone.now()
        return super(CMBCTaskModel, self).save(*args, **kwargs)

    def to_dict(self):
        title = CMBC_TASK_TITLE[self.title] if self.title else self.title
        education = CMBC_TASK_EDUCATION[self.education] if self.company_name else self.company_name

        return dict(user=self.user, province=self.province, city=self.city, district=self.district, identity=self.identity,
                    phone_number=self.phone_number, address=self.address, company_name=self.company_name,
                    education=education, title=title, ip=self.ip, created=self.created)

    class Meta:
        db_table = 'task_cmbc_task'
        verbose_name = '招行信用卡注册任务'
        verbose_name_plural = '招行信用卡注册任务'
        ordering = ['-created']


class CEBBANKTaskModel(models.Model):
    user = models.CharField(verbose_name="姓名", max_length=64)
    phone_number = models.CharField(verbose_name="手机号", max_length=16)

    ip = models.CharField(verbose_name="来源IP", editable=False, max_length=32, blank=True)
    created = models.DateTimeField(verbose_name="添加时间", editable=False)

    def __unicode__(self):
        return self.user

    def save(self, *args, **kwargs):
        if not self.created:
            self.created = timezone.now()
        self.updated = timezone.now()
        return super(CEBBANKTaskModel, self).save(*args, **kwargs)

    def to_dict(self):

        return dict(user=self.user, phone_number=self.phone_number, ip=self.ip, created=self.created)

    class Meta:
        db_table = 'task_cebbank_task'
        verbose_name = '光大信用卡注册任务'
        verbose_name_plural = '光大信用卡注册任务'
        ordering = ['-created']


class CMBCSource1TaskModel(models.Model):
    user = models.CharField(verbose_name="姓名", max_length=64)
    phone_number = models.CharField(verbose_name="手机号", max_length=16)
    ip = models.CharField(verbose_name="来源IP", editable=False, max_length=32, blank=True)
    created = models.DateTimeField(verbose_name="添加时间", editable=False)

    def __unicode__(self):
        return self.user

    def save(self, *args, **kwargs):
        if not self.created:
            self.created = timezone.now()
        self.updated = timezone.now()
        return super(CMBCSource1TaskModel, self).save(*args, **kwargs)

    def to_dict(self):
        return dict(user=self.user, phone_number=self.phone_number, ip=self.ip, created=self.created)

    class Meta:
        db_table = 'task_cmbcsource1_task'
        verbose_name = '招商银行信用卡注册任务-来源1'
        verbose_name_plural = '招商银行信用卡注册任务-来源1'
        ordering = ['-created']


class CMBCSource2TaskModel(models.Model):
    user = models.CharField(verbose_name="姓名", max_length=64)
    phone_number = models.CharField(verbose_name="手机号", max_length=16)
    ip = models.CharField(verbose_name="来源IP", editable=False, max_length=32, blank=True)
    created = models.DateTimeField(verbose_name="添加时间", editable=False)

    def __unicode__(self):
        return self.user

    def save(self, *args, **kwargs):
        if not self.created:
            self.created = timezone.now()
        self.updated = timezone.now()
        return super(CMBCSource2TaskModel, self).save(*args, **kwargs)

    def to_dict(self):
        return dict(user=self.user, phone_number=self.phone_number, ip=self.ip, created=self.created)

    class Meta:
        db_table = 'task_cmbcsource2_task'
        verbose_name = '招商银行信用卡注册任务-来源2'
        verbose_name_plural = '招商银行信用卡注册任务-来源2'
        ordering = ['-created']


class CommonDistrictModel(models.Model):
    id = models.AutoField(verbose_name='ID', primary_key=True)
    name = models.CharField(verbose_name="名称", max_length=255)
    level = models.SmallIntegerField(verbose_name="分级", db_index=True)
    upid = models.IntegerField(verbose_name="上级ID", db_index=True)

    def __unicode__(self):
        return self.name

    @classmethod
    def get_districts_by_upid(self, upid):
        data = self.objects.filter(upid=upid).values('name', 'id').order_by('id')
        results = [item for item in data]
        return results

    class Meta:
        db_table = 'task_common_district'

# <-------------结束
# 历史原因，重复代码块

FORM_CHOICES = (('real_name', '姓名'),
                ('phone', '手机号'),
                ('user_name', '昵称'),
                ('cardid', '身份证号'),
                ('address', '地址'),)


class CustomTaskModel(models.Model):
    id = models.AutoField(verbose_name='ID', primary_key=True)
    task_name = models.CharField(verbose_name='任务名称', max_length=255, null=False, unique=True)
    title = models.CharField(verbose_name='任务标题', max_length=255, null=False)
    forms_setting = MultiSelectField(verbose_name='表单设定', choices=FORM_CHOICES, min_choices=1)
    redirect_url = models.CharField(verbose_name='跳转链接', max_length=255, null=False)
    background_css = models.CharField(verbose_name='选择样式', max_length=20, null=False,
                                      choices=[('red', '红色底'), ])

    def __unicode__(self):
        return unicode('%s' % self.task_name)

    class Meta:
        db_table = 'task_custom_task'
        verbose_name = '自定义任务'
        verbose_name_plural = '自定义任务'
        ordering = ['id']


class TaskRegisterUserInfoModel(models.Model):
    id = models.AutoField(verbose_name='ID', primary_key=True)
    task_type = models.ForeignKey(CustomTaskModel, verbose_name='自定义任务名称', on_delete=models.CASCADE)
    real_name = models.CharField(verbose_name="姓名", max_length=64, blank=True)
    user_name = models.CharField(verbose_name=" 昵称", max_length=64, blank=True)
    province = models.CharField(verbose_name="所在省/直辖市", max_length=64, blank=True)
    city = models.CharField(verbose_name="所在市/地区", max_length=64, blank=True)
    district = models.CharField(verbose_name="所在区", max_length=64, blank=True)
    identity = models.CharField(verbose_name="身份证号", max_length=20, blank=True)
    phone_number = models.CharField(verbose_name="手机号", max_length=16, blank=True)

    ip = models.CharField(verbose_name="来源IP", editable=False, max_length=32, blank=True)
    created = models.DateTimeField(verbose_name="添加时间", editable=False)

    def __unicode__(self):
        return unicode(self.id)

    def save(self, *args, **kwargs):
        if not self.created:
            self.created = timezone.now()
        self.updated = timezone.now()
        return super(TaskRegisterUserInfoModel, self).save(*args, **kwargs)

    def to_dict(self):
        return dict(real_name=self.real_name, user_name=self.user_name, province=self.province,
                    city=self.city, district=self.district, identity=self.identity,
                    phone_number=self.phone_number, ip=self.ip, created=self.created)

    class Meta:
        db_table = 'task_task_register_user_info'
        verbose_name = '自定义任务注册用户'
        verbose_name_plural = '自动义任务注册用户'
        ordering = ['-created']
