from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('main_app/', include('src.app.urls')),
    path('admin/', admin.site.urls),
]
