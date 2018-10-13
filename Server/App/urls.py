from django.urls import path
from .views import CreateTimeData, MainPage

app_name = "App"
urlpatterns = [
    path('create/time/data', CreateTimeData),
    path('', MainPage, name="main"),
]