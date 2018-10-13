from django.db import models

# Create your models here.
class MachineID(models.Model):
    uuid = models.CharField(max_length=255, verbose_name="고유ID", unique=True)
    nickname = models.CharField(max_length=32, verbose_name="닉네임")

    def __str__(self):
        return str(self.nickname)

class TimeTable(models.Model):
    time = models.TimeField(verbose_name="시간")

    def __str__(self):
        return str(self.time)

class Daily(models.Model):
    class Meta:
        unique_together = ('date', 'timetable')
    machine = models.ForeignKey(MachineID, on_delete=models.CASCADE, verbose_name="고유ID")
    date = models.DateField(verbose_name="날짜")
    timetable = models.ForeignKey(TimeTable, on_delete=models.CASCADE, verbose_name="시간")

    def __str__(self):
        return str(self.machine.nickname) +"님의 "+str(self.date)+" - " + str(self.timetable)
