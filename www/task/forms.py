# -*- coding:utf-8 -*-
from django import forms
from captcha.fields import CaptchaField

from task.models import *

class CMBCTaskForm(forms.ModelForm):
    captcha = CaptchaField()

    def __init__(self, *args, **kwargs):
        super(CMBCTaskForm, self).__init__(*args, **kwargs)

        self.fields['user'].required = True
        self.fields['phone_number'].required = True
        self.fields['province'].required = False
        self.fields['city'].required = False
        self.fields['district'].required = False
        self.fields['identity'].required = False
        self.fields['address'].required = False
        self.fields['company_name'].required = False
        self.fields['education'].required = False
        self.fields['title'].required = False

    class Meta:
        model = CMBCTaskModel
        exclude = ['created', 'ip']


class CEBBANKTaskForm(forms.ModelForm):
    captcha = CaptchaField()

    def __init__(self, *args, **kwargs):
        super(CEBBANKTaskForm, self).__init__(*args, **kwargs)

        self.fields['user'].required = True
        self.fields['phone_number'].required = True

    class Meta:
        model = CEBBANKTaskModel
        exclude = ['created', 'ip']


class CMBCSource1TaskForm(forms.ModelForm):
    captcha = CaptchaField()

    def __init__(self, *args, **kwargs):
        super(CMBCSource1TaskForm, self).__init__(*args, **kwargs)

        self.fields['user'].required = True
        self.fields['phone_number'].required = True

    class Meta:
        model = CMBCSource1TaskModel
        exclude = ['created', 'ip']


class CMBCSource2TaskForm(forms.ModelForm):
    captcha = CaptchaField()

    def __init__(self, *args, **kwargs):
        super(CMBCSource2TaskForm, self).__init__(*args, **kwargs)

        self.fields['user'].required = True
        self.fields['phone_number'].required = True

    class Meta:
        model = CMBCSource2TaskModel
        exclude = ['created', 'ip']


class TaskRegisterUserInfoForm(forms.ModelForm):
    captcha = CaptchaField()

    def __init__(self, *args, **kwargs):
        super(TaskRegisterUserInfoForm, self).__init__(*args, **kwargs)

        self.fields['real_name'].required = False
        self.fields['user_name'].required = False
        self.fields['phone_number'].required = False
        self.fields['province'].required = False
        self.fields['city'].required = False
        self.fields['district'].required = False
        self.fields['identity'].required = False

    class Meta:
        model = TaskRegisterUserInfoModel
        exclude = ['created', 'ip', 'task_type']