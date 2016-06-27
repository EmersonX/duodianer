# -*- coding:utf-8 -*-
from django import forms
from captcha.fields import CaptchaField

from .models import CMBCTaskModel

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
