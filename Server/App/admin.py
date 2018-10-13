from django.contrib import admin
from .models import *

# Register your models here.
# ------------------------------------------------------------------
# TableName   : MachineID
# Description : 기계 ID  테이블
# ------------------------------------------------------------------
@admin.register(MachineID)
class MachineIDAdmin(admin.ModelAdmin):
    list_display = [f.name for f in MachineID._meta.fields]

# ------------------------------------------------------------------
# TableName   : TimeTable
# Description : 시간 테이블
# ------------------------------------------------------------------
@admin.register(TimeTable)
class TimeTableAdmin(admin.ModelAdmin):
    list_display = [f.name for f in TimeTable._meta.fields]

# ------------------------------------------------------------------
# TableName   : Daily
# Description : 하루
# ------------------------------------------------------------------
@admin.register(Daily)
class DailyAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Daily._meta.fields]