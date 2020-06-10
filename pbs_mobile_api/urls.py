from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('_api/_auth/', include('login.urls')),
    path('_api/_so_list/', include('so_list.urls')),
]
