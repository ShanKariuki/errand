from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from . models import *
from .forms import *


def index (request):
    return render(request, 'task/index.html',)

def task (request):
    categories=Category.objects.all()[0:6]
    context={'categories':categories,}
    return render(request, 'task/task.html',context)

def create(request):
    return render(request, 'task/create.html',)

@login_required
def myform(request):
    if request.method == 'GET':
        context={'form':TodoForm()}
        return render(request,'task/form.html',context)
    
    elif request.method =='POST':
        form=TodoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'The list for delivery has been created successfully.')
            return redirect('task:task')
        else:
            messages.error(request, 'Please correct the following errors:')
            return render(request, 'task/form.html')
        
        

