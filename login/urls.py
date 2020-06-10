from django.urls import path
from .views import login, logout

urlpatterns = [
    path('_login/', login),
    path('_logout/', logout),
]