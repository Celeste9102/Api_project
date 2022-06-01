from django.shortcuts import render
from Api_app.models import *
# Create your views here.

def v_help(request):
    return render(request,'help.html')

def login(request):
    res = {}
    res["notices"] = list(DB_notice.objects.all().values('content'))[::-1][:2]   # 字典的基本使用，列表下标取值 [::-1][0:2]包左不包右
    print(res)
    return render(request,'login.html',res)