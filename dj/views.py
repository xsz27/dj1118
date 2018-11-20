


import json
from typing import Iterable

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
import datetime,decimal

# Create your views here.
from dj.models import TFilm

# def req_post(request):
#     if request.method == 'GET':
#         return render(request,'acc/log.html')
#     elif request.method =='POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         return HttpResponse('登录成功')
#     else:
#         return HttpResponse('不支持的请求方式')
#
# def movies(request):
#     films = TFilm.objects.all()
#     # import json
#     film_str = json.dumps(films)  #
#     result = to_list(films)
#     films_json = json.dumps(result)
#     return HttpResponse(films_json, content_type='application/json')
#
#
# class User:
#     username = '小明'
#
#
# def obj_to_dict(obj):
#     result = {}
#     if obj:
#
#         keys = vars(obj).keys()
#         if keys:
#             for key in keys:
#                 if not key.startswith('_'):
#
#                     value = getattr(obj, key)
#
#                     if isinstance(value, datetime.datetime):
#                         value = value.strftime('%Y-%m-%H:%i:%s')
#                     # result,update(key=value)
#                     elif isinstance(value, datetime.date):
#                         value = value.strftime('%Y-%m-%d')
#                     elif isinstance(value, decimal.Decimal):
#                         value = float(value)
#                     result[key] = value
#
#     return result
#
#
# def to_list(objects):
#     li = []
#     from collections import Iterable
#     if objects and isinstance(objects, Iterable):
#         for obj in objects:
#             li.append(obj_to_dict(obj))
#     return li



def movies(request):
    try:
        movie = TFilm.objects.all()
        result = to_list(movie)
        data = {
            'status': 200,
            'msg': 'success',
            'data': result
        }
    except:
        data = {'status': 404, 'msg': 'error'}
    return JsonResponse(data)


# 将对象转化成字典对象
def obj_to_dict(obj):
    result = {}
    if obj:
        # 将对象所有属性值,转化成字典形式
        keys = vars(obj).keys()
        if keys:
            for key in keys:
                if not key.startswith('_'):
                    value = getattr(obj, key)
                    if isinstance(value, datetime.datetime):
                        value = value.strftime('%Y-%m-%d %H:%i:%s ')
                    elif isinstance(value, datetime.date):
                        value = value.strftime('%Y-%m-%d')
                    elif isinstance(value, decimal.Decimal):
                        value = float(value)
                    result[key] = value
    return result


# 将QuerySet对象转化列表套字典
def to_list(objects):
    li = []
    if objects and isinstance(objects, Iterable):
        for obj in objects:
            li.append(obj_to_dict(obj))
    return li

def movie():
    try:
        films = TFilm.objects.all()
        result = to_list(films)
        data = {
            'code':200,
            'msg':'success',
            'data':result,
        }
    except:
        data = {'status':404,'msg':'error'}
    return JsonResponse(data)

def log(request):
    return render(request,'log.html')


