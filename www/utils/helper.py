# -*- coding:utf-8 -*-
import os
import csv
import tempfile
from operator import itemgetter

from django.http import StreamingHttpResponse


class DataDumper(object):

    def __init__(self, data, field_names=None, field_title=None, sorted_by=None, reverse=True, save_name="dump.csv"):
        """
        :param data: 需要被dump的数据, data为列表,列表中的元素为字段名相同的字典.
        :param field_names: 所有的字段名
        :param sorted_by: 按指定字段排序
        :param reverse: 是否逆序
        :param save_name: 保存的文件名
        """
        self.data = data
        if len(field_names) != len(field_title):
            raise ValueError("Len of field_names must equals with len of field_title")
        else:
            self.field_title = field_title
            self.field_names = field_names

        if save_name:
            self.save_file = os.path.join(tempfile.gettempdir(), save_name)
        else:
            self.save_file = os.path.join(tempfile.gettempdir(), 'dump.csv')

        if sorted_by and sorted_by in self.field_names:
            self.data = sorted(data, key=itemgetter(sorted_by), reverse=reverse)
        else:
            self.data = data

    def to_csv(self):
        with open(self.save_file, 'w') as csvfile:
            writer = csv.writer(csvfile)

            row = []
            for key in self.field_title:
                row.append(self._to_gb2312(key))
            writer.writerow(row)

            for item in self.data:
                row = []
                for key in self.field_names:
                    value = self._to_gb2312(item[key])
                    row.append(value)

                writer.writerow(row)

        return self.save_file

    @staticmethod
    def _to_gb2312(field):
        if isinstance(field, str):
            value = field.decode('utf-8').encode('gb2312')
        elif isinstance(field, unicode):
            value = field.encode('gb2312')
        else:
            value = field
        return value


def transfer_file(file_path):
    def file_iterator(file_path, chunk_size=512):
        with open(file_path) as f:
            while True:
                c = f.read(chunk_size)
                if c:
                    yield c
                else:
                    break

    response = StreamingHttpResponse(file_iterator(file_path))
    response['Content-Type'] = 'application/octet-stream'
    response['Set-Cookie'] = "fileDownload=true; path=/"
    basename = os.path.basename(file_path)
    response['Content-Disposition'] = 'attachment;filename="{0}"'.format(basename)

    return response


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip