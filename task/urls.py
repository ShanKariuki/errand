from django.urls import path
from .views import *
app_name='task'
urlpatterns=[
    path('', index , name="index"),
    path('task/', task, name="task"),
    path('create/',create, name='create'),
    path('create/form/',myform,name='form'),
]