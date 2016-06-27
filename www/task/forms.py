# -*- coding:utf-8 -*-
from django import forms
from captcha.fields import CaptchaField

from .models import CMBCTaskModel

class CMBCTaskForm(forms.ModelForm):
    ip = forms.CharField(widget=forms.HiddenInput())
    captcha = CaptchaField()

    def __init__(self, *args, **kwargs):
        super(CMBCTaskForm, self).__init__(*args, **kwargs)

        self.fields['user'].required = True
        self.fields['province'].required = True
        self.fields['city'].required = True
        self.fields['district'].required = True
        self.fields['identity'].required = True
        self.fields['phone_number'].required = True
        self.fields['address'].required = True
        self.fields['company_name'].required = True
        self.fields['education'].required = True
        self.fields['title'].required = True
        self.fields['ip'].required = False

    class Meta:
        model = CMBCTaskModel
        exclude = ['created', 'ip']
