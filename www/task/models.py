# encoding:utf-8
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

from www.settings.const import CMBC_TASK_EDUCATION, CMBC_TASK_TITLE

class CMBCTaskModel(models.Model):
    user = models.CharField(verbose_name="姓名", max_length=64)
    province = models.CharField(verbose_name="单位所在省/直辖市", max_length=64)
    city = models.CharField(verbose_name="单位所在市/地区", max_length=64)
    district = models.CharField(verbose_name="单位所在区", max_length=64)
    identity = models.CharField(verbose_name="身份证号", max_length=20)
    phone_number = models.CharField(verbose_name="手机号", max_length=16)
    address = models.CharField(verbose_name="单位详细地址", max_length=256)
    company_name =models.CharField(verbose_name="单位名称", max_length=256)
    education = models.CharField(verbose_name="学历", choices=CMBC_TASK_EDUCATION.iteritems(), max_length=64)
    title = models.CharField(verbose_name="职务", choices=CMBC_TASK_TITLE.iteritems(), max_length=64)

    ip = models.CharField(verbose_name="来源IP", editable=False, max_length=32)
    created = models.DateTimeField(verbose_name="添加时间", editable=False)

    def __unicode__(self):
        return self.user

    def save(self, *args, **kwargs):
        if not self.created:
            self.created = timezone.now()
        self.updated = timezone.now()
        return super(CMBCTaskModel, self).save(*args, **kwargs)

    def to_dict(self):
        return dict(user=self.user, province=self.province, city=self.city, district=self.district, identity=self.identity,
                    phone_number=self.phone_number, address=self.address, company_name=self.company_name,
                    education=self.education, title=self.title, ip=self.ip, created=self.created)

    class Meta:
        db_table = 'task_cmbc_task'
        verbose_name = '招行信用卡注册任务'
        verbose_name_plural = '招行信用卡注册任务'
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