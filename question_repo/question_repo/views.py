from django.shortcuts import HttpResponse,render
import logging
from django.shortcuts import render, HttpResponse, redirect, Http404
from django.core.paginator import Paginator
from django.shortcuts import render
from apps.repo.models import Questions
# apis为settings中Logging配置中的loggers
logger = logging.getLogger('apis')


def logtest(request):
    logger.info("欢迎访问")
    return HttpResponse('0日志测试0')

def test_avator(request):
    return render(request,'test_avator.html')

def index(request):
    # 触发一个404错误
    raise Http404('not exist')

import random
def custom_404(request):
    return render(request, "404.html", {'data': random.randint(1, 100)}, status=404)

def custom_500(request):
    return render(request, "500.html", {'data': random.randint(1, 100)}, status=500)


# 测试分页
# def listing(request):
#     contact_list = Questions.objects.all()
#     paginator = Paginator(contact_list, 25) # Show 25 contacts per page
#
#     page = request.GET.get('page',1)
#     contacts = paginator.page(page)
#     return render(request, 'list.html', {'contacts': contacts})