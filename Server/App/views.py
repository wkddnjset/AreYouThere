from django.shortcuts import render
from .models import *
import json, datetime

# Create your views here.
def CreateTimeData(request):
    id = 1
    for i in range(6, 24):
        print(id)
        TimeTable.objects.create(id=id, time=datetime.datetime.strptime(str(i) + ":00", '%H:%M').time())
        TimeTable.objects.create(id=id + 1, time=datetime.datetime.strptime(str(i) + ":30", '%H:%M').time())
        id = id + 2
    for i in range(0, 6):
        TimeTable.objects.create(id=id, time=datetime.datetime.strptime(str(i) + ":00", '%H:%M').time())
        TimeTable.objects.create(id=id + 1, time=datetime.datetime.strptime(str(i) + ":30", '%H:%M').time())
        id = id + 2
    context = {"success": True}
    return render(request, 'create.html')

# ------------------------------------------------------------------
# ClassName   : MainPage
# Description : 메인페이지
# ------------------------------------------------------------------
def MainPage(request):
    return render(request, 'Main/MainPage.html', {})
