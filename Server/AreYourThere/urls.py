from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('App.urls')),
    path('api/', include('App.urls_api')),
]
