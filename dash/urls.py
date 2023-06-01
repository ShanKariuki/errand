from django.urls import path
from .views import *
app_name='dash'

urlpatterns=[
    path('index/',index, name='index'),
]