from django.shortcuts import render
from task.models import *
def index (request):
 
    tasks=Task.objects.filter(created_by=request.user)
    context={'tasks':tasks}
    return render(request, 'dash/dash.html',context)

