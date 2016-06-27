# -*- coding:utf-8 -*-
from django.contrib import admin

from .models import CMBCTaskModel
from utils.helper import DataDumper, transfer_file


class CMBCTaskAdmin(admin.ModelAdmin):
    def has_delete_permission(self, request, obj=None):
        return False

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


admin.site.register(CMBCTaskModel, CMBCTaskAdmin)