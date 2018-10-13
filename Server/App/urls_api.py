from django.urls import path
from .views_api import getUserAPI, createUserAPI, createDailyAPI

app_name = "API"
urlpatterns = [
    path('get/user', getUserAPI, name="get-user"),
    path('user', createUserAPI, name="create-user"),

    path('daily', createDailyAPI, name="create-daily"),
]