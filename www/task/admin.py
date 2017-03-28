# -*- coding:utf-8 -*-
from django.contrib import admin
from daterange_filter.filter import DateRangeFilter
from django.utils.html import format_html
from django.core.urlresolvers import reverse

from task.models import *
from utils.helper import DataDumper, transfer_file
from django.conf import settings

admin.site.site_header = settings.ADMIN_SITE_HEADER

class CMBCTaskAdmin(admin.ModelAdmin):

    def download_selected_tasks(self, request, queryset):
        """下载选中的任务并导出到CSV中"""
        data = []
        for item in queryset:
            data.append(item.to_dict())
        fields_name = ['user', 'province', 'city', 'district', 'identity', 'phone_number', 'address',
                       'company_name', 'education', 'title', 'ip', 'created']
        fields_title = ['姓名', '单位所在省/直辖市', '单位所在市/地区', '单位所在区', '身份证号', '手机号', '单位详细地址',
                        '单位名称', '学历', '职务', '来源IP', '添加时间']
        dumper = DataDumper(data, field_names=fields_name, field_title=fields_title, sorted_by='created', reverse=True)
        file_path = dumper.to_csv()

        return transfer_file(file_path)

    download_selected_tasks.short_description = "下载所选的 招行信用卡注册任务"

    list_display = ['user', 'province', 'city', 'district', 'identity', 'phone_number', 'address',
                    'company_name', 'education', 'title', 'ip', 'created']
    actions = [download_selected_tasks, ]
    list_filter = [('created', DateRangeFilter)]

class CEBBANKAdmin(admin.ModelAdmin):

    def download_selected_tasks(self, request, queryset):
        """下载选中的任务并导出到CSV中"""
        data = []
        for item in queryset:
            data.append(item.to_dict())
        fields_name = ['user', 'phone_number', 'ip', 'created']
        fields_title = ['姓名', '手机号', '来源IP', '添加时间']
        dumper = DataDumper(data, field_names=fields_name, field_title=fields_title, sorted_by='created', reverse=True)
        file_path = dumper.to_csv()

        return transfer_file(file_path)

    download_selected_tasks.short_description = "下载所选的 光大信用卡注册任务"

    list_display = ['user', 'phone_number', 'ip', 'created']
    actions = [download_selected_tasks, ]
    list_filter = [('created', DateRangeFilter)]


class CMBCSource1Admin(admin.ModelAdmin):

    def download_selected_tasks(self, request, queryset):
        """下载选中的任务并导出到CSV中"""
        data = []
        for item in queryset:
            data.append(item.to_dict())
        fields_name = ['user', 'phone_number', 'ip', 'created']
        fields_title = ['姓名', '手机号', '来源IP', '添加时间']
        dumper = DataDumper(data, field_names=fields_name, field_title=fields_title, sorted_by='created', reverse=True)
        file_path = dumper.to_csv()

        return transfer_file(file_path)

    download_selected_tasks.short_description = "下载所选的  招商银行信用卡注册任务-来源1"

    list_display = ['user', 'phone_number', 'ip', 'created']
    actions = [download_selected_tasks, ]
    list_filter = [('created', DateRangeFilter)]


class CMBCSource2Admin(admin.ModelAdmin):

    def download_selected_tasks(self, request, queryset):
        """下载选中的任务并导出到CSV中"""
        data = []
        for item in queryset:
            data.append(item.to_dict())
        fields_name = ['user', 'phone_number', 'ip', 'created']
        fields_title = ['姓名', '手机号', '来源IP', '添加时间']
        dumper = DataDumper(data, field_names=fields_name, field_title=fields_title, sorted_by='created', reverse=True)
        file_path = dumper.to_csv()

        return transfer_file(file_path)

    download_selected_tasks.short_description = "下载所选的 招商信用卡注册任务-来源2"

    list_display = ['user', 'phone_number', 'ip', 'created']
    actions = [download_selected_tasks, ]
    list_filter = [('created', DateRangeFilter)]


class CustomTaskAdmin(admin.ModelAdmin):
    """
    自定义任务的 admin
    """
    def task_url_column(self, obj):
        task_url = format_html('<a href="{}" target="_blank" style="width:60px;text-decoration: none;">任务页面</a>',
                               '%s?id=%s' % (reverse('custom_task'), obj.id))
        return task_url

    task_url_column.short_description = '任务链接'

    list_filter = ['task_name',]
    list_display = ['id', 'task_name', 'title', 'redirect_url', 'background_css', 'task_url_column']


class TaskRegisterUserInfoAdmin(admin.ModelAdmin):
    def download_selected_tasks(self, request, queryset):
        """下载选中的任务并导出到CSV中"""
        data = []
        for item in queryset:
            data.append(item.to_dict())
        fields_name = ['user', 'province', 'city', 'district', 'identity', 'phone_number', 'ip', 'created']
        fields_title = ['姓名', '单位所在省/直辖市', '单位所在市/地区', '单位所在区', '身份证号', '手机号', '单位详细地址',
                        '单位名称', '学历', '职务', '来源IP', '添加时间']
        dumper = DataDumper(data, field_names=fields_name, field_title=fields_title, sorted_by='created', reverse=True)
        file_path = dumper.to_csv()

        return transfer_file(file_path)

    download_selected_tasks.short_description = "下载所选的 信用卡注册任务"

    list_filter = ['task_type',]
    list_display = ['id', 'real_name', 'user_name', 'province', 'city', 'district', 'identity', 'phone_number', 'task_type']


admin.site.register(CMBCTaskModel, CMBCTaskAdmin)
admin.site.register(CEBBANKTaskModel, CEBBANKAdmin)
admin.site.register(CMBCSource1TaskModel, CMBCSource1Admin)
admin.site.register(CMBCSource2TaskModel, CMBCSource2Admin)
admin.site.register(CustomTaskModel, CustomTaskAdmin)
admin.site.register(TaskRegisterUserInfoModel, TaskRegisterUserInfoAdmin)
