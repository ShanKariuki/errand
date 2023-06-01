from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import *
from django.contrib.auth import login, logout, authenticate
def sign_in(request):
    if request.method =='GET':
        if request.user.is_authenticated:
            return redirect('task:index')
        
        form=LoginForm()
        context={'form':form}
        return render(request, 'user/login.html',context)
    elif request.method =="POST":
        form=LoginForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            user=authenticate(request,username=username,password=password)
            if user:
                login(request,user)
                messages.success(request,f'You have logged in succesfully {request.user.username} !!')
                return redirect('task:index')
            
        messages.error(request,f'Please correct the following error')
        return render(request,'user/login.html', {'form':form})
def sign_up(request):
    if request.method =='GET':
        form=RegisterForm()
        context={'form':form}
        return render(request, 'user/sign_up.html', context)
    
    elif request.method =='POST':
        form=RegisterForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.username=user.username.lower()
            user.save()
            messages.success(request,'You have signed up successfully')
            login(request,user)
            return redirect('task:index')
        else:
            return render(request, 'user/sign_up.html',{'form':form})
    

def sign_out(request):
    logout(request)
    messages.success(request, 'You\'ve Logged out successfully')
    return redirect('task:index')
    # return redirect('user:login')
    