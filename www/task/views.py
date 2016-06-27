# -*- coding:utf-8 -*-
import json

from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from captcha.models import CaptchaStore

from .forms import CMBCTaskForm
from .models import CommonDistrictModel
from utils.helper import get_client_ip
from www.settings.const import CMBC_TASK_REDIRECT_URL

def cmbc_task(request):
    if request.method == "POST":
        form = CMBCTaskForm(request.POST)
        if form.is_valid():
            ip = get_client_ip(request)
            form.instance.ip = ip
            form.save()
            return HttpResponseRedirect(CMBC_TASK_REDIRECT_URL)
        else:
            print form.errors

    form = CMBCTaskForm()
    provinces = CommonDistrictModel.get_districts_by_upid(0)
    return render_to_response('task/cmbc-task.html',
                              context_instance=RequestContext(request, dict_={'provinces': provinces, 'form': form}))

def get_districts_info(request):
    """
    获取地区子级目录信息
    """
    upid = request.GET.get('upid')
    res = CommonDistrictModel.get_districts_by_upid(upid)
    data = json.dumps(res)
    return HttpResponse(data, content_type='text/json')

def ajax_val(request):
    if  request.is_ajax():
        cs = CaptchaStore.objects.filter(response=request.GET['response'],
                                     hashkey=request.GET['hashkey'])
        if cs:
            json_data={'status':1}
        else:
            json_data = {'status':0}
        return JsonResponse(json_data)
    else:
        # raise Http404
        json_data = {'status':0}
        return JsonResponse(json_data)