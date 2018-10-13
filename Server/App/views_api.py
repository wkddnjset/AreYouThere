from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
from .models import *
import json, datetime
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# Rest Framework
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *


# jsno 결과 출력
def getContext(status, msg, data=None):
    result = {}
    result['status'] = status
    result['message'] = msg
    result['data'] = data
    return result


# datetime.datetime.now().hour, datetime.datetime.now().minute
def getTime(hour, minite):
    if minite < 30:
        m = "00"
    else:
        m = "30"
    time = str(hour) + ":" + m
    return datetime.datetime.strptime(str(time), '%H:%M').time()


# datetime.datetime.now().year, datetime.datetime.now().month, datetime.datetime.now().day
def getDate(year, month, day):
    date = str(year) + "-" + str(month) + "-" + str(day)
    return datetime.datetime.strptime(str(date), '%Y-%m-%d').date()


# ------------------------------------------------------------------
# ClassName   : getUserAPI
# Description : 유저 정보 가져오기 API
# ------------------------------------------------------------------
@api_view(['POST'])
def getUserAPI(request):
    # MachineID 가져오기
    device_id = request.POST.get('device_id', None)

    # MachineID 존재 여부 확인
    try:
        user = MachineID.objects.get(uuid=device_id)
        context = getContext("success", user.nickname + "님, 환영합니다.")
    except:
        context = getContext("error", "처음 접속 유저")
    return Response(context)


# ------------------------------------------------------------------
# ClassName   : CreateUserAPI
# Description : 유저 생성 API
# ------------------------------------------------------------------
@api_view(['POST'])
def createUserAPI(request):
    device_id = request.POST.get('device_id', None)
    nickname = request.POST.get('nickname', None)

    # MachineID 존재 여부 확인
    try:
        user = MachineID.objects.create(uuid=device_id, nickname=nickname)
        context = getContext("success", user.nickname + "님, 환영합니다.")
    except:
        context = getContext("error", "이미 존재하는 uuid 입니다.")

    return Response(context)


# ------------------------------------------------------------------
# ClassName   : createDailyAPI
# Description : 일과 생성 API
# ------------------------------------------------------------------
@api_view(['POST'])
def createDailyAPI(request):
    device_id = request.POST.get('device_id', None)
    test = request.POST.get('test', None)
    time = getTime(datetime.datetime.now().hour, datetime.datetime.now().minute)
    date = getDate(datetime.datetime.now().year, datetime.datetime.now().month, datetime.datetime.now().day)


    datas = Daily.objects.filter(date=date)
    id_list = []
    for data in datas:
        id_list.append(data.timetable.id)
    if test == '2':
        try:
            Daily.objects.create(machine=MachineID.objects.get(uuid=device_id), timetable=TimeTable.objects.get(time=time), date=date)
            context = getContext("success", "일과 데이터 생성 성공", id_list)
        except:
            context = getContext("error", "데이터 생성 실패", id_list)
    else:
        context = getContext("success", "당일 일과 데이터 가져오기", id_list)

    return Response(context)

