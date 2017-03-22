# -*- coding:utf-8 -*-
from django.conf.urls import url

urlpatterns = [
    url(r'^cmbc-task', 'task.views.cmbc_task', name="cmbc_task"),
    url(r'^cebbank-task', 'task.views.cebbank_task', name="cebbank_task"),

    url(r'^cmbc-source1-task', 'task.views.cmbc_source1_task', name="cmbc_source1_task"),
    url(r'^cmbc-source2-task', 'task.views.cmbc_source2_task', name="cmbc_source2_task"),

    url(r'^districts_info', 'task.views.get_districts_info', name="get_districts_info"),
    url('^ajax_val/', 'task.views.ajax_val', name='ajax_val')
]
